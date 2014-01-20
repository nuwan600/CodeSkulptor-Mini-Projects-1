# implementation of card game - Memory

import simplegui
import random

Card=[0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7]
Draw_Enable=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
turns=0
# helper function to initialize globals
def new_game():
    global state
    global Draw_Enable
    global turns
    random.shuffle(Card)
    state = 0 
    turns = 0
    label.set_text("Turns = "+str(turns))
    Draw_Enable=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state
    global Draw_Enable
    global next1
    global next2
    global turns
    i=pos[0]/50
    if state == 0:
        if(Draw_Enable[i]==0):
                next1=i
                Draw_Enable[i]=1
                state = 1
    elif state == 1:
         if(Draw_Enable[i]==0):
                next2=i
                Draw_Enable[i]=1
                state = 2
    else:
         if(Draw_Enable[i]==0):
                if(Card[next1]!=Card[next2]):
                    Draw_Enable[next1]=0;
                    Draw_Enable[next2]=0;
                turns=turns+1
                label.set_text("Turns = "+str(turns))
                next1=i
                Draw_Enable[i]=1
                state = 1
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
     x=0
     i=0
     while(i<16):
         if(Draw_Enable[i]==0):
             canvas.draw_polygon([[0+x,0], [0+x,100], [50+x,100], [50+x,0]], 3, 'Gold', 'Green')
         x=x+50
         i=i+1  
            
     x=12
     i=0
     for card in Card:
         if(Draw_Enable[i]==1):
             canvas.draw_text(str(card), [x,65], 50, "White")
         x=x+50
         i=i+1

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
