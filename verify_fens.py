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
		#print "don't have fen list for " + i
		continue
	if not os.path.isfile(os.getcwd()+"/game_data/"+i+"/move_list.txt"):
		#print "don't have move list for " + i
		continue

	# find num line in move list
	fen_file = os.getcwd()+"/game_data/"+i+"/fen_list.txt"
	num_fens = file_len(fen_file)

	# find num lines in fen list
	move_file = os.getcwd()+"/game_data/"+i+"/move_list.txt"
	num_moves = file_len(move_file)

	if num_moves != (num_fens-1):
		print "not equal! moves, fens:", num_moves, num_fens
		print i
		os.system("rm " + fen_file)

	#time.sleep(0.1)
	#os.system("python " +os.getcwd()+"/generate_fen_list.py " + i)
