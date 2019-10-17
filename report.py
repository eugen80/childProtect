#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Script arguments: group reportType

import sys, getopt
import config as cfg
import sqlite3

reports = {
    'totalToday',
    'totalYesterday',
    'totalThisWeek',
    'totalLastWeek',
    'totalThisMonth',
    'totalLastMonth'
}

number_of_arguments = len(sys.argv)
script_name = sys.argv[0]
grp = sys.argv[1]
report = sys.argv[2]

def initSqliteConnection():
    connection = None
    try:
        connection = sqlite3.connect("/log.sqlite")
        cursor = connection.cursor()
    except Error as e:
            print(e)
    return cursor

def getTotalToday(grp):
    sql = "SELECT count(id) FROM log WHERE"
    where = []
    for key, value in cfg.config[grp]['apps'].items():
        where.append("window LIKE '%" + key + "%'")

    whereStr = "(" + " OR ".join(where) + ")"
    sql = (sql + whereStr +
        " AND datetime >= datetime('now', 'localtime', 'start of day')" +
        " AND datetime < datetime('now', 'localtime');")

    cursor = initSqliteConnection()
    cursor.execute(sql)
    return cursor.fetchone()[0]

for key, value in cfg.config.iteritems():
    if key == grp:
        print "Gruppe: " + grp
        if report in reports:
            print "Report: " + report
            #print "Minuten: " + str(getTotalToday(grp))
        else:
            print "Report " + report + " gibt es nicht"