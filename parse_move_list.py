import os
import sys

game_id = 690214

if len(sys.argv) > 1:
	game_id= sys.argv[1]
print game_id

filename = "game_data/"+str(game_id)+"/page.html"

with open(filename) as f:
	content = f.readlines()
content = [x.strip() for x in content] 

for i,v in enumerate(content):
	if '"fen-rep-hist"' in v:
		print v
		fen_rep_hist = v.split('"fen-rep">')[1]
		fen_rep_hist = fen_rep_hist.split("</div>")[0]
		print fen_rep_hist
		fen_rep_hist = list(fen_rep_hist)
		for j,w in enumerate(fen_rep_hist):
			print j,w
			if w=="#":
				fen_rep_hist[j] = " "
		fen_rep_hist = "".join(fen_rep_hist)
		fen_rep_hist = fen_rep_hist.split("startpos ")[1]
		fen_rep_hist = fen_rep_hist.split(" ")
		print fen_rep_hist


move_list_filename = "game_data/"+str(game_id)+"/move_list.txt"
text_file = open(move_list_filename, "w")
for i,v in enumerate(fen_rep_hist):
  text_file.write(str(v)+"\n")
text_file.close()
