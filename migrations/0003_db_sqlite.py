# -*- coding: utf-8 -*-

# Rename column user since it is a postgresql reserved word

steps = [
"""
ALTER TABLE Jobs RENAME TO Jobs_tmp
""",
"""
CREATE TABLE IF NOT EXISTS Jobs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	parent INT DEFAULT 0,
	title TEXT DEFAULT "",
	command TEXT DEFAULT "",
	dir TEXT DEFAULT ".",
	environment TEXT DEFAULT "",
	state TEXT DEFAULT "WAITING",
	paused BOOLEAN DEFAULT 0,
	worker TEXT DEFAULT "",
	start_time INT DEFAULT 0,
	duration INT DEFAULT 0,
	run_done INT DEFAULT 0,
	timeout INT DEFAULT 0,
	priority UNSIGNED INT DEFAULT 8,
	affinity TEXT DEFAULT "",
	affinity_bits BIGINT DEFAULT 0,
	username TEXT DEFAULT "",
	finished INT DEFAULT 0,
	errors INT DEFAULT 0,
	working INT DEFAULT 0,
	total INT DEFAULT 0,
	total_finished INT DEFAULT 0,
	total_errors INT DEFAULT 0,
	total_working INT DEFAULT 0,
	url TEXT DEFAULT "",
	progress FLOAT,
	progress_pattern TEXT DEFAULT "",
	h_affinity BIGINT DEFAULT 0,
	h_priority UNSIGNED BIGINT DEFAULT 0,
	h_paused BOOLEAN DEFAULT 0,
	h_depth INT DEFAULT 0,
    comments VARCHAR(255))
""",
"""
INSERT INTO Jobs(id, parent, title, command, dir, environment, state, paused, worker, start_time, duration, run_done, timeout, priority, affinity, affinity_bits, username, finished, errors, working, total, total_finished, total_working, url, progress, progress_pattern, h_affinity, h_priority, h_paused, h_depth, comments)
SELECT id, parent, title, command, dir, environment, state, paused, worker, start_time, duration, run_done, timeout, priority, affinity, affinity_bits, user, finished, errors, working, total, total_finished, total_working, url, progress, progress_pattern, h_affinity, h_priority, h_paused, h_depth, comments
FROM Jobs_tmp
""",
"""
DROP TABLE Jobs_tmp
""",
"""
UPDATE Migrations SET database_version = 3
"""
]

