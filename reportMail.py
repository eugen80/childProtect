#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, getopt
import config as cfg
import functionsReport as fnRep

mailBody = ''

for key, value in cfg.config.iteritems():
    grpName = key
    if 'maxMin' in value:
        grpLimit = value['maxMin']

    todayMins = fnRep.getTotalToday(grpName)
    leftMins = grpLimit - todayMins

    mailBody +=  "<strong>" + grpName + ":</strong> " + str(todayMins) + " / " + str(grpLimit) + "<br>"

    if leftMins <= 0:
        mailBody += "Keine Zeit mehr!" + "<br>"
        for appKey, appVal in value['apps'].iteritems():
            mailBody += appKey + ' ' + appVal
#             disableApp(appVal)
#     else:
#         mailBody += "Noch: " + str(leftMins) + "\n"

fnRep.mailSenden('Info', mailBody)