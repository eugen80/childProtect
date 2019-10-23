#!/bin/bash
shopt -s extglob

current_user=$(whoami)

#/root/log/winlist.sh | while IFS= read -r line ; do
/root/log/currentwin.sh | while IFS= read -r line ; do
### Trim leading whitespaces ###
line="${line##*( )}"

### trim trailing whitespaces  ##
line="${line%%*( )}"

sqlite3 /log.sqlite "INSERT INTO log (window, user) VALUES ('$line', '$current_user')"
done
