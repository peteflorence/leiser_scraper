import dryscrape
from bs4 import BeautifulSoup
import os
import time
import random

# read in list of games that currently have
d = './game_data/'
game_ids_have = [os.path.join(d, o) for o in os.listdir(d) 
                    if os.path.isdir(os.path.join(d,o))]

game_ids_have = [o.split("game_data/")[1] for o in game_ids_have]
game_ids_have = sorted(game_ids_have)

print game_ids_have

MAX_NUM_NEW_GAMES = 10

next_game_id = str(int(game_ids_have[-1]) + 1)

for i in range(MAX_NUM_NEW_GAMES):
	# scrape one more than the current highest game we have
	time.sleep(1 + random.random()*0.1)
	os.system("python " +os.getcwd()+"/game_scraper.py " + next_game_id)
	next_game_id = str(int(next_game_id) + 1)

