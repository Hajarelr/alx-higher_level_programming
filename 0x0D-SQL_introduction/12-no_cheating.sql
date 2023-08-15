-- Script that update score of Bob to 10 from 'second_table' of db 'hbtn_0c_0'
-- Not allowed to use Bob's id value, only name field
-- Database name will be passed as arg to mysql cmd
UPDATE second_table
SET score = 10
WHERE name = "Bob";
