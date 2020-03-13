#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from socket import gethostbyname

def getip():
	DOMAIN = "./targets.txt"
	with open(DOMAIN,'r') as f:
		 for line in f.readlines():
			try:
				host = gethostbyname(line.strip('\n'))  #域名反解析得到的IP
			except Exception as e:
				with open('error.txt','a+') as ERR:  #error.txt为没有IP绑定的域名
					ERR.write(line.strip()+ '\n')
			else:
				with open('output.txt','a+') as r: #  ****.txt 里面存储的是批量解析后的结果
					print(host)
					r.write(line.strip() + ',')
					r.write(host + '\n')


len=[]
len1=[]
len2=[]
len3=[]
len4=[]


def opt2File0(paths):
	try:
		f = open('output1.txt','a')
		f.write(paths+'\n')
	finally:
		f.close()


def opt2File2(paths):
	try:
		f = open('output2.txt','a')
		f.write(paths+'\n')
	finally:
		f.close()



def opt2File3(paths):
	try:
		f = open('output3.txt','a')
		f.write(paths+'\n')
	finally:
		f.close()

def opt2File4(paths):
	try:
		f = open('output4.txt','a')
		f.write(paths+'\n')
	finally:
		f.close()






def ipuniq():
	file1 = open("output.txt")
	for text1 in file1.readlines():
		targets1=text1.split(',')
		data2= targets1[1]
		data2 = data2.strip('\n')
		text1 = text1.strip('\n')
		if data2 in len:
			continue
		else:
			len.append(data2)
			opt2File0(text1)



def domainuniq():
	file1 = open("output1.txt")
	for text1 in file1.readlines():
		targets1=text1.split(',')
		data2= targets1[0]
		data2 = data2.strip('\n')
		text1 = text1.strip('\n')
		if data2 in len2:
			continue
		else:
			len2.append(data2)
			opt2File2(text1)



def ipin():
	file1 = open("output2.txt")
	for text1 in file1.readlines():
		targets1=text1.split(',')
		data2= targets1[1]
		data3= targets1[0]
		t1 = text1.strip('\n')
		data2 = data2.strip('\n')
		q2 = data2.split('.')
		if q2[0]=='192' and q2[1]=='168':
			continue
		elif q2[0]=='172' and q2[1]=='16':
			continue
		elif q2[0]=='10':
			continue
		else:
			opt2File3(t1)



def blackuniq():
	file = open("blacklist.txt")
	for text in file.readlines():
		data1 = text.strip('\n')
		len4.append(data1)
	file1 = open("output3.txt")
	for text1 in file1.readlines():
		targets1=text1.split(',')
		data2 = targets1[1]
		data3 = targets1[0]
		data2 = data2.strip('\n')
		if data2 in len4 :
			continue
		else:
			opt2File4(data3)



if __name__ == '__main__':
	getip()
	ipuniq()
	domainuniq()
	ipin()
	blackuniq()