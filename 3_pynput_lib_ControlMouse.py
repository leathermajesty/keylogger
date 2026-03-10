# Controlling your mouse
# listening to your mouse
# Controlling your keyboard
# listening to your keyboard

from pynput.mouse import Controller

def ControlMouse():
    mouse = Controller()
    mouse.position = (600,300)

ControlMouse()

