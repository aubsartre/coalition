# -*- coding: utf-8 -*-

# Rename column user since it is a postgresql reserved word

steps = [
"""
ALTER TABLE Jobs CHANGE COLUMN user username TEXT
""",
"""
UPDATE Migrations SET database_version = 3
"""
]

