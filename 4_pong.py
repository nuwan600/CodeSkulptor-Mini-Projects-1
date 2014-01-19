# Implementation of classic arcade game Pong

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
LEFT = False
RIGHT = True

#set global var
bottom1=(200+HALF_PAD_HEIGHT)
top1=(200-HALF_PAD_HEIGHT)
bottom2=(200+HALF_PAD_HEIGHT)
top2=(200-HALF_PAD_HEIGHT)

current_key = ' '

paddle1_vel=0
paddle2_vel=0

paddle1_pos=[(0,(200+HALF_PAD_HEIGHT)),(0,(200-HALF_PAD_HEIGHT))]
paddle2_pos=[((WIDTH-1),(200+HALF_PAD_HEIGHT)),((WIDTH-1),(200-HALF_PAD_HEIGHT))]

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel=[0, 0]

score_pos1 = [150, 30]
score1=0
score_pos2 = [450, 30]
score2=0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
   
    if(direction=="RIGHT"):
         ball_vel=[random.randrange(2, 4), (-1)*random.randrange(1, 3)]
    elif(direction=="LEFT"):
        ball_vel=[(-1)*random.randrange(2, 4), (-1)*random.randrange(1, 3)]
   

# define event handlers
def restart():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    global top1,top2,bottom1,bottom2
    bottom1=(200+HALF_PAD_HEIGHT)
    top1=(200-HALF_PAD_HEIGHT)
    bottom2=(200+HALF_PAD_HEIGHT)
    top2=(200-HALF_PAD_HEIGHT)
    paddle1_vel=0 
    paddle2_vel=0
    score1=0
    score2=0
    new_game()
    
    
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    a=random.randint(0, 1)
    #decide which direction
    if(a==1):
        spawn_ball("LEFT")
    else:
        spawn_ball("RIGHT")
        
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
    global top1,top2,bottom1,bottom2
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    #collision detect
    if ball_pos[0] <= BALL_RADIUS+PAD_WIDTH:
        if(ball_pos[1]>top1 and ball_pos[1]<bottom1):
            ball_vel[0] = - ball_vel[0]*1.1
        else:
            score2+=1
            spawn_ball("RIGHT")
     
    if ball_pos[0] > WIDTH-BALL_RADIUS-PAD_WIDTH:
        if(ball_pos[1]>top2 and ball_pos[1]<bottom2):
            ball_vel[0] = - ball_vel[0]*1.1
        else:
            score1+=1
            spawn_ball("LEFT")
            
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    if ball_pos[1] > HEIGHT-BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    
    # update paddle's vertical position, keep paddle on the screen
    bottom1=bottom1+paddle1_vel
    top1=top1+paddle1_vel
    bottom2=bottom2+paddle2_vel
    top2=top2+paddle2_vel
    
    if(top1<0):
        top1=0
        bottom1=PAD_HEIGHT
       
    if(top2<0):
        top2=0
        bottom2=PAD_HEIGHT
        
        
    if(bottom1>HEIGHT-1):
        top1=HEIGHT-1-PAD_HEIGHT
        bottom1=HEIGHT-1
       
    if(bottom2>HEIGHT-1):
        top2=HEIGHT-1-PAD_HEIGHT
        bottom2=HEIGHT-1
    
    paddle1_pos=[(0, top1),(0,bottom1)]
    paddle2_pos=[((WIDTH-1),top2),((WIDTH-1),bottom2)]
    
    # draw paddles
    c.draw_polygon(paddle1_pos,PAD_WIDTH, 'White', 'White')
    c.draw_polygon(paddle2_pos,PAD_WIDTH, 'White', 'White')
    
    # draw scores
    c.draw_text(str(score1), score_pos1, 36, "White")
    c.draw_text(str(score2), score_pos2, 36, "White")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    global current_key
    global top1,top2,bottom1,bottom2
    current_key = chr(key)
    if current_key in 'W':
        if(top1>0):
            paddle1_vel=-5
       
    if current_key in 'S':
        if(bottom1<HEIGHT-1):
            paddle1_vel=5
    
    if key==simplegui.KEY_MAP["up"]:
         if(top2>0):
            paddle2_vel=-5
         
    if key==simplegui.KEY_MAP["down"]: 
        if(bottom2<HEIGHT-1):
            paddle2_vel=5
         

            
def keyup(key):
    global paddle1_vel, paddle2_vel
    global current_key
    current_key = ''
    paddle1_vel=0
    paddle2_vel=0
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart",restart, 200)

# start frame
new_game()
frame.start()
