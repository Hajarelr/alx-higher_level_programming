-- Script that creates the DB 'hbtn_0d_usa'
-- If DB already exists the script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create table 'cities' in the DB 'hbtn_0d_usa'
-- id INT unique, auto generated cannot be null & is aprimary key
-- state_id INT not null, foreign key that references id of 'states' table
-- name VARCHAR(256) can't be null
-- If table already exists the script should not fail
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities
(
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (state_id)
		REFERENCES hbtn_0d_usa.states(id)
);
