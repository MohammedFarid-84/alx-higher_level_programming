-- show count of show genner.
SELECT tv_shows.title AS title, tv_genres.name AS name
    FROM tv_shows LEFT JOIN (tv_genres, tv_show_genres)
      ON (tv_genres.id = tv_show_genres.genre_id AND tv_shows.id = tv_show_genres.show_id)
    ORDER BY tv_shows.title, tv_genres.name;
