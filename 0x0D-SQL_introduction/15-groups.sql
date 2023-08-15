-- Script that lists number of records with same score in 'second_table'
-- of db 'hbtn_0c_0'
-- The result should display the score and
-- the number of records for this score with label 'number'
-- The loist should be sorted by number of records descending
-- Database name will be passed as arg to mysql cmd
SELECT score, COUNT(1) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
