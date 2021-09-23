# -*- coding: utf-8 -*-

# Add column comment on tables Jobs and Workers

steps = [
"""
ALTER TABLE Jobs ADD comments VARCHAR(255)
""",
"""
ALTER TABLE Workers ADD comments VARCHAR(255)
""",
"""
UPDATE Migrations SET database_version = 2
"""
]

