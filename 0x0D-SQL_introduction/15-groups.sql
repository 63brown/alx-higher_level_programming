-- a script that lists the number of records with the same score in the table second_table
-- The list should be sorted by the number of records (descending)
-- result should display: score, number of records for this score with the label number

SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score ORDER BY number DESC;
