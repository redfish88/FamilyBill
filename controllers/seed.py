#!/usr/bin/env python
# coding:utf-8
#-*- coding: utf-8 -*-

import random,sys,os
import web,json
import urllib2,re
import web
from datetime import datetime

from config  import config


db = config.db
render = config.render
tb = 'lottery'

#db = web.database(dbn='mysql',db='family',user='root',pw='admin')

def getBallByTitle(title):
	result = db.select(tb,where='title=$title',vars=locals())
	print result[0]
	if not result:
		return True
	return False

def getDataFromBD(url):
	html = urllib2.urlopen(url).read()
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
	print _title
	print flag
	if flag:
		redball      = re.compile(reg_redball).findall(html)
		sp           = ','
		_redball     = sp.join(redball)
		blueball     = re.compile(reg_blueball).findall(html)
		_blueball    = blueball[0]
		lotterydate  = re.compile(reg_date).findall(html)
		_lotterydate = lotterydate[0]
		db.insert(tb,title=_title,redball=_redball,blueball=_blueball,lottery_date=_lotterydate,create_time=datetime.now())

#随即双色球
def create():
	red  = random.sample(range(1,34),6)
	red.sort()
	blue = random.sample(range(1,17),1)
	return {'red':red,'blue':blue}

class lottery(object):
	"""随即一注"""
	def POST(self):
		web.header('Content-Type','application/json')
		return json.dumps(create())
	"""获取各期中奖球数"""
	def GET(self):
		getDataFromBD('http://www.baidu.com/s?wd=%E5%8F%8C%E8%89%B2%E7%90%83')
		sql = 'select id,title,redball,blueball,lottery_date from lottery order by create_time desc'
		lotterys = db.query(sql)
		return render.lottery(lotterys)
			
