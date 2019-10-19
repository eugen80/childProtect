#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

def initSqliteConnection():
    connection = None
    try:
        connection = sqlite3.connect("/log.sqlite")
        cursor = connection.cursor()
    except Error as e:
            print(e)
    return cursor