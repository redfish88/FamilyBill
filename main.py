#!/usr/bin/env python
# coding:utf-8
#-*- coding: utf-8 -*-

__version__  = '0.1'
__author__   = 'lvrenkun'


import sys,web,json,os
from   datetime    import datetime,date
from   config  	   import config
from   config.urls import urls
from   decimal 	   import Decimal
import urllib2,re
from apscheduler.scheduler import Scheduler
app_root = os.path.dirname(__file__)

sys.path.append(app_root)
os.chdir(app_root) 

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

def getBallByTitle(title):
	result = db.select('lottery',where='title=$title',vars=locals())
	if not result:
		return True
	return False

def getDataFromBD():
	try:

		html = urllib2.urlopen('http://www.baidu.com/s?wd=%E5%8F%8C%E8%89%B2%E7%90%83').read()
		reg_unicode = '<meta http-equiv="content-type" content="text/html;charset=(.*?)">'
		#code        = re.compile(reg_unicode).findall(html)
		#html = html.decode('utf-8').encode(sys.getfilesystemencoding())
		reg_title 	 = '<p class="op_caipiao_date">(.*?)</p>'
		reg_redball  = '<span class="op_caipiao_red">(.*?)</span>'
		reg_blueball = '<span class="op_caipiao_green">(.*?)</span>'
		reg_date	 = '<div class="op_caipiao_text" style="font-weight:normal;font-family:simsun;">(.*?)</div>'
		title = re.compile(reg_title).findall(html)
		_title = title[0]
		flag 		 = getBallByTitle(_title)
		if flag:
			redball      = re.compile(reg_redball).findall(html)
			sp           = ','
			_redball     = sp.join(redball)
			blueball     = re.compile(reg_blueball).findall(html)
			_blueball    = blueball[0]
			lotterydate  = re.compile(reg_date).findall(html)
			_lotterydate = lotterydate[0]
			db.insert('lottery',title=_title,redball=_redball,blueball=_blueball,lottery_date=_lotterydate,create_time=datetime.now())
	except Exception, e:
		raise
	else:
		pass
	finally:
		pass
def schedulerCreeper():
	getDataFromBD()
	sched = Scheduler()
	job = sched.add_cron_job(getDataFromBD,day_of_week='0,2,4',hour='22')
	sched.start()

class index:
	"""index page to display all bills"""
	def GET(self):
		sql = 'select a.id,consume_time,fee,discription,name from fee_record a left join member b on a.member_id=b.id order by a.consume_time desc'
		bills = db.query(sql)
		print bills
		return render.index(bills)
	def POST(self):
		sql = 'select a.id,consume_time,fee,discription,name from fee_record a left join member b on a.member_id=b.id order by a.consume_time desc'
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
		db.insert(tbmember,name=member.name,isDelete=0,create_time=datetime.now())
		return web.seeother('/')
class allMember:
	"""docstring for allMember"""
	def POST(self):
		members = db.query("select id,name,create_time from member where isDelete=0 order by create_time").list()
		web.header('Content-Type','application/json')
		print members
		return json.dumps(members,default=dthandle)
	def GET(self):
		return self.POST()
class searchBill:
	"""docstring for searchBill"""

	def POST(self):
		args 	   = web.input()
		begin_time = args.begin_time
		end_time   = args.end_time
		member_id  = int(args.member_id)
		sql		   = 'select a.id,consume_time,fee,discription,name from fee_record a left join member b \
					  on a.member_id = b.id  where 1=1'
		
		if begin_time != '':
			sql = sql + ' and consume_time >= $begin_time'
		if end_time   != '':
			sql = sql + ' and consume_time <= $end_time'
		if member_id  != 0:
			sql = sql + ' and b.id=$member_id'
		sql = sql + ' order by a.consume_time desc'
		bills = db.query(sql,vars=locals()).list()
		web.header('Content-Type','application/json')
		return json.dumps(bills,default=dthandle)
	def get(self):
		return self.POST()	
class User_delete(object):
	"""docstring for User_update"""
	def POST(self,id):
		db.update(tbmember,where='id=$id',isDelete=1,vars=locals())
		return web.seeother('/')
	def GET(self,id):
		return self.POST(id)
class Bill_delete(object):
	"""docstring for User_update"""
	def POST(self,id):
		db.delete(tb,where='id=$id',vars=locals())
		return web.seeother('/')
	def GET(self,id):
		return self.POST(id)
class countBill(object):
	"""docstring for count"""
	def POST(self):
		args 	   = web.input()
		begin_time = args.begin_time
		end_time   = args.end_time
		member_id  = int(args.member_id)
		sql		   = 'select sum(a.fee) as count,name from fee_record a left join member b \
					  on a.member_id = b.id  where 1=1'
		
		if begin_time != '':
			sql = sql + ' and consume_time >= $begin_time'
		if end_time   != '':
			sql = sql + ' and consume_time <= $end_time'
		if member_id  != 0:
			sql = sql + ' and b.id=$member_id'
		sql = sql + ' group by name order by a.consume_time desc'
		bills = db.query(sql,vars=locals()).list()
		web.header('Content-Type','application/json')
		return json.dumps(bills,default =dthandle)
	def GET(self):
		return self.POST()		
		

#db.insert(tb,fee=12.3,DISCRIPTION='测试111',create_time=datetime.now())
#result = db.select(tb,where='id=1')



if __name__ == '__main__':
	app = web.application(urls,globals())
	schedulerCreeper()
	app.run()