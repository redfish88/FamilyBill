#!/usr/bin/env python
# coding:utf-8
#-*- coding: utf-8 -*-
import sys,web,json
from   datetime    import datetime,date
from   config  	   import config
from   config.urls import urls
from   decimal 	   import Decimal

db 	     = config.db
render   = config.render
tb 	 	 = 'fee_record'
tbmember = 'member'
def dthandle(obj):
	if isinstance(obj,date):
		return obj.isoformat()
	elif isinstance(obj,Decimal):
	    return str(obj) 
def get_by_id(id):
	result	= db.select(tb,where='id=$id',vars=locals())
	if not result:
		return False
	return result[0]

class index:
	"""index page to display all bills"""
	def GET(self):
		sql = 'select consume_time,fee,discription,name from fee_record a left join member b on a.member_id=b.id order by a.consume_time desc'
		bills = db.query(sql)
		return render.index(bills)
	def POST(self):
		sql = 'select consume_time,fee,discription,name from fee_record a left join member b on a.member_id=b.id order by a.consume_time desc'
		bills = db.query(sql).list()
		web.header('Content-Type','application/json')
		return json.dumps(bills,default=dthandle)
class new:
	"""add new bill """
	def POST(self):
		bill = web.input()
		db.insert(tb,fee=bill.fee,discription=bill.discription,member_id=bill.member,consume_time=bill.consume_time,create_time=datetime.now())
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
		members = db.query("select id,name,create_time from member order by name").list()
		web.header('Content-Type','application/json')
		return json.dumps(members,default=dthandle)
	def GET(self):
		return self.POST()
class searchBill:
	"""docstring for searchBill"""
	def __init__(self, arg):
		super(searchBill, self).__init__()
		self.arg = arg
	def POST(self):
		args 	   = web.input()
		begin_time = args.begin_time
		end_time   = args.end_time
		member_id  = args.member_id
		sql		   = '''select consume_time,fee,discription,name from fee_record a left join member b
				 on a.member_id = b.id order by a.consume_time desc where consume_time >$begin_time
				 and consume_time < $end_time and b.id=$member_id
		      '''

	def get(self):
		return self.POST()	
				

#db.insert(tb,fee=12.3,DISCRIPTION='测试111',create_time=datetime.now())
#result = db.select(tb,where='id=1')

if __name__ == '__main__':
	app = web.application(urls,globals())
	app.run()