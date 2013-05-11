#Stopwatch - the game.
'''
Mini-project description - "Stopwatch: The Game"
author: Luka Rajcevic
demo can be seen at: 
http://www.codeskulptor.org/#user12_qTz9x4LC5P_1.py
'''

# template for "Stopwatch: The Game"
import simplegui

# define global variables
number = 0
num1 = 0
num2 = 0
milis = 0
changed = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(num):
    global milis
    if num == 0:
        return "0:00.0"
    minutes = int(num/600)
    num = num - (minutes * 600)
    seconds = int(num/10)
    num = num - (seconds * 10)
    milis = num
    if (seconds < 10):
        seconds = "0"+str(seconds)
    else:
        seconds = str(seconds)
    return str(minutes)+":"+ seconds +"."+str(milis)


# define event handlers for buttons; "Start", "Stop", "Reset"
def timer_start():
    global changed
    changed = False
    timer.start()
    
def timer_stop():
    global number, changed, num2, num1
    if number % 10 == 0 and changed == False:
        num1 += 1
        changed = True
    num2 += 1
    timer.stop()
    
def timer_reset():
    global number
    number = 0
    timer.stop()
    
# define event handler for timer with 0.1 sec interval
def tick():
    global number
    number += 1
    

# define draw handler
def draw_time(canvas):
    canvas.draw_text(format(number), (80, 120), 80, "Red")
    canvas.draw_text(str(num1), (200, 40), 40, "Green")
    canvas.draw_text(" / ", (220, 40), 40, "Green")
    canvas.draw_text(str(num2), (250, 40), 40, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 150)

# register event handlers
frame.set_draw_handler(draw_time)
timer = simplegui.create_timer(100, tick)
button1 = frame.add_button("Start", timer_start)
button2 = frame.add_button("Stop", timer_stop)
button3 = frame.add_button("Reset", timer_reset)

# start frame
frame.start()

# Please remember to review the grading rubric
