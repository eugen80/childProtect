#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config as cfg
import functionsDb as fnDb

def getTotalToday(grp):
    sql = "SELECT count(id) FROM log WHERE"
    where = []
    for key, value in cfg.config[grp]['apps'].items():
        where.append("window LIKE '%" + key + "%'")

    whereStr = "(" + " OR ".join(where) + ")"
    sql = (sql + whereStr +
        " AND datetime >= datetime('now', 'localtime', 'start of day')" +
        " AND datetime < datetime('now', 'localtime');")

    cursor = fnDb.initSqliteConnection()
    cursor.execute(sql)
    return cursor.fetchone()[0]

def getTotalYesterday(grp):
    sql = "SELECT count(id) FROM log WHERE"
    where = []
    for key, value in cfg.config[grp]['apps'].items():
        where.append("window LIKE '%" + key + "%'")

    whereStr = "(" + " OR ".join(where) + ")"
    sql = (sql + whereStr +
        " AND datetime >= datetime('now', 'localtime', 'start of day', '-1 day')" +
        " AND datetime < datetime('now', 'localtime', 'start of day');")

    cursor = fnDb.initSqliteConnection()
    cursor.execute(sql)
    return cursor.fetchone()[0]

def getTotalThisWeek(grp):
    return 2

def getTotalLastWeek(grp):
    return 3

def getTotalThisMonth(grp):
    return 4

def getTotalLastMonth(grp):
    return 5