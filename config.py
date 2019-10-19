#!/usr/bin/env python
# -*- coding: utf-8 -*-

# config[GROUP]             app group
# config[GROUP][maxMin]     allowed Minutes per day
# config[GROUP][grp]        same groups share 'maxMin'

config = {}
config['fun'] = {}
config['fun']['maxMin'] = 90
config['fun']['apps'] = {}
config['fun']['apps']['minecraft'] = 1
config['fun']['apps']['youtube'] = 1
config['fun']['apps']['minetest'] = 1

config['communication'] = {}
config['communication']['maxMin'] = 60
config['communication']['apps'] = {}
config['communication']['apps']['whatsup'] = 1

config['productive'] = {}
config['productive']['maxMin'] = 180
config['productive']['apps'] = {}
config['productive']['apps']['schlaukopf'] = 1

config['misc'] = {}
config['misc']['maxMin'] = 180
config['misc']['apps'] = {}
config['misc']['apps']['konsole'] = 1
