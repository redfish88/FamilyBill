#!/usr/bin/env python
# coding:utf-8
#-*- coding: utf-8 -*-
import sys,web
from datetime import datetime
from config import config
from config.urls import urls

db = config.db
render = config.render
tb = 'fee_record'

def get_by_id(id):
	result	= db.select(tb,where='id=$id',vars=locals())
	if not result:
		return False
	return result[0]

class index:
	"""index page to display all bills"""
	def GET(self):
		bills = db.select(tb,order='id desc')
		return render.index(bills)
class new:
	"""add new bill """
	def POST(self):
		bill = web.input()
		print bill
		db.insert(tb,fee=bill.fee,discription=bill.discription,create_time=bill.create_time)
		return web.seeother('/')
				

#db.insert(tb,fee=12.3,DISCRIPTION='测试111',create_time=datetime.now())
#result = db.select(tb,where='id=1')

if __name__ == '__main__':
	app = web.application(urls,globals())
	app.run()