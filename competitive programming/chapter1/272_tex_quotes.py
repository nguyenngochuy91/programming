# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 15:47:01 2019

@author: Huy Nguyen
"""
c = 0
while True:
	try :
		n = input()
	except EOFError:
		break	
	
	a = []
	for i in n:
		if i == "\"":
			if c == 0:
				a.append("``")
				c = 1
			else:
				a.append("''")
				c = 0
		else:
			a.append(i)
	print("".join(a))