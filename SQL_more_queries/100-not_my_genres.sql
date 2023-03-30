-- SQL script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT g.name
FROM tv_genres g
WHERE g.name NOT IN (SELECT g.name AS name
                     FROM tv_shows s INNER JOIN tv_show_genres sg
                       ON s.id = sg.show_id
                       INNER JOIN tv_genres g
                       ON sg.genre_id = g.id
                       WHERE s.title = 'Dexter')
ORDER BY g.name asc;
