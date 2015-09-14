#!/usr/bin/env python
# coding:utf-8
#-*- coding: utf-8 -*-
import web,json
from config  import config
import datetime
from   decimal 	   import Decimal

# 注释 11
def dthandle(obj):
	if isinstance(obj,datetime.date):
		return obj.isoformat()
	elif isinstance(obj,Decimal):
	    return float(obj) 

db = config.db
render = config.render
class Report(object):
	"""docstring for Report"""
	def GET(self):
		return render.report()
	def other(self):
		sql = 'select consume_time,sum(fee) fee,b.name from fee_record a,member b \
		  	   where a.member_id = b.id group by consume_time,name order by consume_time'
		dateList = db.query(sql).list()
		datetime = []
		categories = {}
		dict1 = {}
		dict2 = {}
		for d in dateList:
			datetime.append(d.consume_time)
		categories['categories'] = datetime
		data1 = [12,20]
		data2 = [20,30]
		dict1['name'] = '张三'
		dict1['data'] = data1
		dict2['name'] = '李死'
		dict2['data'] = data2

		data = [dict1,dict2]
		categories['series'] = data
	 	web.header('Content-Type','application/json')
	 	return json.dumps(categories,default=dthandle)
	def POST(self):
		week = datetime.timedelta(days =7)
		now = datetime.datetime.now()
		end = now
		start =  datetime.date(2013,01,01)
		begin = now - week
		sql = 'select day from nature_date where  day >= $begin and day <=$end order by day'
		categories = db.query(sql,vars=locals())
		xData = transferList(categories,'day')
		sql = 'select member_id as id,name from fee_record a,member b \
			where a.member_id = b.id \
			      and a.consume_time >= $begin \
			      and a.consume_time <= $end \
			group by a.member_id,name'
		members = db.query(sql,vars=locals()).list()
		dataList = []
		for member in members:
			dataDict = {}
			name = member['name']
			id 	 = member['id']
			dataDict['name'] = name
			sql = 'select day,IFNULL(SUM(fee),0) data  \
			   from nature_date a left join fee_record b \
			    on a.day = b.consume_time and b.member_id = $id\
		 	    where day >= $begin and day <= $end \
		 	    group by day'
			memberFees = db.query(sql,vars=locals())
			data = transferList(memberFees,'data')
			dataDict['data'] = data
			dataDict['name'] = name
			dataList.append(dataDict)		
		resultDict = {'categories':xData,'series':dataList}


		web.header('Content-Type','application/json')
		return json.dumps(resultDict,default=dthandle)

def transferList(_list,column):
	result = []
	try:
		for obj in _list:
			result.append(obj[column])
	except Exception, e:
		print '非法对象'
	finally:
		pass
	return result