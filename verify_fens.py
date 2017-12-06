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
print len(game_ids_have)

def file_len(fname):
	i = -1
	with open(fname) as f:
		for i, l in enumerate(f):
			pass
	return i + 1

for i in game_ids_have:
	# if fen list already exists, go on to next game
	if not os.path.isfile(os.getcwd()+"/game_data/"+i+"/fen_list.txt"):
		print "don't have fen list for " + i
		quit()
	if not os.path.isfile(os.getcwd()+"/game_data/"+i+"/move_list.txt"):
		print "don't have move list for " + i
		quit()

	# find num line in move list
	num_fens = file_len(os.getcwd()+"/game_data/"+i+"/fen_list.txt")

	# find num lines in fen list
	num_moves = file_len(os.getcwd()+"/game_data/"+i+"/move_list.txt")

	if num_moves != (num_fens-1):
		print "not equal! moves, fens:", num_moves, num_fens
		print i

	#time.sleep(0.1)
	#os.system("python " +os.getcwd()+"/generate_fen_list.py " + i)
