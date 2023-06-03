-- List tv_shows with linked genre_ids
SELECT s.title, sg.genre_id
FROM tv_shows s
JOIN tv_show_genres sg ON (s.id = sg.show_id)
JOIN tv_genres g ON (sg.genre_id = g.id)
ORDER BY s.title, sg.genre_id;
