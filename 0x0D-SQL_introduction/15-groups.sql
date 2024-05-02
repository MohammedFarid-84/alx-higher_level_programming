-- count rows and show resultes in a deferent column.
SELECT score, COUNT(score) AS 'number' FROM second_table GROUP BY score ORDER BY score DESC;
