#!/usr/bin/env python
# coding:utf-8
import web,os

#数据库连接配置
db = web.database(host='127.0.0.1',dbn='mysql',db='family',user='root',pw='admin')
#render 配置
root = os.path.dirname(__file__)
render = web.template.render(os.path.join(root,'..','templates/'))

config = web.storage(
	static = '/static'
	)

web.template.Template.globals['render'] = render
web.template.Template.globals['config'] = config

def _Test():
		sql = 'select consume_time from fee_record group by consume_time'
		date = db.query(sql).list()
		datetime = []
		categories = {}
		dict1 = {}
		dict2 = {}
		for d in date:
			datetime.append(d.consume_time)
		categories['categories'] = datetime
		data1 = [12,20]
		data2 = [20,30]
		dict1['张三'] = data1
		dict2['李斯'] = data2

		data = [dict1,dict2]
		categories['series'] = data
		print categories

def _NatureInsert():
	import datetime
	print datetime.datetime.now()
	step = datetime.timedelta(days =1)
	week = datetime.timedelta(days =7)
	now = datetime.datetime.now()
	end = now
	start =  datetime.date(2013,01,01)
	begin = now - week

	end = datetime.date(2014,01,01)
	while start < end:
		str_date = start.strftime('%Y-%m-%d')
		dateList = str_date.split('-')
		year = dateList[0]
		month = dateList[1]
		db.insert('nature_date',day = start,year=year,month=month)
	 	start  = start + step

def _natureSelect():
	import datetime

	week = datetime.timedelta(days =7)
	now = datetime.datetime.now()
	end = now
	start =  datetime.date(2013,01,01)
	begin = now - week
	sql = 'select day from nature_date where day <= $now and day >= $begin order by day'
	categories = db.query(sql,vars=locals())
	print categories
	for item in categories:
		print item['day']
	sql = 'select member_id as id,name from fee_record a,member b \
			where a.member_id = b.id \
			      and a.consume_time >= $begin \
			      and a.consume_time <= $now \
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
		 	    where day > $begin and day < $end \
		 	    group by day'
		memberFees = db.query(sql,vars=locals())
		data = transferList(memberFees,'data')
		dataDict['name'] = name
		dataDict['data'] = data
		dataList.append(dataDict)
	print len(dataList)

def transferList(_list,column):
	result = []
	try:
		for obj in _list:
			fee = obj[column]
			print(type(fee))
			result.append(obj[column])
	except Exception, e:
		print '非法对象'
	finally:
		pass
	return result
			 


if __name__ == '__main__':
	#NatureInsert()
	_natureSelect()



