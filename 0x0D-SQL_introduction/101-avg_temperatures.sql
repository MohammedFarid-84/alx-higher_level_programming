-- list average of fahrinhit temprure.
SELECT city, SUM(value) / COUNT(value) AS 'avg_temp' FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
