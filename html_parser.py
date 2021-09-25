from bs4 import BeautifulSoup
from icecream import ic

with open('Calendar_dump.txt', 'r') as f:
	source = f.read()

soup = BeautifulSoup(source, 'html.parser')

event_dct = {}
days = ['Mon', 'Tue','Wed', 'Thu','Fri', 'Sat','Sun']

divs = soup.find_all('div')


for d in divs:
	day = d.find("span", {"class": "date"}).text.strip()
	infos = d.find("span", {"class": "info"}).text.strip().split('\n')[0]
	times = d.find("span", {"class": "hours"}).text.strip().split('\n')[0]

	if day:
		current = day
		event_dct[day] = [{'Activity':infos,
						  'Time':times}]
	else:
		event_dct[current].append({'Activity':infos,
						  'Time':times})

for i in event_dct.keys():
	print(i,event_dct[i])
	# if d.text.split(",")[0] in days:
	# 	print(d.text)




# count = 0
# for day in days_of_week:
# 	if count %7 ==0: 
# 		print("\n")
# 	print(day)
# 	count+=1




# for c in classes:
# 	print(c.text)c