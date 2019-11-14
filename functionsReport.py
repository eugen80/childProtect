#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config as cfg
import functionsDb as fnDb
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def testDebug(grp):
    print "OK, in testDebug"
    sql = "SELECT count(id) FROM log WHERE"
    where = []
    for key, value in cfg.config[grp]['apps'].items():
        where.append("window LIKE '%" + key + "%'")

    whereStr = "(" + " OR ".join(where) + ")"
    sql = (sql + whereStr +
        " AND datetime >= datetime('now', 'localtime', 'start of day', '-10 day')" +
        " AND datetime < datetime('now', 'localtime', 'start of day');")

    cursor = fnDb.initSqliteConnection()
    cursor.execute(sql)
    return cursor.fetchone()[0]

def getMailStr(subj, body):
    d = {
        'subj': subj,
        'body': body
    }
    mailStr = (""
    "<html>"
        "<head></head>"
        "<body>"
            "<h1>{subj}</h1>"
            "<p>{body}</p>"
        "</body>"
    "</html>")
    mailStr = mailStr.format(**d)
    return mailStr

def mailSenden(subj, body, toaddr = cfg.MAILTO):
    html = getMailStr(subj, body)
    text = ""

    msg = MIMEMultipart()
    msg['From'] = cfg.MAILFROM
    msg['To'] = toaddr
    msg['Subject'] = subj

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    server = smtplib.SMTP(cfg.MAILSMTP, 587)
    server.starttls()
    server.login(cfg.MAILFROM, cfg.MAILPASS)
    text = msg.as_string()
    server.sendmail(cfg.MAILFROM, toaddr, text)
    server.quit()

def getUncatApps():
    print "**********************"
    for key, value in cfg.config.iteritems():
        print "GRP: " + key
        for appKey, app in value['apps'].items():
            print 'APP: ' + appKey
#             where.append("window LIKE '%" + key + "%'")
        print ''
    print "**********************"

def getTotalToday(grp = 'all'):
    sql = "SELECT count(id) FROM log"
    where = []
    whereStr = ''

    if grp != 'all':
        for key, value in cfg.config[grp]['apps'].items():
            where.append("window LIKE '%" + key + "%'")
        whereStr = "(" + " OR ".join(where) + ") AND"

    sql = (sql + ' WHERE ' + whereStr +
        " datetime >= datetime('now', 'localtime', 'start of day')" +
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
    sql = "SELECT count(id) FROM log WHERE"
    where = []
    for key, value in cfg.config[grp]['apps'].items():
        where.append("window LIKE '%" + key + "%'")

    whereStr = "(" + " OR ".join(where) + ")"
    sql = (sql + whereStr +
        " AND datetime >= datetime('now', 'localtime', 'start of day', 'weekday 1')" +
        " AND datetime < datetime('now', 'localtime', 'start of day');")

    cursor = fnDb.initSqliteConnection()
    cursor.execute(sql)
    return cursor.fetchone()[0]

def getTotalLastWeek(grp):
    sql = "SELECT count(id) FROM log WHERE"
    where = []
    for key, value in cfg.config[grp]['apps'].items():
        where.append("window LIKE '%" + key + "%'")

    whereStr = "(" + " OR ".join(where) + ")"
    sql = (sql + whereStr +
        " AND datetime >= datetime('2019-11-14', 'localtime', '-13 days', 'weekday 1', 'start of day')" +
        " AND datetime < datetime('2019-11-17', 'localtime', '-7 days', 'weekday 0');")

    cursor = fnDb.initSqliteConnection()
    cursor.execute(sql)
    return cursor.fetchone()[0]

def getTotalThisMonth(grp):
    sql = "SELECT count(id) FROM log WHERE"
    where = []
    for key, value in cfg.config[grp]['apps'].items():
        where.append("window LIKE '%" + key + "%'")

    whereStr = "(" + " OR ".join(where) + ")"
    sql = (sql + whereStr +
        " AND datetime >= datetime('2019-11-14', 'localtime', 'start of month')" +
        " AND datetime < datetime('2019-11-17', 'localtime');")

    cursor = fnDb.initSqliteConnection()
    cursor.execute(sql)
    return cursor.fetchone()[0]

def getTotalLastMonth(grp):
    return 5