import dryscrape
from bs4 import BeautifulSoup
import os
import time
import random

# currently update this manually
#highest_known_game_id = 754817
highest_known_game_id = 740775 # many of the games in the couple thousand above this range have no moves?

# read in list of games that currently have
d = './game_data/'
game_ids_have = [os.path.join(d, o) for o in os.listdir(d) 
                    if os.path.isdir(os.path.join(d,o))]

game_ids_have = [o.split("game_data/")[1] for o in game_ids_have]
game_ids_have = sorted(game_ids_have)

print game_ids_have

MAX_NUM_NEW_GAMES = 50000

next_game_id = str(highest_known_game_id)

retries = 0

for i in range(MAX_NUM_NEW_GAMES):
	if os.path.isdir("./game_data/"+next_game_id):
		print "already have " + next_game_id
		next_game_id = str(int(next_game_id) - 1)
		continue
	if retries > 2:
		retries = 0
		next_game_id = str(int(next_game_id) - 1)

	# scrape one more than the current highest game we have
	time.sleep(0.05 + random.random()*0.1)
	os.system("python " +os.getcwd()+"/game_scraper.py " + next_game_id)

	# try to parse move list
	os.system("python " +os.getcwd()+"/parse_move_list.py " + next_game_id)

	# if move list exists, go on to next game
	if os.path.isfile(os.getcwd()+"/game_data/"+next_game_id+"/move_list.txt"):
		next_game_id = str(int(next_game_id) - 1)

	retries += 1
	# otherwise, try this game again



	

