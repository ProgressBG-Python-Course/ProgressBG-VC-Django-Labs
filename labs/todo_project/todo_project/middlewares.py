import requests
from datetime import datetime
from django.conf import settings


class SOMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response
		# One-time configuration and initialization.

	def __call__(self, request):
		# Code to be executed for each request before
		# the view (and later middleware) are called.
		# current date and time

		# TODO: make example for this with function midleware
		# now = datetime.now()
		# timestamp = now.strftime('%H:%M:%S')
		# print(f'->>>>>>>>> {timestamp} <<<<<<<<<<<<<<,-')



		response = self.get_response(request)

		# Code to be executed for each request/response after
		# the view is called.

		return response

	def process_exception(self, request, exception):
		print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
		if settings.DEBUG:

			intitle = '{}'.format(exception.__class__.__name__)

			# now query the SO APIs:
			url = 'https://api.stackexchange.com/2.2/search'
			headers = { 'User-Agent': 'github.com/vitorfs/seot' }
			params = {
				'order': 'desc',
				'sort': 'votes',
				'site': 'stackoverflow',
				'pagesize': 3,
				'tagged': 'python;django',
				'intitle': intitle
			}

			# send request to SE API:
			r = requests.get(url, params=params, headers=headers)
			
			# process SE API response
			questions = r.json()

			# print first 3 SO answers in console:
			print('\n','#'*50)
			for question in questions['items']:
			  	print('{}:{}'.format(question['title'], question['link'] ))
			print('#'*50)

		return None