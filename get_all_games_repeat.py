import os
import time
import random

while(1):
  time.sleep(3 + random.random())
  os.system("python " +os.getcwd()+ "/get_all_games.py")