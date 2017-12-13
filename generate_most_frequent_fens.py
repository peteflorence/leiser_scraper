import os
import time
import random

# read in list of games that currently have
d = './game_data/'
game_ids_have = [os.path.join(d, o) for o in os.listdir(d) 
                    if os.path.isdir(os.path.join(d,o))]

game_ids_have = [o.split("game_data/")[1] for o in game_ids_have]
game_ids_have = sorted(game_ids_have)

# filter by only good players!

list_of_good_players = ['dbausher', 'mengjiao', 'peteflo', 'reference_tas', 'reference_plus', 'akkas', 'endrias', 'itinawi', 'obeya', 'jakobw', 'stefren', 'vxia','yangk', 'ajayjain', 'igliu', 'jkearl','shreyask', 'akshat','alisao','jinglin','phuvp', 'insinger','sunphil','umaroy']
print list_of_good_players
list_of_games_with_good_players = []

def game_contains_player(game_id, list_of_good_players):
    with open(os.getcwd()+"/game_data/"+game_id+"/page.html") as f:
        content = f.readlines()
    content = [x.strip() for x in content] 
    for i,v in enumerate(content):
        if "vs" in v:
            for player in list_of_good_players:
                if player in v:
                    print v
                    return True
    return False

for game in game_ids_have:
    if game_contains_player(game, list_of_good_players):
        list_of_games_with_good_players.append(game)

print list_of_games_with_good_players

quit()
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
cum_fen_counts_y = []

unique_two_or_more = 0
num_two_or_more = 0
num_total = 0
i = 0
for key, value in sorted(fen_counts.iteritems(), key=lambda (k,v): (-v,k)):
    i+=1
    num_total += value
    if (value > 1):
        unique_two_or_more += 1
        num_two_or_more += value
        fen_counts_x.append(i)
        fen_counts_y.append(value)
        cum_fen_counts_y.append(num_total)
    if value > 1:
        print "%s: %s" % (key, value)
        text_file.write(str(key)+","+str(value)+"\n")

for i,v in enumerate(cum_fen_counts_y):
    cum_fen_counts_y[i] = v*1.0 / num_total

text_file.close()

print len(fen_counts), "total number of different fens"
print unique_two_or_more, "of these have been seen twice or more times"
print "that is", unique_two_or_more*1.0/len(fen_counts), "percent"
print "---"
print num_total, "is the total number of instances of fens"
print num_two_or_more, "is the number of instances for two or more"
print "that is", num_two_or_more*1.0/num_total, "percent"
print  ""
import matplotlib.pyplot as plt

plt.plot(fen_counts_x, fen_counts_y)
plt.axis([0,2000,0,110])
plt.title("Distribution of most frequent board states, N="+str(len(game_ids_have))+" games")
plt.ylabel("# occurences of board state")
plt.xlabel("unique board positions (sorted by most frequent)")
plt.show()

plt.plot(fen_counts_x, cum_fen_counts_y)
plt.title("Cdf of most frequent board states, N="+str(len(game_ids_have))+" games")
plt.ylabel("fraction of all board state instances")
plt.xlabel("unique board positions (sorted by most frequent)")
plt.show()