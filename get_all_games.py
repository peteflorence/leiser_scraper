import dryscrape
from bs4 import BeautifulSoup
import os

# read in all games
with open("all_games.txt") as f:
	all_games = f.readlines()
all_games = [int(x.strip()) for x in all_games] 
all_games = sorted(all_games)


# scrape currently listed games
session = dryscrape.Session()
session.visit("http://scrimmage.csail.mit.edu/")
response = session.body()
response_uni = u''.join(response).encode('utf-8') 
content = response_uni.splitlines()


for i,v in enumerate(content):
	if 'gameid' in v:
		split_after = v.split("gameid=")[1]
		i_game = split_after.split("&")
		if len(i_game) > 1:
			new_game_id = int(i_game[0])
			if new_game_id not in all_games:
				print "found a new game!!"
				print new_game_id
				all_games.append(new_game_id)

all_games = sorted(all_games)

# search for if there are any missing holes
prev_v = all_games[0]
for i,v in enumerate(all_games):
	if i == 0:
		continue
	if (v != prev_v + 1):
		print "HOLE BETWEEN", v, prev_v
	prev_v = v


text_file = open("all_games.txt", "w")
for i in all_games:
  text_file.write(str(i)+"\n")
text_file.close()

