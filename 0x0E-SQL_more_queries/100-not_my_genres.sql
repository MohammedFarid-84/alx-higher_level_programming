-- show what not in define show.
SELECT tv_genres.name AS name
    FROM tv_genres WHERE NOT EXISTS (
	SELECT NULL FROM tv_show_genres LEFT JOIN tv_shows
	ON tv_shows.id = tv_show_genres.show_id
	WHERE tv_genres.id = tv_show_genres.genre_id AND
	      tv_shows.title = 'Dexter')
    ORDER BY name;
