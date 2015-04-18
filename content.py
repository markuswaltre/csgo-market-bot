from urllib2 import Request, urlopen, URLError
from bs4 import BeautifulSoup
import json
import sys

def content(url):
	request = Request(url)

	try:
		response = urlopen(request)
		data = json.load(response)
	except URLError, e:
	    print 'Nope. Got an error code:', e
	    sys.exit()
	else:

		html = data['results_html']
		return BeautifulSoup(html)
