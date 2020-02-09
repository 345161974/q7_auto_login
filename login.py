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
		# 快期可执行程序路径
		q7_path = broker.getElementsByTagName('q7_path')[0]
		q7_path_value = q7_path.childNodes[0].data
		print('load_xml q7_path:', q7_path_value)

		# 快期登录用户名
		user_id = broker.getElementsByTagName('user_id')[0]
		user_id_value = user_id.childNodes[0].data
		print('load_xml userid:', user_id_value)

		# 快期登录密码
		password = broker.getElementsByTagName('password')[0]
		password_value = password.childNodes[0].data
		print('load_xml password:', password_value)

		# login.py
		app = Application(backend="uia").start(q7_path_value)
		login_form = app.window(title=r'用户登录', found_index=0)
		#login_form.print_control_identifiers()
		# 国贸盘后测试,选择最下方盘后服务器
		# login_form['选择服务器ComboBox'].type_keys("{DOWN}")
		# login_form['选择服务器ComboBox'].type_keys("{DOWN}")
		# 国贸实盘测试,选择最上方电信线路
		login_form['选择服务器ComboBox'].type_keys("{UP}")
		login_form['选择服务器ComboBox'].type_keys("{UP}")
		login_form['用户代码Edit'].set_text(user_id_value)
		# time.sleep(1)
		login_form['交易密码Edit'].set_text(password_value)
		# time.sleep(1)
		login_form['登录Button'].click()
		time.sleep(15)
		# 如果是打包版本执行如下代码
		# 查找middleware目录下的inform.exe
		# dirname = os.path.dirname(os.path.realpath("__file__"))
		# filename = os.path.join(dirname, r'middleware/inform.exe')
		# os.system(filename)

		如果是调试版本,执行如下代码
		os.system('python inform.py')
