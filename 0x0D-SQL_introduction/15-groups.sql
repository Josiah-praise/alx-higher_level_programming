-- List the number of records with the same score in the table second_table
-- Display the score and the number of records for this score with the label number
SELECT `score`, count(*) AS `number` FROM `second_table`
GROUP BY `score` ORDER BY `number` DESC;
