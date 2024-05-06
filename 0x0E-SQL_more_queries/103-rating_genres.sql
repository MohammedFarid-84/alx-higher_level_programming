-- sum rateing query by genres
SELECT tv_genres.name AS name, SUM(tv_show_ratings.rate) AS rating
    FROM tv_genres LEFT JOIN (tv_show_genres, tv_show_ratings)
      ON tv_genres.id = tv_show_genres.genre_id
         AND tv_show_ratings.show_id = tv_show_genres.show_id
    GROUP BY name ORDER BY rating DESC;
