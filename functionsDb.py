#!/usr/bin/env python
# -*- coding: utf-8 -*-

def initSqliteConnection():
    connection = None
    try:
        connection = sqlite3.connect("/log.sqlite")
        cursor = connection.cursor()
    except Error as e:
            print(e)
    return cursor