-- Lists all non-comedy shows in the database
SELECT s.title FROM tv_shows s
JOIN tv_show_genres sg
ON (s.id = sg.show_id)
JOIN tv_genres g
ON (g.id = sg.genre_id)
WHERE g.name <> 'Comedy'
ORDER BY s.title;
