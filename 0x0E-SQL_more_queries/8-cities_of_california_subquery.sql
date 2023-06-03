-- Lists all cities of California in hbtn_0d_usa database
SELECT c.id, c.name FROM hbtn_0d_usa.cities c WHERE c.state_id IN (
	SELECT s.id FROM hbtn_0d_usa.states s WHERE s.name = 'California'
) ORDER BY c.id;
