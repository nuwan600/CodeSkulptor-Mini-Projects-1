# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0.5
acc=[0,0]

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2013.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.info=info
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = self.info.get_center()
        self.image_size = self.info.get_size()
        self.radius = self.info.get_radius()
        self.fire=False
  
    def set_thrust(self, a):
        self.thrust=a
        if(a==True):
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.rewind()
        
    def shoot(self):
        global a_missile
        missile_vel=[0,0]
        vec=angle_to_vector(my_ship.angle)
        missile_vel[0]=2.5*vec[0]+self.vel[0]
        missile_vel[1]=2.5*vec[1]+self.vel[1]
        a_missile = Sprite([self.pos[0], self.pos[1]], missile_vel, self.angle, 0, missile_image, missile_info, missile_sound)
        self.fire=True
        
    
    def draw(self,canvas):
        if(self.thrust==True):
            self.info = ImageInfo([135, 45], [90, 90], 35)
            self.image_center = self.info.get_center()
            self.image_size = self.info.get_size()
            self.radius = self.info.get_radius()
            
        else:
            self.info = ImageInfo([45, 45], [90, 90], 35)
            self.image_center = self.info.get_center()
            self.image_size = self.info.get_size()
            self.radius = self.info.get_radius()
            
        canvas.draw_image(self.image,self.image_center,self.image_size,self.pos,self.image_size,self.angle)
        if(self.fire==True):
            a_missile.draw(canvas)
        
        
        
        
    
    def update(self):
        global acc
        acc=angle_to_vector(my_ship.angle)
        self.angle+=self.angle_vel
        self.pos[0]=self.pos[0]+self.vel[0]
        self.vel[0]=0.97*self.vel[0]
        self.pos[1]=self.pos[1]+self.vel[1]
        self.vel[1]=0.97*self.vel[1]
        #print acc
        self.pos[0]=self.pos[0]%800
        self.pos[1]=self.pos[1]%600
        if self.thrust==True:
            self.vel[0]+=0.5*acc[0]
            self.vel[1]+=0.5*acc[1]
        if self.thrust==False:
            acc[0]=0
            acc[1]=0
        if(self.fire==True):
            a_missile.update()
        
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        canvas.draw_image(self.image,self.image_center,self.image_size,self.pos,self.image_size,self.angle)
    
    def update(self):
        self.pos[0]=self.pos[0]+self.vel[0]
        self.pos[1]=self.pos[1]+self.vel[1]
        self.pos[0]=self.pos[0]%800
        self.pos[1]=self.pos[1]%600
        self.angle=self.angle+0.1*self.angle_vel/100

           
def draw(canvas):
    global time,score,lives
   
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_text('lives:'+ str(lives), [15, 20], 20, 'White')
    canvas.draw_text('score:'+ str(score), [680, 20], 20, 'White')
    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    #a_missile.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    a_rock.update()

    
            
# timer handler that spawns a rock    
def rock_spawner():
    global a_rock
    random.seed()
    x=random.randint(0, 800)
    y=random.randint(0, 600)
    x_v=random.randint(0, 2)
    y_v=random.randint(0, 2)
    angle=random.randint(0,360)
    temp=random.randint(0,100)
    a_v=temp
    a_rock = Sprite([x, y], [x_v, y_v], angle, a_v, asteroid_image, asteroid_info)
    
    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites

my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0, asteroid_image, asteroid_info)
a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info)

#key_handler_down
def key_handler_down(key):
    global my_ship, acc
    if key==simplegui.KEY_MAP["space"]:
        my_ship.shoot()
    if key==simplegui.KEY_MAP["up"]:
        my_ship.set_thrust(True)
    if key==simplegui.KEY_MAP["right"]:
        my_ship.angle_vel=0.1
    if key==simplegui.KEY_MAP["left"]:
        my_ship.angle_vel=-0.1

#key_handler_up
def key_handler_up(key):
    global my_ship
    if key==simplegui.KEY_MAP["space"]:
        pass        
    if key==simplegui.KEY_MAP["up"]:
        my_ship.set_thrust(False)
    if key==simplegui.KEY_MAP["right"]:
        my_ship.angle_vel=0   
    if key==simplegui.KEY_MAP["left"]:
        my_ship.angle_vel=0;
        
# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_handler_down)
frame.set_keyup_handler(key_handler_up)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()