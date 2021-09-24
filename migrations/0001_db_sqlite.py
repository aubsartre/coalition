# -*- coding: utf-8 -*-

# Add table Migrations
# Set initial database_version

steps = [
"""
CREATE TABLE IF NOT EXISTS Migrations(
    database_version INT)
""",
"""
INSERT INTO Migrations (database_version) VALUES (1)
"""
]


