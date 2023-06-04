-- Lists all Comedy Shows in hbtn_0d_tvshows database
SELECT s.title FROM tv_shows s
JOIN tv_show_genres sg
ON (s.id = sg.show_id)
JOIN tv_genres g
ON (g.id = sg.genre_id)
WHERE g.name = 'Comedy'
ORDER BY s.title ASC;
