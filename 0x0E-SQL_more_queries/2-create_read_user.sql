-- creates the database hbtn_0d_2

CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' identified by 'user_0d_2_pwd';

GRANT SELECT on `hbtn_0d_2`.* to 'user_0d_2'@'localhost';
