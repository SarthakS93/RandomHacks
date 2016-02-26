import requests
from bs4 import BeautifulSoup
import re

def magic():
	url = 'http://www.example.com'
	r = requests.get(url)
	a = r.text
	b = re.sub('Example', 'Test', a)
	soup = BeautifulSoup(b)
	print(soup)
	
magic()
		
