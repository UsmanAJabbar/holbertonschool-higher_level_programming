-- Extracts information from the database and
-- returns all rows that contain at least a name
SELECT score, name FROM second_table WHERE `name` IS NOT NULL ORDER BY `second_table`.`score` DESC;   
