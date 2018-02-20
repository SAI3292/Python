import time
from datetime import datetime as dt

host_path="/etc/hosts"
redirect="127.0.0.1"
web_list=["www.facebook.com","facebook.com"]

while True:
	if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18):
		print("working hours...")
		with open(host_path,'r+') as file:
			content = file.read()
			print(content)
			for web in web_list:
				if web in content:
					pass
				else:
					file.write(redirect+" "+web+"\n")
	else:
		print("fun time")
		with open(host_path,'r+') as file:
			content = file.readlines()
			file.seek(0)
			for line in content:
				if not any(web in line for web in web_list):
					file.write(line)
			file.truncate()
	time.sleep(5)
