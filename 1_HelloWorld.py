# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper function

import random;

def number_to_name(number):
    # fill in your code below
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if(number==0): return "rock"
    if(number==1): return "Spock"
    if(number==2): return "paper"
    if(number==3): return "lizard"
    if(number==4): return "scissors"
    
def name_to_number(name):
    # fill in your code below

    # convert name to number using if/elif/else
    # don't forget to return the result!
    if(name=="rock"): return 0
    if(name=="Spock"): return 1
    if(name=="paper"): return 2
    if(name=="lizard"): return 3
    if(name=="scissors"): return 4
    
def rpsls(name): 
    # fill in your code below
     
    # convert name to player_number using name_to_number
    
    player_number=name_to_number(name)
        
    # compute random guess for comp_number using random.randrange()
    computer_number=random.randint(0, 4)
    
    # compute difference of player_number and comp_number modulo five
    different=(player_number-computer_number)%5
    
    # use if/elif/else to determine winner
    if  different==1 or different==2:
        player_win=True
        computer_win=False
        draw=False
        
    if  different==3 or different==4: 
        player_win=False
        computer_win=True
        draw=False
    
    if  different==0: 
        player_win=False
        computer_win=False
        draw=True
    
    # convert comp_number to name using number_to_name
    computer_name=number_to_name(computer_number)
    
    # print results   () for python3!!
    print ("Player choose " + name)
    print ("Computer choose " + computer_name)
    if(player_win): print ("Player wins")
    if(computer_win): print ("Computer wins")
    if(draw): print ("Draw!")
        
        
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

