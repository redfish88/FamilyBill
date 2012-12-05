#!/usr/bin/env python
# coding:utf-8

pre_fix = 'controllers.'

urls = (
	'/'	,					'main.index',
	'/new',					'main.new',
	'/view',				'main.view',
	'/newMember',			'main.newMember',
	'/allMember',			'main.allMember',
	'/search'	,			'main.searchBill',
	'/count'	,			'main.countBill',
	'/del_user/(\d+)',		'main.User_delete',
	'/del_bill/(\d+)',		'main.Bill_delete',
	'/caipiao',				'controllers.seed.caipiao',
	)
