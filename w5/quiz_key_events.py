#key up key down events
'''
Write a Python program that initializes a global variable to 5. 
The keydown event handler updates this global variable by doubling it, 
while the keyup event handler updates it by decrementing it by 3.

What is the value of the global variable after 12 separate key presses, 
i.e., pressing and releasing one key at a time, and repeating this 12 times in total?

To test your code, the global variable's value should be 35 after 4 key presses.

demo: http://www.codeskulptor.org/#user12_CvYcaTYhfkv3f3S.py
'''

# control the position of a ball using the arrow keys

import simplegui

# Initialize globals
b = 5
num_presses = 0



def keydown(key):
    global b, num_presses
    num_presses += 1
    b *= 2
    print str(num_presses) + "   " + str(b)
    
def keyup(key):
    global b
    b -= 3
    print str(b)
# create frame 
frame = simplegui.create_frame("Echo", 35, 35)

# register event handlers
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
frame.start()
