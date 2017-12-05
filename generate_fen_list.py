import os
from time import sleep
from subprocess import Popen, PIPE

# Kill any currently-running leiserchess binaries
os.system("killall leiserchess")

game_id = 690214
move_list_filename = "game_data/"+str(game_id)+"/move_list.txt"

fw = open("tmpout", "w")
fr = open("tmpout", "r")
p = Popen("../leiserchess", stdin = PIPE, stdout = fw, stderr = fw, bufsize = 1)

fen_list_filename = "game_data/"+str(game_id)+"/fen_list.txt"
book = open(fen_list_filename, "wa", 0)
done_file = "/done.txt"
os.system("rm -f " + os.getcwd()+done_file)

# read in move list
with open(move_list_filename) as f:
    content = f.readlines()
move_list = [x.strip() for x in content] 
print move_list

# make all the moves
for i in move_list:
    print i

    # p.stdin.write("go depth 3\n")
    # while(1):
    #     if os.path.isfile(os.getcwd()+done_file):
    #         os.system("rm " + os.getcwd()+done_file)
    #         break
    #     #print "not yet found"
    #     sleep(0.1)
    # #sleep(5)

    # out = fr.readlines()
    # print out
    # entry, move = out[-2], out[-1].split()[-1]
    # print (entry, move)
    # book.write(entry)

    p.stdin.write("move " + i + "\n")
    sleep(0.05)
    out = fr.readlines()
    #print "out", out
    
    p.stdin.write("printfen\n")
    sleep(0.05)
    fen = fr.readlines()[0]
    print "out", fen
    book.write(fen)
    
    


p.stdin.write("quit\n")
out = fr.read()
fw.close()
fr.close()
