-- Script that lists all shows without 'Comedy' in 'hbtn_0d_tvshows'
-- The 'tv_genres' table contains only one record where name = Comedy
-- Each record should display tv_shows.title
-- Results must be sorted in ascending order by the show title
SELECT s.title
FROM tv_shows s
WHERE s.title NOT IN (
      SELECT s.title
      FROM tv_shows s
      INNER JOIN tv_show_genres m ON s.id = m.show_id
      INNER JOIN tv_genres g ON m.genre_id = g.id
      WHERE g.name = 'Comedy'
)
ORDER BY s.title ASC;
