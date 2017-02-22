-- From imported db weather info, display average temp by city
-- ordered by temperature descending
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
