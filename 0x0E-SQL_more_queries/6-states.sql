-- Creates new database hbtn_0d_usa and new table 'states'
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE hbtn_0d_usa.states IF NOT EXISTS (
	PRIMARY KEY(id),
	id INT NOT NULL	UNIQUE AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL
);
