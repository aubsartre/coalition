# -*- coding: utf-8 -*-

steps = [
"""
ALTER TABLE Jobs ADD COLUMN max_simultaneous_working_childs INTEGER
""",
"""
UPDATE Migrations SET database_version = 5
"""
]

