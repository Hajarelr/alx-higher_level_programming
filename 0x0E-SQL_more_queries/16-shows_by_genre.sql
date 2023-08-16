-- Script that lists all shows and genres linked to the show from 'hbtn_0d_tvshows'
-- If a show doesn't have a genre, display NULL in genre column
-- Each record should display tv_shows.title, tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name
SELECT s.title, g.name
FROM tv_shows s
LEFT JOIN tv_show_genres m ON s.id = m.show_id
LEFT JOIN tv_genres g ON m.genre_id = g.id
ORDER BY s.title ASC;
