-- Creates new database hbtn_0d_usa and new table 'states'
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE hbtn_0d_usa.states IF NOT EXISTS (
	id INT PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT,
	name VARCHAR(256)
);
