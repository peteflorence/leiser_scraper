import os

game_id = 690213

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
		print fen_rep_hist