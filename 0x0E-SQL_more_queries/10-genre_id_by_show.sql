-- show that that have at least one genre
select tv_shows.title, tv_show_genres.genre_id
from tv_shows
inner join tv_show_genres
where tv_shows.id = tv_show_genres.show_id
order by tv_shows.title, tv_show_genres.genre_id ASC;

