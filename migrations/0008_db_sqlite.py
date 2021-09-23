# -*- coding: utf-8 -*-

steps = [
"""
ALTER TABLE Jobs_deleted ADD end_time INTEGER DEFAULT 0
""",
"""
UPDATE Migrations SET database_version = 8
"""
]

