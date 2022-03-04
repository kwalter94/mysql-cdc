#!/bin/bash

while true; do
    message=$(/usr/games/fortune)
    echo "Saving message '$message' to MySQL"
    mysql -u $DB_USER --password=$DB_PASSWORD --host=mysql --database=foobar -e "INSERT INTO foobar (message) VALUES (\"$message\")"
    
    sleep 1
done
