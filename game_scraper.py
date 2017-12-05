import dryscrape
from bs4 import BeautifulSoup
import os

game_id = 690213

session = dryscrape.Session()
session.visit("http://scrimmage.csail.mit.edu/watch_game?gameid=" + str(game_id))
response = session.body()
response_uni = u''.join(response).encode('utf-8')

os.system("mkdir -p " + os.getcwd()+"/game_data/"+str(game_id))
print "mkdir -p " + os.getcwd()+"/game_data/"+str(game_id)
text_file = open("game_data/"+str(game_id)+"/page.html", "w")
text_file.write(response_uni)
text_file.close()

