import random
from sswu.settings import IPPOOL
from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware

class IPPOOLS(HttpProxyMiddleware):
	def __init__(self,ip = ''):
		self.ip = ip
	def process_request(self,request,spider):
		thisip = random.choice(IPPOOL)
		print("Now IP is: " + thisip['ipaddr'])
		request.meta['proxy'] = 'http://' + thisip['ipaddr']