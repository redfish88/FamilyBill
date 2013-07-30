#!/usr/bin/env python
# coding:utf-8
#-*- coding: utf-8 -*-

from config  import config

render = config.render
class Report(object):
	"""docstring for Report"""
	def GET(self):
		return render.report()
	def POST(self):
		return self.GET()		