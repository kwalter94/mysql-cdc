CREATE USER 'maxwell'@'%' IDENTIFIED BY 'P@ssw0rd';
CREATE USER 'maxwell'@'localhost' IDENTIFIED BY 'P@ssw0rd';

GRANT ALL ON maxwell.* TO 'maxwell'@'%';
GRANT ALL ON maxwell.* TO 'maxwell'@'localhost';

GRANT SELECT, REPLICATION CLIENT, REPLICATION SLAVE ON *.* TO 'maxwell'@'%';
GRANT SELECT, REPLICATION CLIENT, REPLICATION SLAVE ON *.* TO 'maxwell'@'localhost';