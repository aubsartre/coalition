# -*- coding: utf-8 -*-

_lines = []
_lines.append("BEGIN EXCLUSIVE TRANSACTION;")  # Transactional DDL
_lines.append("CREATE INDEX jobs_unfinished_idx ON Jobs (state) WHERE NOT state = 'FINISHED';")
_lines.append("UPDATE Migrations SET database_version = 9;")
_lines.append("COMMIT TRANSACTION;")
_add_jobs_unfinished_idx_sql = "\n".join(_lines)

steps = [_add_jobs_unfinished_idx_sql]

