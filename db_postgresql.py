# -*- coding: utf-8 -*-

import psycopg2
from textwrap import dedent

from db_sql import DBSQL


class DBPostgreSQL(DBSQL):

    PRIORITY_MAX_BYTE_DEPTH = 6  # [bytes] Limit for h_priority based on DBMS (un)signed int support

    GET_JOBS_WHERE_QUERY_TEMPLATE = "SELECT Jobs.* FROM Jobs WHERE {0} OFFSET {1} LIMIT {2}"  # for getJobsWhere(), q.v.

    UPDATE_CHILDREN_QUERY_TEMPLATE = dedent("""\
                                            UPDATE Jobs
                                            SET h_depth = {:d}, h_affinity = {:d}, h_priority = {:d}, h_paused = '{:d}'
                                            WHERE id = {:d}
                                            """)  # see _updateChildren(); requires single quote for h_paused bool

    def __init__ (self, host, user, password, database, **kwargs):
        self.logger = kwargs["logger"]
        self.config = kwargs["config"]
        self.cloudconfig = kwargs["cloudconfig"]
        self.Conn = psycopg2.connect(host=host, user=user, password=password, database=database)
        if self.Conn.status != 1:
            raise AssertionError("Connection to postgresql server failed.")
        # super is called *after* because DBSQL inits stuffs in the DB
        super(DBPostgreSQL, self).__init__(self.logger, self.config, self.cloudconfig)

    def _getDatabaseTables(self):
        """Return a list of database tables."""

        cur = self.Conn.cursor()
        req = "SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname NOT IN ('pg_catalog', 'information_schema')"
        self._execute(cur, req)

        return cur.fetchall()

    @staticmethod
    def _jump_scan_sql(table, column, column_has_nulls=True):
        """Return a SQL statement equivalent to SELECT DISTINCT col FROM tbl; but faster in some cases.

        See: https://wiki.postgresql.org/wiki/Loose_indexscan

        In the case where a column has a limited number of values, a loose index/skip/jump scan can be performed
        which is faster than SELECT DISTINCT.  However, Postgres 9.4 doesn't have an equivalent to this, but does
        provide a recursive query that can be orders of magnitide faster than the SELECT DISTINCT.  This fn returns a
        SQL statement that implements this.

        For example,if we scan the jobs table for the users by using:
            SELECT DISTINCT username FROM jobs ORDER BY username;
        Since there are a small number of unique usernames (a few hundred, say), whereas there are hundreds of thousands
        or millions of rows to scan, we could benefit from the use a jump scan, which isn't actually implemented in our
        current (9.4) version of Postgres.  However, we can create the same effect with a special recursive query, that
        this returns. See the link above for more detail.

        Args:
            table (str): the name of a table
            column (str): the name of a column

        Return:
            sql (str): A SQL query to perform the equivalent of a SELECT DISTINCT col from tbl;
        """

        lines = []
        if column_has_nulls:
            lines.append("WITH RECURSIVE t AS (")
            lines.append("  SELECT min({0}) AS {0} FROM {1}".format(column, table))
            lines.append("  UNION ALL")
            lines.append("  SELECT (SELECT min({0}) FROM {1} WHERE {0} > t.{0})".format(column, table))
            lines.append("  FROM t WHERE t.{0} IS NOT NULL".format(column))
            lines.append("  )")
            lines.append("SELECT {0} FROM t WHERE {0} IS NOT NULL".format(column))
            lines.append("UNION ALL")
            lines.append("SELECT null WHERE EXISTS(SELECT 1 FROM {0} WHERE {1} IS NULL)".format(table, column))
            lines.append("ORDER BY {0};".format(column))

        else:
            lines.append("WITH RECURSIVE t AS (")
            lines.append("  (SELECT {0} FROM {1} ORDER BY {0} LIMIT 1)".format(column, table))
            lines.append("  UNION ALL")
            lines.append("  SELECT (SELECT {0} FROM {1} WHERE {0} > t.{0} ORDER BY {0} LIMIT 1)".format(column, table))
            lines.append("  FROM t")
            lines.append("  WHERE t.{0} IS NOT NULL".format(column))
            lines.append("  )")
            lines.append("SELECT {0} FROM t WHERE {0} IS NOT NULL".format(column))
            lines.append("ORDER BY {0};".format(column))

        sql = '\n'.join(lines)

        return str(sql)

    def _execute(self, cur, req, data=None, return_id=False):
        """(Protected) Query the DB with the input request, and data, using the supplied cursor.

        Args:
            cur (?): TODO(AS): type?
            req (str): An SQL query
            data (?): TODO(AS): type?
            return_id (bool): If True, return last row ID, if available

        Return:
            id (int or None): if return_id is True and a last row id is available, return it, else return None
        """

        if return_id:
            req = req if req.lower().rstrip().endswith("returning id") else req + " RETURNING id"

        super(DBPostgreSQL, self)._execute(cur, req, data, return_id=False)

        if return_id:
            row = cur.fetchone()
            id_ = row[0] if row and len(row) > 0 else None

            return id_

    def getJobsUsers(self):
        """Get users."""

        sql = self._jump_scan_sql("jobs", "username")
        cur = self.Conn.cursor()
        self._execute(cur, sql)  # equivalent to "SELECT DISTINCT username FROM Jobs ORDER BY username"

        return [self._rowAsDict (cur, row) for row in cur.fetchall()]

    def getCountJobsWhere(self, where_clause=""):
        """Get the number of matching jobs."""

        # It's illegal Postgres to have ORDER BY in a SELECT COUNT() query; remove
        where_clause = where_clause.partition('ORDER BY')[0]

        return super(DBPostgreSQL, self).getCountJobsWhere(where_clause)
