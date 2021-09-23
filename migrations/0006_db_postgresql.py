# -*- coding: utf-8 -*-

steps = [
"""
CREATE TABLE IF NOT EXISTS Jobs_deleted (
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
	comments VARCHAR(255),
	max_simultaneous_working_childs INTEGER)
""",
"""
CREATE TABLE IF NOT EXISTS Events_deleted (
	id SERIAL PRIMARY KEY,
	worker VARCHAR(255),
	job_id INT,
	job_title TEXT,
	state TEXT,
	start INT,
	duration INT)
""",
"""
CREATE TABLE IF NOT EXISTS Events_archive (
	id SERIAL PRIMARY KEY,
	worker VARCHAR(255),
	job_id INT,
	job_title TEXT,
	state TEXT,
	start INT,
	duration INT)
""",
"""
CREATE TABLE IF NOT EXISTS Dependencies_deleted (
	job_id Int,
	dependency INT)
""",
"""
CREATE TABLE IF NOT EXISTS Dependencies_archive (
	job_id Int,
	dependency INT)
""",
"""
ALTER TABLE Jobs_archive ADD COLUMN max_simultaneous_working_childs INTEGER
""",
"""
UPDATE Migrations SET database_version = 6
"""
]

