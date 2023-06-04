-- Lists all non-comedy shows in the database
SELECT s.title FROM tv_shows s
WHERE s.id NOT IN (
	SELECT sg.show_id FROM tv_show_genres sg
	JOIN tv_genres g
	ON (sg.genre_id = g.id)
	WHERE g.name = 'Comedy'
	)
ORDER BY s.title;
