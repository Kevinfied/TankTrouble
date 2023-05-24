from pygame import *
from math import *
joystick.init()
joysticks = [joystick.Joystick(x) for x in range(joystick.get_count())]
screen = display.set_mode((800,600))
running = True # need to break outer loop from inner loop
tank = image.load('assets/redTank.png')


def moveTank(surf, image, rad, x, y):
    rotated_image = transform.rotate(image, degrees(rad))
    
    ogImageCenter = (x,y)
    offsetToDown = 13
    tankCenterX = ogImageCenter[0]
    tankCenterY = ogImageCenter[1]+offsetToDown
    rotatedCenter = (offsetToDown * cos(rad+pi/2) + x,  -offsetToDown * sin(rad + pi/2) + y+offsetToDown)

    new_rect = rotated_image.get_rect(center = rotatedCenter)

    surf.blit(rotated_image, new_rect)
    draw.circle(surf, (0,0,0), (tankCenterX, tankCenterY), 5)

spin = 0
x = screen.get_width()/2
y = screen.get_height()/2
mag = 5
angVel = 2*pi/40

myClock = time.Clock()
while running:
    FORWARD,BACK,LEFT,RIGHT = False,False,False,False
    for evt in event.get():
        if evt.type == QUIT:
            running = False
    keyArray = key.get_pressed()
    joyHat = joysticks[0].get_hat(0)
    
    if keyArray[K_UP] or keyArray[K_w] or joyHat[1] == 1:
        FORWARD = True
    if keyArray[K_DOWN] or keyArray[K_s] or joyHat[1] == -1:
        BACK = True
    if keyArray[K_LEFT] or keyArray[K_a] or joyHat[0] == -1:
        LEFT = True
    if keyArray[K_RIGHT] or keyArray[K_d] or joyHat[0] == 1:
        RIGHT = True
    
    #------------------------
    screen.fill((155,155,155))
    moveTank(screen, tank, spin,x,y)

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
    display.flip()
    myClock.tick(30)
quit()
    
