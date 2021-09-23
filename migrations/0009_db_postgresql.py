# -*- coding: utf-8 -*-

_lines = []
_lines.append("BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;")  # Transactional DDL
_lines.append("CREATE INDEX jobs_unfinished_idx ON jobs (state) WHERE NOT state = 'FINISHED';")  # ~5 mins
_lines.append("UPDATE Migrations SET database_version = 9;")
_lines.append("COMMIT;")
_add_jobs_unfinished_idx_sql = "\n".join(_lines)

steps = [_add_jobs_unfinished_idx_sql]

