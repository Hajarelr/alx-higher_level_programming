-- Script that removes all records with score <= 5 in 'second_table'
-- of 'hbtn_0c_0'
-- Database name will be passed as arg to mysql cmd
DELETE FROM second_table
WHERE score <= 5;
