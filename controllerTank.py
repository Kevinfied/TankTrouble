from pygame import *
from math import *
screen = display.set_mode((800,600))
running = True # need to break outer loop from inner loop
GREEN = (0,255,0)
RED = (255,0,0)
BLACK = (0,0,0)
BLUE = (0,0,255)
WHITE = (255,255,255)

import pygame
pygame.joystick.init()


joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

print(joysticks)

def drawRect(x,y,r,color,spinRad):
    points=[]
    RED = (255,0,0)
    points.append((x+r*cos(2*pi/6 + spinRad), y- r*sin(2*pi/6 + spinRad)))
    points.append((x+r*cos(2*pi/6 + 2*pi/6 + spinRad), y- r*sin(2*pi/6 + 2*pi/6 + spinRad)))
    points.append((x+r*cos(2*pi/6 + pi + spinRad), y- r*sin(2*pi/6 + pi + spinRad)))
    points.append((x+r*cos(2*pi/6 + 2*pi/6 + pi + spinRad ), y- r*sin(2*pi/6 + 2*pi/6 + pi+ spinRad)))
    draw.polygon(screen,color,points)
    # draw.circle(screen, RED, points[0], 5)
    # draw.circle(screen, RED, points[1], 5)
    draw.line(screen, RED, points[0], points[1],6)



ang = 0
spin = 0
x = screen.get_width()/2
y = screen.get_height()/2
mag = 5
angVel = 2*pi/90

class Player(object):

    def __init__(self):
        self.player = pygame.rect.Rect((300, 400, 50, 50))

        self.color = "white"


    def move(self, x_speed, y_speed):
        self.player.move_ip((x_speed, y_speed))

    def change_color(self, color):
        self.color = color
    
    def draw(self, game_screen):
        pygame.draw.rect(game_screen, self.color, self.player)

pygame.init()

player = Player()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.JOYBUTTONDOWN:
            print(event)
            if pygame.joystick.Joystick(0).get_button(0):
                print(event)
                player.change_color("green")
            elif pygame.joystick.Joystick(0).get_button(1):
                player.change_color("red")
            elif pygame.joystick.Joystick(0).get_button(2):
                player.change_color("blue")
            elif pygame.joystick.Joystick(0).get_button(3):
                player.change_color("yellow")
        if event.type == pygame.JOYAXISMOTION:
            print(event)


    x_speed = round(pygame.joystick.Joystick(0).get_axis(0)*10)
    y_speed = round(pygame.joystick.Joystick(0).get_axis(1)*10)
    player.move(x_speed, y_speed)


    screen.fill((0,0,0))
    player.draw(screen)
    pygame.display.update()
    clock.tick(100)

            
            





while running:
    # event.get() returns a list
    FORWARD,BACK,LEFT,RIGHT = False,False,False,False
    for evt in event.get():
        if evt.type == QUIT:
            running = False
    keyArray = key.get_pressed() 
    
    if keyArray[K_UP] or keyArray[K_w]:
        FORWARD = True
    if keyArray[K_DOWN] or keyArray[K_s]:
        BACK = True
    if keyArray[K_LEFT] or keyArray[K_a]:
        LEFT = True
    if keyArray[K_RIGHT] or keyArray[K_d]:
        RIGHT = True
    
    #------------------------
    # x = 400 + 100*cos(radians(ang))
    # y = 300 + 100*sin(radians(ang))
    # ang +=1
    screen.fill((0,0,0))
    drawRect(x,y,50,GREEN,spin)
   
    if LEFT:
        spin+= angVel
    elif RIGHT:
        spin-= angVel
    
    if FORWARD:
        x = (x + mag*cos(spin + pi/2) +800) % 800
        y = (y - mag*sin(spin + pi/2) +600) % 600
    elif BACK:
        x = (x - mag*cos(spin + pi/2) +800) % 800
        y = (y + mag*sin(spin + pi/2) +600) % 600


    spin = spin % (2*pi)
    print(f"{spin/pi:.2f}")

    
    #------------------------
    time.delay(10)
    display.flip()


quit()
    
