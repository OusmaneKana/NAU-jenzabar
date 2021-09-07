from bs4 import BeautifulSoup


with open('Calendar_dump.txt', 'r') as f:
	source = f.readlines()

soup = BeautifulSoup(source[0], 'html.parser')
classes = soup.find_all('tr')