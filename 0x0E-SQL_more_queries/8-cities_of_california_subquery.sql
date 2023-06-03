-- Lists all cities of California in hbtn_0d_usa database
SELECT * FROM hbtn_0d_usa.cities WHERE state_id IN (
	SELECT id FROM hbtn_0d_usa.states WHERE name = 'California'
) AS cali_ids;
