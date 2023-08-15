-- Import in hbtn_0c_0 database a table dump
-- Using the same data from task 18
-- Script that displays the max temperature of each state
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
LIMIT 3;
