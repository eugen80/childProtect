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
# check if osd_cat is available
if ! hash osd_cat 2>/dev/null
then
    echo "'osd_cat' was not found in PATH"
    exit 1
fi

# Copy files
if test -d "$basePath"; then
  echo "$basePath already exists"
else
  echo "$basePath does not exist"
  mkdir $basePath
  cp log.sh $basePath/
  cp currentwin.sh $basePath/
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

# Manual tasks
echo "Add to cronjob as root:\n"
echo '* * * * * export DISPLAY=":0.0"; /root/log/log.sh'
echo "\n"

echo "DONE!"
