-- use inerr join to show from two tables
SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id
    FROM tv_shows INNER JOIN tv_show_genres
      ON (tv_shows.id = tv_show_genres.show_id)
    ORDER BY tv_shows.title, tv_show_genres.genre_id;