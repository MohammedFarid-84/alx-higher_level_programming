-- show what not in define show.
SELECT title
    FROM tv_shows WHERE NOT EXISTS (
	SELECT NULL FROM tv_show_genres LEFT JOIN tv_genres
	ON tv_genres.id = tv_show_genres.genre_id
	WHERE tv_shows.id = tv_show_genres.show_id AND tv_genres.name = 'Comedy')
    ORDER BY title;
