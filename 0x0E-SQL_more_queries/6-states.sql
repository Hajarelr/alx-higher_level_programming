-- Script that creates DB 'hbtn_0d_usa'
-- If db already exists, script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create table 'states' in DB 'hbtn_0d_usa'
-- id INT unique auto-generated can't be null and is a primary key
-- name VARCHAR(256) cannot be null
-- If table already exists, script should not fail
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states
(
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
);
