#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Script arguments: group reportType

import sys, getopt
import config as cfg
import functionsReport as fnRep

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

for key, value in cfg.config.iteritems():
    if key == grp:
        print "Gruppe: " + grp
        if report in reports:
            repUp = report[0].upper() + report[1:]
            print "Report: " + repUp

            # Den Funktionsnamen dynamisch zusammenbauen und aufrufen
            print "Minuten: " + str(getattr(fnRep, "get%s" % repUp)(grp))
        else:
            print "Report " + report + " gibt es nicht"