-- Script that lists all cities of CA that can be found in DB 'hbtn_0d_usa'
-- The 'states' table contains only one record where 'name = California'
-- but 'id' can be different
-- Results must be sorted in ascending order by 'cities.id'
-- Not allowed to use JOIN keyword
SELECT id, name
FROM cities
WHERE state_id = (
      SELECT id
      FROM states
      WHERE name = 'California'
);
