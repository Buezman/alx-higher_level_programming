-- List all cities by state using JOIN
SELECT c.id, c.name, s.name
FROM cities c
JOIN states s ON (c.state_id = s.id)
ORDER BY c.id;
