-- creates user by name user_0d_1 @localhost
-- grant user all permissions
-- sets password t user_0d_1_pwd

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' identified by 'user_0d_1_pwd';
GRANT ALL on *.* to 'user_0d_1'@'localhost';
