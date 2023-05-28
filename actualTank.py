from pygame import *
from math import *
joystick.init()
# joysticks = [joystick.Joystick(x) for x in range(joystick.get_count())]
screen = display.set_mode((1024,768))
HEIGHT = screen.get_height()
WIDTH = screen.get_width()
BLACK = (0,0,0)
BLUE = (0,0,255)
bulletVel = 14
bulletLife = 6000
reloadPeriod = 5000
loads = 5
margin = 50
X = 0
Y = 1
VX = 2
VY = 3
TIME = 4
running = True # need to break outer loop from inner loop
redTank = image.load('assets/redTank.png')


def velComponents(heading,d):
    return d*cos(heading+pi/2) , -d*sin(heading + pi/2)

class tank:
    def __init__(self,surf, img, x, y, angle, col):
        self.surf = surf
        self.img = img
        self.x = x
        self.y = y
        self.angle = angle
        
        self.offsetDown = 13
        self.col = col

        self.angVel = 2*pi/40
        self.mag = 10

        self.bulletVel = 11
        self.shots = []
        self.loads = loads
    def update(self,forward, back, left, right,shooting):
        # self.forward = forward
        # self.back = back
        # self.left = left
        # self.right = right
        # self.shooting = shooting
        
            

        if left:
            self.angle += self.angVel
        elif right:
            self.angle -= self.angVel
        
        if forward:
            self.x = (self.x + self.mag*cos(self.angle  + pi/2) + WIDTH) % WIDTH
            self.y = (self.y - self.mag*sin(self.angle  + pi/2) + HEIGHT) % HEIGHT
        elif back:
            self.x = (self.x - self.mag*cos(self.angle  + pi/2) + WIDTH) % WIDTH
            self.y = (self.y + self.mag*sin(self.angle  + pi/2) + HEIGHT) % HEIGHT

        rotated_image = transform.rotate(self.img, degrees(self.angle))
        rotatedCenter = (self.offsetDown * cos(self.angle+pi/2) + self.x,  -self.offsetDown * sin(self.angle + pi/2) + self.y+self.offsetDown)
        new_rect = rotated_image.get_rect(center = rotatedCenter)


        self.surf.blit(rotated_image, new_rect)
        draw.circle(self.surf, self.col, (self.x, self.y+self.offsetDown), 10)
        draw.rect(self.surf, self.col, new_rect, 2)

        if shooting and self.loads != 0:
            muzX, muzY = rotatedCenter[:2]
            vx,vy = velComponents(self.angle, bulletVel)
            self.shots.append([muzX,muzY,vx,vy,time.get_ticks()])
            self.loads -= 1
        if 0<= time.get_ticks()%5000 <= margin:
            print('reloaded')
            self.loads = loads
        # print(time.get_ticks()%5000)
        for shot in self.shots:
            if shot[X]  <= 0 or shot[X]>=screen.get_width():
                shot[VX] = -shot[VX]
            if shot[Y] <= 0 or shot[Y] >= screen.get_height():
                shot[VY] = -shot[VY]

            shot[X] += shot[VX]
            shot[Y] += shot[VY]
        for i in range(len(self.shots)):  
            shot = self.shots[i]
            if time.get_ticks() - shot[TIME] >= bulletLife:
                del self.shots[i]
                break
            if 0 <= shot[X] <= screen.get_width() and 0 <= shot[Y] <= screen.get_height():
                draw.circle(screen, self.col, shot[:2], 5)

        

tankLeft = tank(screen, redTank, 200, screen.get_height()/2, 0, BLACK)
tankRight = tank(screen, redTank, 800, screen.get_height()/2, 0, BLUE)
tankRight.mag = 18

class Tank:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
    def move(self, x, y):
        self.x = x
        self.y = y
    def draw(self, surf):
        surf.blit(self.image, (self.x, self.y))


def moveTank(surf, image, rad, x, y):
    rotated_image = transform.rotate(image, degrees(rad))
    offsetToDown = 13
    rotatedCenter = (offsetToDown * cos(rad+pi/2) + x,  -offsetToDown * sin(rad + pi/2) + y+offsetToDown)
    new_rect = rotated_image.get_rect(center = rotatedCenter)
    surf.blit(rotated_image, new_rect)
    draw.circle(surf, (0,0,0), (x, y+offsetToDown), 5)




# x = screen.get_width()/2
# y = screen.get_height()/2
# self.mag = 10
# angVel = 2*pi/40

myClock = time.Clock()
while running:
    rightShoot,leftShoot = False, False
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == KEYDOWN:
            if evt.key == K_SPACE:
                rightShoot = True
            if evt.key == K_TAB:
                leftShoot = True
    keyArray = key.get_pressed()
    # joyHat = joysticks[0].get_hat(0)
    
    # if keyArray[K_UP] or keyArray[K_w]:
    #     FORWARD = True
    # if keyArray[K_DOWN] or keyArray[K_s]:
    #     BACK = True
    # if keyArray[K_LEFT] or keyArray[K_a]:
    #     LEFT = True
    # if keyArray[K_RIGHT] or keyArray[K_d]:
    #     RIGHT = True
    #------------------------
    # keyArray[K_UP],keyArray[K_DOWN],keyArray[K_LEFT],keyArray[K_RIGHT]
    screen.fill((155,155,155))
    tankLeft.update(keyArray[K_w],keyArray[K_s],keyArray[K_a],keyArray[K_d],leftShoot)
    tankRight.update(keyArray[K_UP],keyArray[K_DOWN],keyArray[K_LEFT],keyArray[K_RIGHT], rightShoot)

    #------------------------
    display.flip()
    myClock.tick(30)
quit()
    
