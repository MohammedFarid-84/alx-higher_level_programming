-- list all values that have a value in a name column.
SELECT score, name FROM second_table WHERE name <> '' ORDER BY score DESC;
