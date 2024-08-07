import requests
import json
from urllib.parse import urlencode


class ShopifyRest:
	def __init__(self,site,token,apiVersion="2024-07"):
		self.token = token
		self.site = site
		self.apiVersion = apiVersion
	def headers(self):
		return {
			"X-Shopify-Access-Token": self.token,
			"Content-Type": "application/json",
		}
	def queryString(self,params={}):
		qs = [f"{key}={value}" for key,value in params.items()]
		if len(qs)>0:
			return f"?{'&'.join(qs)}"
		return ""
  
	def url(self,url,params={}): 
		ret = f"https://{self.site}.myshopify.com/admin/api/{self.apiVersion}/{url}.json{self.queryString(params)}"
		print(ret)
		return ret
	def get(self,url,params={}):
		return requests.get(self.url(url,params),headers=self.headers()).json()
	def post(self,url,body={}):
		return requests.post(self.url(url),data=json.dumps(body),headers=self.headers()).json()
	def put(self,url,body={}):
		return requests.put(self.url(url),data=json.dumps(body),headers=self.headers()).json()
	def delete(self,url):
		return requests.delete(self.url(url),headers=self.headers()).status_code\
    