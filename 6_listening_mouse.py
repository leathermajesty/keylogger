from pynput.mouse import Listener

def printcordinate(x,y):
    #print("Position of current mouse {0}".format((x,y)))
    with open("movement.txt",'a') as f:
        
        f.write(str((x,y))+"\n")

with Listener(on_move=printcordinate) as l:
    l.join()


