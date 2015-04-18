from content import content
from sendemail import sendemail
from notification import notification
import time
import webbrowser

url = "http://steamcommunity.com/market/search/render/?query=&start=0&count=10&search_descriptions=0&sort_column=price&sort_dir=asc&appid=730&category_730_ItemSet%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_Knife"
linktag = "market_table_value"
nametag = "market_listing_item_name"
THRESHOLD = 30
CURRENCY = ''

html = content(url)

sent = []

def parse(html):
	arr = []
	for link in html.find_all('a'):
		href = link.get('href')
		value = link.find(attrs={'class': linktag})
		price = value.span.text
		image = link.find('img').get('src')
		name = link.find(attrs={'class', nametag}).text

		amount, currency = price[1:-4], price[:1]

		CURRENCY = currency

		arr.append({
			'amount': float(amount), 
			'href': href,
			'image': image,
			'name': name
		})

	return arr

def prettyMessage(item):
	s = ''

	# for item in items:
	s += str(item['amount']) + ' ' + CURRENCY + '<br>'
	s += '<img src="' + item['image'] + '"><br>'
	s += '<a href="' + item['href'] + '">' + item['name'] + '</a>'
	s += '<br>'

	return s.encode('utf-8')


def run():
	for i in range(1000000):
		cheapSeen = False
		html = content(url)
		items = parse(html)
		item = items[0]

		if item['amount'] < THRESHOLD:
			print item['amount']
			print item['href']
			cheapSeen = True

			subject = 'Cheapest knife: %s' % item['name']
						
			if item['amount'] not in sent:
				webbrowser.open(item['href'], new=1)
				sendemail(subject.encode('utf-8'), prettyMessage(item))
				sent.append(item['amount'])

		if not cheapSeen:
			if len(items) > 0:
				print '#', i, ': Cheapest is ', items[0]['amount']


		time.sleep(1)

run()