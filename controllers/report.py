#!/usr/bin/env python
# coding:utf-8
#-*- coding: utf-8 -*-

from config  import config

db = config.db
render = config.render
class Report(object):
	"""docstring for Report"""
	def GET(self):
		return render.report()
	def POST(self):
		date = db.select('fee_record',what='consume_time',group='consume_time')
		web.header('Content-Type','application/json')
		return 	self.GET()

