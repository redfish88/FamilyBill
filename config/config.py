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
	for d in date:
		print d.consume_time
	print date
if __name__ == '__main__':
	_Test()




