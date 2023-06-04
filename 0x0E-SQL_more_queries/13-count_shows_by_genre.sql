-- Counts shows by genres
SELECT g.name AS genre, COUNT(sg.id) AS number_of_shows
FROM tv_genres g
JOIN tv_show_genres sg
ON (g.id = sg.genre_id)
WHERE number_of_shows > 0
GROUP BY genre
ORDER BY number_of_shows DESC;
