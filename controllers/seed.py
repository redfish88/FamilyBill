#!/usr/bin/env python
# coding:utf-8
#-*- coding: utf-8 -*-

import random,sys,os
import web,json

from datetime import datetime

from config  import config


db = config.db
render = config.render
tb = 'lottery'

#db = web.database(dbn='mysql',db='family',user='root',pw='admin')

def getBallByTitle(title):
	result = db.select(tb,where='title=$title',vars=locals())
	if not result:
		return True
	return False

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
		sql = 'select id,title,redball,blueball,lottery_date from lottery order by create_time desc'
		lotterys = db.query(sql)
		return render.lottery(lotterys)
			
