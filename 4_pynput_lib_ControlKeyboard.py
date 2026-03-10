# Controlling your keyboard
# listening to your keyboard

# from pynput.keyboard import Controller

# def ControlKeyboard():
#     keyboard = Controller()
#     keyboard.type("This is text")
    
# ControlKeyboard()

import time
from pynput.keyboard import Controller

def ControlKeyboard():
    keyboard = Controller()
    
    # Wait 3 seconds before starting
    time.sleep(3) 
    
    keyboard.type("Hi")

ControlKeyboard()

