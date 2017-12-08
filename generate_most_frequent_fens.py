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

fen_counts = dict()
fen_counts_indices = dict()

def increment_ctr(in_dict, key):
    if key not in in_dict:
        in_dict[key] = 1
    else:
        in_dict[key] += 1
        
def add_idx(in_dict, key, idx):
    if key not in in_dict:
        in_dict[key] = [idx]
    else:
        in_dict[key].append(idx)
    
for i in game_ids_have:
    fen_list_filename = os.getcwd()+"/game_data/"+i+"/fen_list.txt"
    
    # if fen list already exists, go on to next game
    if not os.path.isfile(fen_list_filename):
        #print "don't have fen_list for ", i
        continue
    
    with open(fen_list_filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content] 
    for i,v in enumerate(content):
        #print i, v
        increment_ctr(fen_counts, v)
        add_idx(fen_counts_indices, v, i)

most_frequent_filename = "most_frequent_fens.txt"
text_file = open(most_frequent_filename, "w")

fen_counts_x = []
fen_counts_y = []

i = 0
for key, value in sorted(fen_counts.iteritems(), key=lambda (k,v): (-v,k)):
    if (value > 1):
        fen_counts_x.append(i)
        fen_counts_y.append(value)
    i+=1
    if value > 1:
        print "%s: %s" % (key, value)
        text_file.write(str(key)+"\n")

text_file.close()

print len(fen_counts), "total number of different fens"
import matplotlib.pyplot as plt

plt.plot(fen_counts_x, fen_counts_y)
plt.axis([0,2000,0,110])
plt.title("Distribution of most frequent board states, N=11,588 games")
plt.ylabel("# occurences of board state")
plt.xlabel("unique board positions (sorted by most frequent)")
plt.show()