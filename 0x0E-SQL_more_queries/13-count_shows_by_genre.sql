-- most genre type in shows
SELECT tv_genres.name, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY name
ORDER BY number_of_shows DESC;
