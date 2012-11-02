#!/usr/bin/env python
# coding:utf-8
import web,os

#数据库连接配置
db = web.database(dbn='mysql',db='family',user='root',pw='admin')
#render 配置
root = os.path.dirname(__file__)
render = web.template.render(os.path.join(root,'..','templates/'))

config = web.storage(
	static = '/static'
	)

web.template.Template.globals['render'] = render
web.template.Template.globals['config'] = config
print render




