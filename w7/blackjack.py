# Mini-project #6 - Blackjack
# Demo can be seen and played at
'''
http://www.codeskulptor.org/#user14_wKWCSAy2CS_54.py
'''

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")

# initialize some useful global variables
in_play = False
outcome = ""
score_dealer = 0
score_player = 0
deck = None
player_hand = None
dealer_hand = None

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)


class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        result = ""
        for elem in self.hand:
            result += str(elem) + " "
        return "Hand contains " + result

    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        val = 0
        ace = 0
        for e in self.hand:
            if e.get_rank() == 'A' and val + 11 <= 21:
                val += 11
                ace += 1
                continue
            val += VALUES[e.get_rank()]
            if val > 21 and ace > 0:
                ace -= 1
                val -= 10
        return val

    def draw(self, canvas, pos):
        for elem in self.hand:
            elem.draw(canvas, [pos[0] + 15*self.hand.index(elem), pos[1]])

    def draw_in_play(self, canvas, pos):
        for elem in self.hand:
            if self.hand.index(elem) == 0 and in_play:
                canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (135.5,348), CARD_BACK_SIZE)
            else:
                elem.draw(canvas, [pos[0] + 15*self.hand.index(elem), pos[1]])

# define deck class
class Deck:
    def __init__(self):
        self.deck = []
        self.dealt = []
        for elem in SUITS:
            for el in RANKS:
                self.deck.append(Card(elem, el))

    def shuffle(self):
        self.deck = self.dealt + self.deck
        random.shuffle(self.deck)

    def deal_card(self):
        c = self.deck.pop()
        self.dealt.append(c)
        return c

    def __str__(self):
        res = ""
        for e in self.deck:
            res += e.get_suit() + e.get_rank() + " "
        return "Deck contains " + res

#define event handlers for buttons

def deal():
    global outcome, in_play, deck, total, score_dealer
    global player_hand, dealer_hand, outcome
    if in_play:
        outcome = "You called deal during game. You lose. Press again to play."
        score_dealer += 1
        in_play = False
        return
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()
    deck.shuffle()
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    in_play = True
    outcome = ""

def hit():
    global in_play, player_hand, deck, outcome
    global score_dealer, score_player
    if in_play and player_hand.get_value() < 21:
        player_hand.add_card(deck.deal_card())
        if player_hand.get_value() > 21:
            in_play = False
            outcome = "You bust!Press <deal> to play again."
            score_dealer += 1

    # if the hand is in play, hit the player

    # if busted, assign a message to outcome, update in_play and score

def stand():
    global in_play, player_hand, deck, dealer_hand, outcome
    global score_dealer, score_player
    if in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
        if dealer_hand.get_value() > 21:
            score_player += 1
            outcome = "Dealer busts. Press <deal> to play again."
        elif dealer_hand.get_value() < player_hand.get_value():
            outcome = "You win. Press <deal> to play again."
            score_player += 1
        elif dealer_hand.get_value() >= player_hand.get_value():
            score_dealer += 1
            outcome = "You lose. Press <deal> to play again."
        in_play = False

# draw handler
def draw(canvas):
    canvas.draw_text("Black", (230, 50), 40, "Black")
    canvas.draw_text("Jack", (320, 60), 30, "White")
    if in_play:
        player_hand.draw(canvas, [100, 150])
        dealer_hand.draw_in_play(canvas, [100, 300])
        canvas.draw_text(outcome, (230, 500), 40, "Red")
        canvas.draw_text("You vs Dealer: " + str(score_player) + " / " + str(score_dealer), (50, 100), 25, "Black")
        canvas.draw_text("Your hand: " + str(player_hand.get_value()), (350, 170), 20, "White")
    else:
        if player_hand != None and dealer_hand != None:
            player_hand.draw(canvas, [100, 150])
            dealer_hand.draw(canvas, [100, 300])
            canvas.draw_text("You vs Dealer: " + str(score_player) + " / " + str(score_dealer), (50, 100), 25, "Black")
            canvas.draw_text("Players hand: " + str(player_hand.get_value()), (350, 170), 20, "White")
            canvas.draw_text("Dealers hand: " + str(dealer_hand.get_value()), (350, 320), 20, "White")
        canvas.draw_text(outcome, (100, 500), 20, "Black")

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")


#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
frame.start()

