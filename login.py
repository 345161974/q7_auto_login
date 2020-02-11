# -*- coding:utf-8 -*-

from pywinauto.application import Application
import os
import time
from xml.dom.minidom import parse

if __name__ == '__main__':
	# 加载配置文件
	doc=parse(r'config/broker.xml')
	root = doc.documentElement
	brokers = root.getElementsByTagName('broker')
	# 遍历配置文件
	for broker in brokers:

		# 是否需要确认结算单功能
		settlement_inform = broker.getElementsByTagName('settlement_inform')[0]
		settlement_inform_value = settlement_inform.childNodes[0].data
		print("load_xml settlement_inform_value:", int(settlement_inform_value))

		# 结算单窗口弹出之前延时(s)
		delay_to_settlement = broker.getElementsByTagName('delay_to_settlement')[0]
		delay_to_settlement_value = delay_to_settlement.childNodes[0].data
		print("load_xml delay_to_settlement:", int(delay_to_settlement_value))

		# 快期可执行程序路径
		q7_path = broker.getElementsByTagName('q7_path')[0]
		q7_path_value = q7_path.childNodes[0].data
		print('load_xml q7_path:', q7_path_value)

		# 快期服务器列表索引
		server_index = broker.getElementsByTagName('server_index')[0]
		server_index_value = server_index.childNodes[0].data
		print('load_xml server_index:', server_index_value)

		# 快期登录用户名
		user_id = broker.getElementsByTagName('user_id')[0]
		user_id_value = user_id.childNodes[0].data
		print('load_xml userid:', user_id_value)

		# 快期登录密码
		password = broker.getElementsByTagName('password')[0]
		password_value = password.childNodes[0].data
		print('load_xml password:', password_value)

		# login.py
		# app = Application(backend="uia").start(q7_path_value)
		# 采用win32
		app = Application(backend="win32").start(q7_path_value)
		login_form = app.window(title=r'用户登录', found_index=0)
		# 输出该窗口下的属性(调试模式可以查看)
		# login_form.print_control_identifiers()
		# 选择服务器
		login_form['选择服务器ComboBox'].select(int(server_index_value))
		# 输入期货账户
		login_form['用户代码Edit'].set_text(user_id_value)
		# 输入登录密码
		login_form['交易密码Edit'].set_text(password_value)
		# 登录按钮点击
		login_form['登录Button'].click()

		# 如果需要结算单确认功能
		if int(settlement_inform_value) == 1:
			time.sleep(int(delay_to_settlement_value))
			# 如果是打包版本执行如下代码
			'''开始'''
			# 查找middleware目录下的inform.exe
			dirname = os.path.dirname(os.path.realpath("__file__"))
			filename = os.path.join(dirname, r'middleware/inform.exe')
			os.system(filename)
			'''结束'''

			# 如果是调试版本,执行如下代码
			'''开始'''
			# os.system('python inform.py')
			'''结束'''
