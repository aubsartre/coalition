# -*- coding: utf-8 -*-

# Add the table for the archived jobs

steps = [
"""
CREATE TABLE IF NOT EXISTS Jobs_archive (
	id SERIAL PRIMARY KEY,
	parent INT DEFAULT 0,
	title TEXT,
	command TEXT,
	dir TEXT,
	environment TEXT,
	state TEXT,
	paused BOOLEAN DEFAULT '0',
	worker TEXT,
	start_time INT DEFAULT 0,
	duration INT DEFAULT 0,
	run_done INT DEFAULT 0,
	timeout INT DEFAULT 0,
	priority INT DEFAULT 8,
	affinity TEXT,
	affinity_bits BIGINT DEFAULT 0,
	username TEXT,
	finished INT DEFAULT 0,
	errors INT DEFAULT 0,
	working INT DEFAULT 0,
	total INT DEFAULT 0,
	total_finished INT DEFAULT 0,
	total_errors INT DEFAULT 0,
	total_working INT DEFAULT 0,
	url TEXT,
	progress FLOAT,
	progress_pattern TEXT,
	h_affinity BIGINT DEFAULT 0,
	h_priority BIGINT DEFAULT 0,
	h_paused BOOLEAN DEFAULT '0',
	h_depth INT DEFAULT 0,
	comments VARCHAR(255))

""",
"""
UPDATE Migrations SET database_version = 4
"""
]

