-- List number of records with same score in 'second_table'
-- of db 'hbtn_0c_0'
-- Result should display the score and
-- number of records for this score with label 'number'
-- List should be sorted by number of records descending
-- db name will be passed as arg to mysql cmd
SELECT score, COUNT(1) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
