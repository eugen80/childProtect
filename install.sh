#!/bin/bash

basePath="/root/log"

#
# Requirements
#

# check if sqlite is available
if ! hash sqlite3 2>/dev/null
then
    echo "'sqlite3' was not found in PATH"
    exit 1
fi
# check if xdotool is available
if ! hash xdotool 2>/dev/null
then
    echo "'xdotool' was not found in PATH"
    exit 1
fi

#Copy files
mkdir /root/log
cp log.sh /root/log/
cp


# Create sqlite DB
FILE="/log.sqlite"
if test -f "$FILE"; then
    echo "$FILE exist"
    exit 1
else
    echo "$FILE does not exist"
    sqlite3 $FILE < sql/table_log
fi

echo "DONE!"
