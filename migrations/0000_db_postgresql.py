# -*- coding: utf-8 -*-

# Initial database setup

steps = [
"""
CREATE TABLE IF NOT EXISTS WorkerAffinities(
	id SERIAL PRIMARY KEY,
	worker_name VARCHAR(255),
	affinity BIGINT DEFAULT 0,
	ordering INT DEFAULT 0)
""",
"""
CREATE TABLE IF NOT EXISTS Jobs(
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
	h_depth INT DEFAULT 0)
""",
"""
CREATE TABLE IF NOT EXISTS Dependencies(
	job_id Int,
	dependency INT)
""",
"""
CREATE TABLE IF NOT EXISTS Workers(
	name VARCHAR(255),
	start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	ip TEXT,
	affinity TEXT,
	state TEXT,
	finished INT,
	error INT,
	last_job INT,
	current_event INT,
	cpu TEXT,
	free_memory INT,
	total_memory int,
	active BOOLEAN)
""",
"""
CREATE TABLE IF NOT EXISTS Events(
	id SERIAL PRIMARY KEY,
	worker VARCHAR(255),
	job_id INT,
	job_title TEXT,
	state TEXT,
	start INT,
	duration INT)
""",
"""
CREATE TABLE IF NOT EXISTS Affinities(
	id INTEGER PRIMARY KEY,
	name TEXT)
""",
"""
CREATE INDEX worker_name_index ON WorkerAffinities(worker_name)
""",
"""
CREATE UNIQUE INDEX name_index ON Workers(name)
""",
"""
CREATE INDEX parent_index ON Jobs(parent)
""",
"""
CREATE INDEX job_id_index ON Dependencies(job_id)
""",
"""
CREATE INDEX dependency_index ON Dependencies(dependency)
""",
"""
CREATE INDEX worker_index ON Events(worker)
""",
"""
CREATE INDEX job_id_name ON Events(job_id)
""",
"""
CREATE INDEX start_name ON Events(start)
""",
]

