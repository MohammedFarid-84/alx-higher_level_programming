-- create new database and new user.
-- grnat the new user read only privilege.
DROP DATABASE IF EXISTS hbtn_0d_2;
CREATE DATABASE hbtn_0d_2;
DROP USER IF EXISTS 'user_0d_2'@'localhost';
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY'user_0d_2_pwd';
GRANT READ ON 'hbtn_0d_2'.* TO 'user_0d_2'@'localhost';
