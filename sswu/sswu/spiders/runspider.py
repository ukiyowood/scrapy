from scrapy.spiders import Spider
from sswu.items import MyFirstProjectItem 

class FirstSpider(Spider):
	name = "first"
	allowed_domains = ["sina.com.cn"]
	start_urls = ["http://slide.news.sina.com.cn/s/slide_1_2841_103185.html",
		'http://slide.mil.news.sina.com.cn/k/slide_8_193_45192.html#p=1',
		'http://news.sina.com.cn/pl/2016-09-12/doc-ifxvukhv8147404.shtml'
		]
	"""urls2 = ['http://www.jd.com',
		'http://sina.com.cn',
		'http://yum.iqianyue.com']
	def start_requests(self):
		for url in self.urls2:
			yield self.make_requests_from_url(url)
"""
	def __init__(self,myurl = None,*args,**kwargs):
		super(FirstSpider,self).__init__(*args,**kwargs)
		
		myurllist = myurl.split('|')
		for i in myurllist:
			print("Crawling URLs are: %s"%i)
		self.start_urls = myurllist
		print(myurllist)

	def parse(self,response):
		item = MyFirstProjectItem()
		item["urlname"] = response.xpath("/html/head/title/text()")
		print("Next list the title of crawling URL:")
		print(item["urlname"])