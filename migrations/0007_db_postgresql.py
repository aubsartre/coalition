# -*- coding: utf-8 -*-

steps = [
"""
ALTER TABLE Jobs ADD COLUMN end_time INTEGER DEFAULT 0
""",
"""
ALTER TABLE Jobs_archive ADD COLUMN end_time INTEGER DEFAULT 0
""",
"""
UPDATE Migrations SET database_version = 7
"""
]
