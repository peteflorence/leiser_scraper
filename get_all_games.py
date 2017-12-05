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


def is_a_game(game_id):
	session = dryscrape.Session()
	session.visit("http://scrimmage.csail.mit.edu/watch_game?gameid=" + str(game_id))
	response = session.body()
	response_uni = u''.join(response).encode('utf-8') 
	content = response_uni.splitlines()
	for i,v in enumerate(content):
		if "<title>500 Internal Server Error</title>" in v:
			print "NOT A GAME"
			return False
			quit()
	print "yes a game"
	return True

# low, high are both already in all_games
# but nothing in between currently is
def find_games_between(low, high):
	for i in range(low+1,high):
		if is_a_game(i):
			all_games.append(i)
			return                   ## REMOVE

print len(all_games), " is length before filling holes"

# search for if there are any missing holes
prev_v = all_games[0]
for i,v in enumerate(all_games):
	if i == 0:
		continue
	if (v != prev_v + 1):
		print "HOLE BETWEEN", prev_v, v
		find_games_between(prev_v, v)
		break						## REMOVE
	prev_v = v

print len(all_games), " is length after filling holes"

all_games = sorted(all_games)

text_file = open("all_games.txt", "w")
for i in all_games:
  text_file.write(str(i)+"\n")
text_file.close()

