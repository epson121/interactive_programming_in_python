'''
Implementation of the memory game.
Demo can be seen at:
	http://www.codeskulptor.org/#user14_WxOqkmqEHb_16.py
'''

import simplegui
import random

memory_deck = range(0, 8) + range(0, 8)
exposed = [False] * 16
random.shuffle(memory_deck)
state = 0
selected = {}
click_counter = 0

def init():
    global memory_deck, exposed, state, selected, click_counter
    memory_deck = range(0, 8) + range(0, 8)
    exposed = [False] * 16
    random.shuffle(memory_deck)
    state = 0
    selected = {}
    click_counter = 0
    label.set_text("Moves: " + str(0))

# define event handlers
def mouseclick(pos):
    global exposed, state, memory_deck, selected, click_counter
    p = pos[0] / 50
    if state == 0:
        if exposed[int(p)] == False:
            exposed[int(p)] = True
            selected[int(p)] = memory_deck[int(p)]
            state = 1
            click_counter += 1
    elif state == 1:
        if exposed[int(p)] == False:
            exposed[int(p)] = True
            selected[int(p)] = memory_deck[int(p)]
            state = 2
            click_counter += 1
    else:
        if exposed[int(p)] == False:
            if selected.values()[0] != selected.values()[1]:
                exposed[selected.keys()[0]] = False
                exposed[selected.keys()[1]] = False
            selected = {}
            exposed[int(p)] = True
            selected[int(p)] = memory_deck[int(p)]
            state = 1
            click_counter += 1
    label.set_text("Moves: " + str(click_counter))
# cards are logically 50x100 pixels in size
def draw(canvas):
    global memory_deck
    i = 0
    for elem in memory_deck:
        if exposed[i] == True:
            canvas.draw_text(str(elem), (i*50 + 12.5, 70), 50, "White")
        else:
            canvas.draw_text("X", (i*50 + 12.5, 70), 50, "Green")
        i += 1

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()