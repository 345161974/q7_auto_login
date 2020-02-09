# -*- coding:utf-8 -*-

from pywinauto.application import Application
import os

if __name__ == '__main__':
	# inform_settlement.py
	#main_win = Application().connect(title=r'丁俊-快期交易系统-CTP-国贸期货-CTP主席盘后查询')
	try:
		main_win = Application().connect(title_re=r'.*快期交易系统*', found_index=0)
	except Exception as e:
		print("登录快期失败! or 网络超时!")
		raise e
	
	set_win = main_win['结算结果确认']
	# print("settlement_win exists:", set_win.exists())
	if set_win.exists() and set_win.is_visible():
		# set_win.print_control_identifiers()
		set_win['确认Button'].click()
		# set_win['取消Button'].click()