-- List all Genres not linked to the show 'Dexter'
SELECT g.name FROM tv_genres g
WHERE g.id NOT IN (
	SELECT g.id FROM tv_genres g
	JOIN tv_show_genres sg
	ON (g.id = sg.genre_id)
	JOIN tv_shows s
	ON (s.id = sg.show_id)
	WHERE s.title = 'Dexter'
	)
ORDER BY g.name ASC;
