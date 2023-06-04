-- Lists all genres of the show Dexter
SELECT g.name FROM tv_genres g
JOIN tv_shows_genres sg
ON (g.id = sg.genre_id)
JOIN tv_shows s
ON (s.id = sg.show_id)
WHERE s.name = 'Dexter'
ORDER BY g.name ASC;
