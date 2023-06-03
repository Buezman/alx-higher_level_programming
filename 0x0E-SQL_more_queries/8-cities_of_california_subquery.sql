-- Lists all cities of California in hbtn_0d_usa database
SELECT c.id, c.name FROM cities c WHERE c.state_id IN 
	(SELECT s.id FROM states s WHERE s.name = 'California') 
ORDER BY c.id;
