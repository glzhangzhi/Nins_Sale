import random
import time

import requests
from lxml import etree


def GetHTML(url, interval=5):
	headers = {
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
		"Accept-Encoding": "gzip, deflate, br", 
		"Accept-Language": "zh-CN,zh;q=0.9,de-DE;q=0.8,de;q=0.7,en-US;q=0.6,en;q=0.5,zh-TW;q=0.4", 
		"Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"", 
		"Sec-Ch-Ua-Mobile": "?0", 
		"Sec-Ch-Ua-Platform": "\"Windows\"", 
		"Sec-Fetch-Dest": "document", 
		"Sec-Fetch-Mode": "navigate", 
		"Sec-Fetch-Site": "cross-site", 
		"Sec-Fetch-User": "?1", 
		"Upgrade-Insecure-Requests": "1", 
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36", 
		"X-Amzn-Trace-Id": "Root=1-6590a04e-308fcbd366b9de10367c8d7e"
	}
	r = requests.get(url, headers=headers)
	r.raise_for_status()
	time.sleep(interval)
	r.encoding = 'UTF-8'
	html = etree.HTML(r.text)
	return html

