Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 

import time
from datetime import datetime as dt

# change hosts path according to your OS
hosts_path = "C:\Windows\System32\drivers\etc"
# localhost's IP
redirect = "127.0.0.1"

# websites That you want to block
website_list =
["https://www.cm.com/en-in/"]

while True:

	# time of your work
	if dt(dt.now().year, dt.now().month, dt.now().day,8)
	< dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
		print("Working hours...")
		with open(hosts_path, 'r+') as file:
			content = file.read()
			for website in website_list:
				if website in content:
					pass
				else:
					# mapping hostnames to your localhost IP address
					file.write(redirect + " " + website + "\n")
	else:
		with open(hosts_path, 'r+') as file:
			content=file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)

			# removing hostnmes from host file
			file.truncate()

		print("Fun hours...")
	time.sleep(5)
