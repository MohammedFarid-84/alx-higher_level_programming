-- show count of show genner.
SELECT tv_shows.title AS title
    FROM tv_shows LEFT JOIN (tv_genres, tv_show_genres)
      ON (tv_genres.id = tv_show_genres.genre_id AND tv_shows.id = tv_show_genres.show_id)
    WHERE tv_genres.name = 'Comedy'
    ORDER BY tv_shows.title;
