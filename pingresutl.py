#!/usr/bin/python3
import os
import sys

ipadd = sys.argv[1]
task = sys.argv[2]
#print (ipadd)
if (task == "ping"):
	open(ipadd,"w+")
#	open('pingfile', 'w').close()
#	os.system('ping ' + "www.google.com" + ' -c ' + '2' ' >> pingfile')
	os.system('ping ' + str(ipadd) + ' -c ' + '2  >> ' + ipadd)
	f=open(ipadd, "r")
	if f.mode == 'r':
	   contents =f.read()
	   print (contents)
	   open(ipadd, 'w').close()
	   pass
