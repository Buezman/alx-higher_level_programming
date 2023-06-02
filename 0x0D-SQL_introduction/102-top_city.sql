-- Lists top 3 cities with highest average temperatures between July and August
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month IN ('july', 'august')
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
