-- Lists all genres according to their ratings
SELECT g.name, SUM(r.rate) AS rating
FROM tv_genres g
JOIN tv_show_genres sg
ON (g.id = sg.genre_id)
JOIN tv_show_ratings r
ON (r.show_id = sg.show_id)
GROUP BY g.name
ORDER BY rating DESC;
