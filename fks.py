#! /usr/bin/python

import sys, random, time

if len(sys.argv) > 1 and sys.argv[1]=="run" :	
	file = open("/home2/marcos/pacova/ptu.txt","a") 
	while 1:
		ctime = time.strftime('%Y-%m-%d %H:%M:%S')
		p = random.uniform(700, 900)
		rh = random.uniform(50, 99)
		t = random.uniform(10, 40)
		line = "%s P= %.2fhPa  RH=  %.2f%%RH  T=  %.2f'C \r"%(ctime, p, rh, t)
		file.write(line)
		print(line)
		time.sleep(1)
	file.close()
else:
	print("Opcao nao disponivel")
