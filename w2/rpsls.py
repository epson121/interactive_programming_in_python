# Rock-paper-scissors-lizard-Spock template
#Made by Codeskulptor (codeskulptor.org)

# LINK TO THE PROGRAM
#   http://www.codeskulptor.org/#user10_yUTZuvXdQ2_3.py


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return -1

    
def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return -1


def rpsls(name): 
    player_number = name_to_number(name)
    print "Player chooses", name
    comp_number = random.randrange(0,5)
    print "Computer chooses", number_to_name(comp_number)
    difference = (player_number - comp_number) % 5
    if difference == 3 or difference == 4:
        print "Computer wins.\n"
        return
    elif difference == 1 or difference == 2:
        print "Player wins.\n"
        return
    elif difference == 0:
        print "Draw.\n"
        return
    else:
        print "Error.\n"
        
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# run example
'''
Player chooses rock
Computer chooses lizard
Player wins.

Player chooses Spock
Computer chooses paper
Computer wins.

Player chooses paper
Computer chooses scissors
Computer wins.

Player chooses lizard
Computer chooses Spock
Player wins.

Player chooses scissors
Computer chooses rock
Computer wins.
'''

