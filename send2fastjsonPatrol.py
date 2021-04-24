#encoding=utf-8

#the reason of not using requests.post is because it will send plenty of payloads to those servers not using json

import requests

#headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36","Content-Type":"application/json"}

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}

proxies = {"http":"http://127.0.0.1:8080","https":"http://127.0.0.1:8080"}

#body = '{"uid": "1337"}'

with open("urls.txt","r") as f:
	for line in f:
		print(line)
		try:
			r = requests.get(url=line,headers=headers,proxies=proxies,verify=False,allow_redirects=False,timeout=3)
		except:
			pass
		
