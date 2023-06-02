-- Lists average temperatures of cities ordered by temperature
SELECT city, AVG(value) AS avg_temp
FROM TABLE temperatures
GROUP BY city
ORDER BY avg_temp DESC;