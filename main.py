#!/usr/bin/env python
# coding:utf-8
#-*- coding: utf-8 -*-
import sys,web,json
from   datetime    import datetime
from   config  	   import config
from   config.urls import urls

db 	     = config.db
render   = config.render
tb 	 	 = 'fee_record'
tbmember = 'member'

def get_by_id(id):
	result	= db.select(tb,where='id=$id',vars=locals())
	if not result:
		return False
	return result[0]

class index:
	"""index page to display all bills"""
	def GET(self):
		sql = 'select a.consume_time,fee,discription,name from fee_record a left join member b on a.member_id=b.id order by a.consume_time desc'
		bills = db.query(sql)
		print bills[0]
		return render.index(bills)
class new:
	"""add new bill """
	def POST(self):
		bill = web.input()
		db.insert(tb,fee=bill.fee,discription=bill.discription,member_id=bill.member,consume_time=bill.create_time,create_time=datetime.now())
		return web.seeother('/')
class newMember:
	"""add new memeber"""
	def POST(self):
		member =	web.input()
		db.insert(tbmember,name=member.name,create_time=datetime.now())
		return web.seeother('/')
class allMember:
	"""docstring for allMember"""
	def POST(self):
		members = db.query("select id,name from member order by name").list()
		web.header('Content-Type','application/json')
		print members
		return json.dumps(members)
	def GET(self):
		return self.POST()
				

#db.insert(tb,fee=12.3,DISCRIPTION='测试111',create_time=datetime.now())
#result = db.select(tb,where='id=1')

if __name__ == '__main__':
	app = web.application(urls,globals())
	app.run()