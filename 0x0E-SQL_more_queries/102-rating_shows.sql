-- tv shows with their corresponding total rating
select tv_shows.title, SUM(tv_show_ratings.rate) AS rating 
from tv_shows
join tv_show_ratings
on tv_shows.id = tv_show_ratings.show_id
group by tv_shows.title
order by rating desc;
