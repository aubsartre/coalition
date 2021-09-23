# -*- coding: utf-8 -*-

# Add table Migrations
# Set initial database_version

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

