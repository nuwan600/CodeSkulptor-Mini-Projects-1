# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random;

# initialize global variables used in your code
number = 0
count = 0

# helper function to start and restart the game
def new_game():
    # remove this when you add your code  
    #global number
    number=range100()
    #global count
    count=7
    
    
    #pass


# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global number
    number =random.randint(0, 100)
    global count
    count =7
    print"New game. Range is from 0 to 100"
    print"Number of remaining guess is",count,"\n"
    # remove this when you add your code    
    #pass

def range1000():
    # button that changes range to range [0,1000) and restarts
    global number
    number =random.randint(0, 1000)
    global count
    count=10
    print"New game. Range is from 0 to 1000"
    print"Number of remaining guess is",count,"\n"
    # remove this when you add your code    
    #pass
    
def input_guess(guess):
    # main game logic goes here
    #global number
    #print number
    global count
    num = int(guess)
    
    if num==number: 
            print "Correct!\n"
            new_game()
            return
    if num>number:
            count=count-1
            if(count!=0):
                
                print"Guess was",num
                print"Number of remaining guess is",count
                print"lower!\n"
            else:
                print "you ran out of times, the number was ",number,"\n"
                new_game()
    if num<number:
            count=count-1
            if(count!=0):
                
                print"Guess was",num
                print"Number of remaining guess is",count
                print"Higher!\n"
            else:
                print "you ran out of times, the number was ",number,"\n"
                new_game()
    
    # remove this when you add your code
    #pass
    
# create frame
f = simplegui.create_frame("Guess the number",200,200)


# register event handlers for control elements
f.add_button("range is [0 to 100]",range100, 200)
f.add_button("range is [0 to 1000]",range1000, 200)
f.add_input("Enter",input_guess, 200)


# call new_game and start frame
new_game()


# always remember to check your completed program against the grading rubric
f.start()
