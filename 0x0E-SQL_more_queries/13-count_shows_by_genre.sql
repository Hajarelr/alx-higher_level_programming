-- Script that liists all genres from 'hbtn_0d_tvshows'
-- and display number of shows linked to each
-- Each record should display tv_genres.name, number of shows linked to this genre
-- Don't display a genre that doesn't have any shows list
SELECT tv_genres.name AS genre, COUNT(*) AS number_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_shows DESC;