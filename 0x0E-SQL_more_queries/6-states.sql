-- Creates new database hbtn_0d_usa and new table 'states'
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE hbtn_0d_usa;
CREATE TABLE `states` IF NOT EXISTS (
	id INT PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT,
	name VARCHAR(256)
);
