# template for "Stopwatch: The Game"

# Import modules
import simplegui

# define global variables
interval = 100
time=0
run=0
pause_times=0
hit_times=0
position = [60, 110]
position1 = [150, 30]
message = "0:00.0"
score="0/0"

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    mins=time/600
    sec=(time-mins*600)/10;
    ssec=(time-mins*600)%10;
    p0=str(mins)
    
    if(sec<10):
        p1="0"+str(sec)
    else:
        p1=str(sec)
    
    p2=str(ssec)
    
    return p0+":"+p1+"."+p2
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global run
    run=1

def pause():
    global run
    global time
    #global store
    global pause_times
    global hit_times
    global position1
  
    if(run==1):
        if((time%10)==0):
            pause_times=pause_times+1
            hit_times=hit_times+1
            if(pause_times>=10):
                if(hit_times>=10):
                    position1[0]=122
                else:
                    position1[0]=135
            
        else:
            pause_times=pause_times+1
            if(pause_times>=10):
                   position1[0]=135

    run=0
    
    
def restart():
    global time
    global run
    global pause_times
    global hit_times
    pause_times=0
    hit_times=0
    run=0
    time=0

# define event handler for timer with 0.1 sec interval
def run_time():
    global time
    global message
    global run
    global pause_times
    global hit_times
    global score
    message=format(time)
    score=str(hit_times)+"/"+str(pause_times)
    if(run==1):
        time=time+1
    else:
        time=time

# define draw handler
def draw(canvas):
    canvas.draw_text(message, position, 36, "White")
    canvas.draw_text(score, position1, 36, "Green")


# create frame
f = simplegui.create_frame("stop watch",200,200)
timer = simplegui.create_timer(interval, run_time)

# register event handlers
f.add_button("Start",start, 200)
f.add_button("Pause",pause, 200)
f.add_button("Restart",restart, 200)
f.set_draw_handler(draw)

# start frame
f.start()
timer.start()
# Please remember to review the grading rubric
