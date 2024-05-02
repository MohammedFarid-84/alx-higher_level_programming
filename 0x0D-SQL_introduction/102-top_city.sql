-- list rows in a maximum three row only (limit) do that.
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city, month HAVING month >= 7 AND month <= 8 ORDER BY avg_temp DESC LIMIT 3;
