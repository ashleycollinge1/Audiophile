CREATE DATABASE IF NOT EXISTS audiophile;
CREATE OR REPLACE USER audiophile@'0.0.0.0' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON  audiophile.* to 'audiophile'@'0.0.0.0' WITH GRANT OPTION;
FLUSH PRIVILEGES;