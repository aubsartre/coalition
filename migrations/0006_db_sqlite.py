# -*- coding: utf-8 -*-

steps = [
"""
CREATE TABLE IF NOT EXISTS Jobs_deleted (
    id INTEGER PRIMARY KEY,
    parent INTEGER DEFAULT 0,
    title TEXT,
    command TEXT,
    dir TEXT,
    environment TEXT,
    state TEXT,
    paused BOOLEAN DEFAULT 0,
    worker TEXT,
    start_time INTEGER DEFAULT 0,
    duration INTEGER DEFAULT 0,
    run_done INTEGER DEFAULT 0,
    timeout INTEGER DEFAULT 0,
    priority UNSIGNED INTEGER DEFAULT 8,
    affinity TEXT,
    affinity_bits BIGINT DEFAULT 0,
    username TEXT,
    finished INTEGER DEFAULT 0,
    errors INTEGER DEFAULT 0,
    working INTEGER DEFAULT 0,
    total INTEGER DEFAULT 0,
    total_finished INTEGER DEFAULT 0,
    total_errors INTEGER DEFAULT 0,
    total_working INTEGER DEFAULT 0,
    url TEXT,
    progress FLOAT,
    progress_pattern TEXT,
    h_affinity BIGINT DEFAULT 0,
    h_priority BIGINT DEFAULT 0,
    h_paused BOOLEAN DEFAULT '0',
    h_depth INTEGER DEFAULT 0,
    comments VARCHAR(255),
    max_simultaneous_working_childs INTEGER)
""",
"""
CREATE TABLE IF NOT EXISTS Events_deleted (
    id INTEGER PRIMARY KEY,
    worker VARCHAR(255),
    job_id INT,
    job_title TEXT,
    state TEXT,
    start INT,
    duration INT)
""",
"""
CREATE TABLE IF NOT EXISTS Events_archive (
    id INTEGER PRIMARY KEY,
    worker VARCHAR(255),
    job_id INT,
    job_title TEXT,
    state TEXT,
    start INT,
    duration INT)
""",
"""
CREATE TABLE IF NOT EXISTS Dependencies_deleted (
    job_id INTEGER,
    dependency INTEGER)
""",
"""
CREATE TABLE IF NOT EXISTS Dependencies_archive (
    job_id INTEGER,
    dependency INTEGER)
""",
"""
ALTER TABLE Jobs_archive ADD max_simultaneous_working_childs INTEGER
""",
"""
UPDATE Migrations SET database_version = 6
"""
]

