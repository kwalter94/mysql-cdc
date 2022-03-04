CREATE DATABASE foobar;

CREATE USER 'app-user'@'%' IDENTIFIED BY 'P@ssw0rd';
CREATE USER 'app-user'@'localhost' IDENTIFIED BY 'P@ssw0rd';

GRANT ALL ON foobar.* TO 'app-user'@'%';
GRANT ALL ON foobar.* TO 'app-user'@'localhost';

USE foobar;

CREATE TABLE foobar (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    message VARCHAR(4096),
    created_at DATETIME NOT NULL DEFAULT NOW()
);
