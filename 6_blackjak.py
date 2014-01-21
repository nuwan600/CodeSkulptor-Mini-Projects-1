# Mini-project #6 - Blackjack

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
score = 0
cover=True
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
        
# define hand class
class Hand:
    def __init__(self):
        self.card_list=[]
        #pass	# create Hand object

    def __str__(self):
        pass	# return a string representation of a hand

    def add_card(self, card):
        self.card_list.append(card)
        #pass	# add a card object to a hand

    def get_value(self):
        sum_value=0;
        ace_count=False
        for card in self.card_list:
            sum_value=sum_value+VALUES.get(card.get_rank());
            if(card.get_rank()=='A'):
                ace_count=True
                
        if(ace_count==True):
            if(sum_value+10<=21):
                sum_value=sum_value+10
               
        print sum_value
        
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        #pass	# compute the value of the hand, see Blackjack video
        return sum_value
    
    def draw(self, canvas, pos):
        x=0;
        for card in self.card_list:
            card.draw(canvas,[pos[0]+x, pos[1]])
            x=x+100
        #pass	# draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.card_list=[]
        for i in SUITS:
            for j in RANKS:
                card= Card(i,j)
                self.card_list.append(card)

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.card_list)

    def deal_card(self):
        return self.card_list.pop()
        #pass	# deal a card object from the deck
    
    def __str__(self):
        pass	# return a string representing the deck

    
Dealer=Hand()
Player=Hand()
deck=Deck()
message=""
#define event handlers for buttons
def deal():
    global outcome, in_play, Player, Dealer, deck, message, score,cover
    # your code goes here
    message=""
    Dealer=Hand()
    Player=Hand()
    deck.shuffle()
    card1=deck.deal_card()
    card2=deck.deal_card()
    
    Dealer.add_card(card2)
    Player.add_card(card1)
    
    card3=deck.deal_card()
    card4=deck.deal_card()

    Player.add_card(card3)
    Dealer.add_card(card4)
    
    in_play = True
    cover=True
def hit():
    global Player, message, in_play, score, cover
    if(in_play==True):
        card1=deck.deal_card()
        # if the hand is in play, hit the player
        Player.add_card(card1)
        i=Player.get_value()
        # if busted, assign a message to outcome, update in_play and score
        if(i>21):
            message="you went busted and lose!"
            score=score-1
            in_play=False
            cover=False
       
def stand():
    # replace with your code below
    global message, in_play,score,cover
    if(in_play==True):
        cover=False
        # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
        while(Dealer.get_value()<17):
            card1=deck.deal_card()
            # if the hand is in play, hit the player
            Dealer.add_card(card1)
            
        if(Dealer.get_value()>21):
            message="You win!"
            score=score+1
            in_play=False
        else:
            if(Dealer.get_value()>=Player.get_value()):
                message="You lose!"
                score=score-1
                in_play=False
            else:
                message="You win!"
                score=score+1
                in_play=False
        
    # assign a message to outcome, update in_play and score
    
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global message
    Dealer.draw(canvas, [90, 200])
    Player.draw(canvas, [90, 400])
    canvas.draw_text('Blackjack', (90, 90), 48, 'Aqua')
    canvas.draw_text('Dealer', (90, 150), 24, 'Black')
    canvas.draw_text('Player', (90, 350), 24, 'Black')
    canvas.draw_text('Score: '+ str(score),(390, 90),24, 'Black')
    
    if(cover==True):
        card_loc = (CARD_BACK_CENTER[0],CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE,(90 + CARD_BACK_SIZE[0]/2,200+CARD_BACK_SIZE[1]/2),CARD_BACK_SIZE)
    
    if(in_play==True):
        canvas.draw_text( "Hit or Not?", (290, 350), 24, 'Black')
    else:
        canvas.draw_text( "New Deal?", (290, 350), 24, 'Black')
        canvas.draw_text( message,( 300, 150), 24, 'Black')
    
    
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
