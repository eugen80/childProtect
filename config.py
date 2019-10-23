#!/usr/bin/env python
# -*- coding: utf-8 -*-

# config[GROUP]             app group
# config[GROUP][maxMin]     allowed Minutes per day
# config[GROUP][grp]        same groups share 'maxMin'

config = {}
config['fun'] = {}
config['fun']['maxMin'] = 90
config['fun']['apps'] = {}
config['fun']['apps']['minecraft'] = '/usr/bin/java'
config['fun']['apps']['Mozilla Firefox (Privater Modus)'] = '/usr/bin/firefox'
config['fun']['apps']['minetest'] = ''

config['communication'] = {}
config['communication']['maxMin'] = 60
config['communication']['apps'] = {}
config['communication']['apps']['whatsup'] = ''

config['productive'] = {}
config['productive']['maxMin'] = 180
config['productive']['apps'] = {}
config['productive']['apps']['schlaukopf'] = 1

config['misc'] = {}
config['misc']['maxMin'] = 10
config['misc']['apps'] = {}
config['misc']['apps']['konsole'] = '/usr/bin/konsole'
