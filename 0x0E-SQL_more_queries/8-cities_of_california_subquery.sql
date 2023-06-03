-- Lists all cities of California in hbtn_0d_usa database
SELECT * FROM hbtn_0d_usa.cities c WHERE c.state_id IN (
	SELECT id FROM hbtn_0d_usa.states s WHERE s.name = 'California'
) AS cali_ids;
