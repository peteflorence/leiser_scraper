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

for i in game_ids_have:
	# if fen list already exists, go on to next game
	if os.path.isfile(os.getcwd()+"/game_data/"+i+"/fen_list.txt"):
		continue

	os.system("python " +os.getcwd()+"/generate_fen_list.py " + i)




	

