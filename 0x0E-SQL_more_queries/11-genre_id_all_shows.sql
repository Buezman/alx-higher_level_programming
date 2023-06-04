-- Lists all shows contained in the databse hbtn_0d_tvshows
SELECT s.title, sg.genre_id
FROM tv_shows s
LEFT JOIN tv_show_genres sg
ORDER BY s.title, sg.genre_id;
