# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui

# initialize global variables used in your code
number = -1
count = 0
max_count = 0

# define event handlers for control panel
    
def range100():
    print "You have chosen 0 - 100 game mode.\nTake your guess.."
    f.start()
    global number, max_count, count
    number = random.randrange(0, 100)
    count = 0
    max_count = 7

def range1000():
    print "You have chosen 0 - 1000 game mode.\nTake your guess.."
    f.start()
    global number, max_count, count
    number = random.randrange(0, 1000)
    count = 0
    max_count = 10

    
def get_input(guess):
    global count
    if number == -1:
        print "Please choose a game mode...(1-100 or 1-1000)"
        f.start()
        return
    count += 1
    print "You guessed: ", guess
    print "Number of guesses so far: ", count, "/", max_count
    if int(guess) > number:
        print "Lower."
    elif int(guess) < number:
        print "Higher."
    else:
        print "Correct."
        print "Starting new game..."
        count = 0
        f.start()
        return
    if count >= max_count:
        print "Maximum number of guesses used. Restarting..."
        count = 0
        f.start()
        return

    
# create frame
f = simplegui.create_frame("Home", 100, 200)

# register event handlers for control elements
f.add_button("0 - 100", range100, 100)
f.add_button("0 - 1000", range1000, 100)
f.add_input("Guess", get_input, 100)

# start frame
f.start()

# always remember to check your completed program against the grading rubric
