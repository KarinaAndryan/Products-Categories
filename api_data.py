import requests
import sys
import time
import key

class Request:
	def __init__(self, url, headers, params):
		self.url_ = url
		self.headers_ = headers
		self.params_ = params

	def post_request(self):
		print('Post request')
		try:
			request = requests.post(url = self.url_, headers = self.headers_, json = self.params_)
			if request.status_code != 200:
				print("Request status: ", request.status_code, '\nMessage: ', request.text)
				sys.exit()
			time.sleep(20)
		except Exception as exc:
			print("Error in api_data:", exc)
			sys.exit()
		return request
	
	def get_request(self):
		try:
			print('Get request')
			request = requests.get(url = self.url_, headers = self.headers_, params = self.params_)
			if request.status_code != 200:
				print("Request status: ", request.status_code, '\nMessage: ', request.text)
				raise SystemExit(exc)
			time.sleep(5)
		except Exception as exc:
			print("Error in api_data:", exc)
			sys.exit()
		return request


def get_data(url, params):
	headers = {
	 'Authorization': key.wb_api_token
	}
	requests = Request(url, headers, params).post_request()
	return requests.json()