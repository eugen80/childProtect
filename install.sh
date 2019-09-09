#!/bin/bash

# check if sqlite is available
if ! hash sqlite3 2>/dev/null
then
    echo "'sqlite3' was not found in PATH"
    exit 1
fi


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
