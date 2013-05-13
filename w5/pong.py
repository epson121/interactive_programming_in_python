# Implementation of classic arcade game Pong
# DEMO AT http://www.codeskulptor.org/#user13_m18WJ61w9LTWw7M_0.py
# still missing: restart button, and update on collision detection

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [300, 200]
ball_vel = [0, 0]
ball_initiated = False
point_right = False
point_left = False
points_right = 0
points_left = 0

paddle2_pos = [PAD_WIDTH/2, HEIGHT/2 -1]
paddle1_pos = [WIDTH - 1 - PAD_WIDTH/2, HEIGHT/2 - 1]
paddle1_vel = [0, 0]
paddle2_vel = [0, 0]
# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel, ball_initiated # these are vectors stored as lists
    if right == True:
        ball_pos = [WIDTH/2, HEIGHT/2]
        ball_vel = [3, 3]
    else:
        ball_pos = [WIDTH/2, HEIGHT/2]
        ball_vel = [-3, 3]
    ball_initiated = True    
    
def update_ball():
    global ball_pos, ball_vel
    check_for_collisions()
    ball_pos = [ball_pos[0] + ball_vel[0], ball_pos[1] - ball_vel[1]]

def check_for_collisions():
    global BALL_RADIUS, ball_pos, ball_vel, paddle1_pos, paddle2_pos, point_right, point_left
    if ball_pos[0] - BALL_RADIUS <= PAD_WIDTH and ball_pos[1] > paddle1_pos[1] - HALF_PAD_HEIGHT and ball_pos[1] < paddle1_pos[1] + HALF_PAD_HEIGHT:
        ball_vel[0] *= -1.1
    if ball_pos[0] + BALL_RADIUS >= WIDTH - 1 -PAD_WIDTH and ball_pos[1] > paddle2_pos[1] - HALF_PAD_HEIGHT and ball_pos[1] < paddle2_pos[1] + HALF_PAD_HEIGHT:
        ball_vel[0] *= -1.1
    if ball_pos[1] + BALL_RADIUS >= HEIGHT -1:
        ball_vel[1] *= -1
    if ball_pos[1] - BALL_RADIUS <= 0:
        ball_vel[1] *= -1 
    if ball_pos[0] < 0:
        point_right = True
    if ball_pos[0] > WIDTH:
        point_left = True

def update_paddle1():
    paddle1_pos[1] += paddle1_vel[1]
    if paddle1_pos[1] - HALF_PAD_HEIGHT <= 0:
        paddle1_pos[1] = HALF_PAD_HEIGHT
    if paddle1_pos[1] + HALF_PAD_HEIGHT >= HEIGHT - 1:
        paddle1_pos[1] = HEIGHT - 1 - HALF_PAD_HEIGHT
        
def update_paddle2():
    paddle2_pos[1] += paddle2_vel[1]
    if paddle2_pos[1] - HALF_PAD_HEIGHT <= 0:
        paddle2_pos[1] = HALF_PAD_HEIGHT
    if paddle2_pos[1] + HALF_PAD_HEIGHT >= HEIGHT - 1:
        paddle2_pos[1] = HEIGHT - 1 - HALF_PAD_HEIGHT

# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global ball_initiated, point_left, point_right, points_left, points_right
    # update paddle's vertical position, keep paddle on the screen
    update_paddle1()
    update_paddle2()    
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_polygon([(0, paddle1_pos[1] + HALF_PAD_HEIGHT), (0,paddle1_pos[1] - HALF_PAD_HEIGHT), (PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT), (PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT)], 1, "Green", "White")
    c.draw_polygon([(WIDTH-1, paddle2_pos[1] + HALF_PAD_HEIGHT), (WIDTH-1,paddle2_pos[1] - HALF_PAD_HEIGHT), (WIDTH - 1 - PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT), (WIDTH - 1 - PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT)], 1, "Green", "White")
    # draw paddles
     
    # update ball
    if ball_initiated == False:
        ball_init(random.choice([True, False]))
    update_ball()
    # draw ball and scores
    if point_left == True:
        point_left = False
        points_left += 1
        ball_initiated = False
    if point_right == True:
        point_right = False
        points_right += 1
        ball_initiated = False  
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Green", "White")
    c.draw_text(str(points_left), (WIDTH/3, HEIGHT/3), 40, "Red")
    c.draw_text(str(points_right), (2*WIDTH/3, HEIGHT/3), 40, "Red")
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos
    if key == simplegui.KEY_MAP['down']:
        paddle1_vel[1] = 5
    elif key == simplegui.KEY_MAP['up']:
        paddle1_vel[1] = -5
    if key==simplegui.KEY_MAP['w']:
        paddle2_vel[1] = -5
    elif key==simplegui.KEY_MAP['s']:
        paddle2_vel[1] = 5
    
        
def keyup(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos
    if key == simplegui.KEY_MAP['down']:
        paddle1_vel[1] = 0
    elif key == simplegui.KEY_MAP['up']:
        paddle1_vel[1] = 0
    if key==simplegui.KEY_MAP["w"]:
        paddle2_vel[1] = 0
    elif key==simplegui.KEY_MAP["s"]:
        paddle2_vel[1] = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
frame.start()
