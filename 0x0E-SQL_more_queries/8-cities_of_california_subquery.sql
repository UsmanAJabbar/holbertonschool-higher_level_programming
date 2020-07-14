-- Lists out all the cities found in
-- California by running a subquery
SELECT `cities`.id, cities.name
	FROM `states`, `cities`
	WHERE cities.state_id = states.id;
