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
  mkdir -v $basePath
  cp -v log.sh $basePath/
  cp -v currentwin.sh $basePath/
  cp -v functionsReport.py $basePath/
  cp -v reportMail.py $basePath/
  cp -v config.py $basePath/
  mkdir -v $basePath/reports
  cp -v reports/fun-min-today-sum.sh $basePath/reports
fi

# Create sqlite DB
FILE="/log.sqlite"
if test -f "$FILE"; then
    echo "$FILE exist"
    exit 1
else
    echo "$FILE does not exist"
    echo "try to create $FILE"
    sqlite3 $FILE < sql/table_log
fi

# Manual tasks
echo "1. Add your mail credentials to config.py"
echo "2. Add to cronjob as root:"
echo 'MAILTO=""'
echo '* * * * * export DISPLAY=":0.0"; /root/log/log.sh'
echo '* * * * * export DISPLAY=":0.0"; /root/log/log.sh'

echo "DONE!"
