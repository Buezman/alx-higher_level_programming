-- List tv_shows with linked genre_ids
SELECT s.title, sg.genre_id
FROM tv_shows s
JOIN tv_show_genres sg ON (s.id = sg.show_id)
ORDER BY s.title, sg.genre_id;
