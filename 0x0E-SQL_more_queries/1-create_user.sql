-- Script that creates server user 'user_0d_1' with all privileges
-- Password forthe user created 'user_0d_1_pwd'
-- If user already exists, script should not fail
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO user_0d_1@localhost;
