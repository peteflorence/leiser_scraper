import dryscrape
from bs4 import BeautifulSoup
import os

session = dryscrape.Session()
session.visit("http://scrimmage.csail.mit.edu/")
response = session.body()
response_uni = u''.join(response).encode('utf-8') 
content = response_uni.splitlines()

all_games = []

for i,v in enumerate(content):
	if 'gameid' in v:
		split_after = v.split("gameid=")[1]
		i_game = split_after.split("&")
		if len(i_game) > 1:
			print i_game[0]
			all_games.append(i_game[0])


text_file = open("all_games.txt", "w")
for i in all_games:
	text_file.write(i + "\n")
text_file.close()

