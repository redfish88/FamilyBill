#!/usr/bin/env python
# coding:utf-8

import random
import web,json



def create():
	red  = random.sample(range(1,34),6)
	red.sort()
	blue = random.sample(range(1,17),1)

	return {'red':red,'blue':blue}

class caipiao(object):
	"""docstring for caipiao"""
	def POST(self):
		web.header('Content-Type','application/json')
		return json.dumps(create())

	def GET(self):
		return self.POST()
	
		