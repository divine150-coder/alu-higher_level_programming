-- List all shows with their total rating sum
-- Sorted by rating descending

SELECT tv_shows.title, IFNULL(SUM(tv_show_ratings.rating), 0) AS rating
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.id
ORDER BY rating DESC;

