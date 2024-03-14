-- join corresponding states with their cities
SELECT id, name, states.name 
FROM cities NATURAL JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;
