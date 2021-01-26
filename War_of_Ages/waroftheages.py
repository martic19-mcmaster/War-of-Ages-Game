'''
Features to implement:

1) character generation cooldown....
2) Timed character atttacks with modifiable attack speed
4) Dino riders have different hitboxes
5) Enemies are generated on a timer 

'''

import pygame
pygame.init()
(width, height) = (1500, 850)

#colors
white = (255,255,255)
silver = (192,192,192)
black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)

#initialize the window and window name

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("War of the Ages")

#space for implementing a clock


#point system

class points():
    amount = 1000

    def draw(self, window, outline=None):
        self.label = "Points: " + str(self.amount)
        font = pygame.font.SysFont('arial.ttf', 40)
        label = font.render(self.label, 1, white)
        window.blit(label, (600 + (100 - label.get_width()/2), 30 + (30 - label.get_height()/2)))

class loseOrWin():
    color = black

#classes for buttons and mobs

class button():
    width = 40
    height = 20
    color = silver
    costColor = black
    
    def __init__(self, x, y, label='', cost=''):
        self.x = x
        self.y = y
        self.label = label
        self.costLabel = cost

    
    def draw(self, window, outline=None):

        if outline:
            pygame.draw.rect(window, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)

        pygame.draw.rect(window, self.color, (self.x,self.y,self.width,self.height),0)

        font = pygame.font.SysFont('arial.ttf', 20)
        label = font.render(self.label, 1, black)
        label2 = font.render(self.costLabel, 1, self.costColor)
        window.blit(label, (self.x + (self.width/2 - label.get_width()/2), self.y + (self.height/2 - label.get_height()/2)))
        window.blit(label2,(self.x - 7 - (self.width/2 - label.get_width()/2), self.y + 20 + (self.height/2 - label.get_height()/2)))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

class enemyBase():
    health = 1000
    color = red
    x = 1350
    y = 600
    width = 220
    height = 200
    
    def draw(self, window, outline=None):
        self.label = str(int(self.health))
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height),0)
        font = pygame.font.SysFont('arial.ttf', 20)
        label = font.render(self.label, 1, white)
        window.blit(label, (self.x + (self.width/2 - label.get_width()/2), self.y + (self.height/2 - label.get_height()/2)))


class homeBase():
    health = 1000
    color = red
    x = -70
    y = 600
    width = 220
    height = 200
    
    def draw(self, window, outline=None):
        self.label = str(int(self.health))
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height),0)
        font = pygame.font.SysFont('arial.ttf', 20)
        label = font.render(self.label, 1, white)
        window.blit(label, (self.x + (self.width/2 - label.get_width()/2), self.y + (self.height/2 - label.get_height()/2)))
    

class dinoRider():
    health = 200
    damage = 0.5
    atkSpeed = 2
    walkSpeed = 0.6
    color = silver
    xpos = 100
    leftEdge = xpos - 40
    healthLabel = str(health)
    labelColor = white

    #draw function
    def create(self):
        self.healthLabel = str(int(self.health))

        #original hitbox
        '''
        pygame.draw.rect(window, black,((self.xpos)-3,717,126,86),0)
        pygame.draw.rect(window, self.color, (self.xpos,720,120,80),0)
        font = pygame.font.SysFont('arial.ttf', 20)
        label = font.render(self.healthLabel, 1, self.labelColor)
        window.blit(label, (self.xpos + (60 - label.get_width()/2), 710 + (50 - label.get_height()/2)))
        '''
        
        pygame.draw.rect(window, black,((self.xpos)-3,707,36,96),0)
        pygame.draw.rect(window, self.color,(self.xpos,710,30,90),0)
        font = pygame.font.SysFont('arial.ttf', 20)
        label = font.render(self.healthLabel, 1, self.labelColor)
        window.blit(label, (self.xpos + (15 - label.get_width()/2), 710 + (45 - label.get_height()/2)))
        

    def move(self):
        self.xpos += self.walkSpeed
        self.leftEdge = self.xpos - 40

    def stop(self):
        self.xpos -= self.walkSpeed
        self.leftEdge = self.xpos - 40

    def drawAttLabel(self):
        self.attLabel = "Attacking..."
        self.attlabelColor = red
        font = pygame.font.SysFont('arial.ttf', 20)
        label = font.render(self.attLabel, 1, self.attlabelColor)
        window.blit(label, (self.xpos+5 + (15 - label.get_width()/2), 650 + (45 - label.get_height()/2)))
    

class caveMan():
    health = 100
    damage = 0.3
    atkSpeed = 1
    walkSpeed = 0.9
    color = blue
    xpos = 70
    leftEdge = xpos - 40
    labelColor = white
    
    #draw function
    def create(self):

        self.healthLabel = str(int(self.health))
        
        pygame.draw.rect(window, black,((self.xpos)-3,707,36,96),0)
        pygame.draw.rect(window, self.color,(self.xpos,710,30,90),0)
        
        font = pygame.font.SysFont('arial.ttf', 20)
        label = font.render(self.healthLabel, 1, self.labelColor)
        window.blit(label, (self.xpos + (15 - label.get_width()/2), 710 + (45 - label.get_height()/2)))

    def move(self):
        self.xpos += self.walkSpeed
        self.leftEdge = self.xpos - 40
        
    def stop(self):
        self.xpos -= self.walkSpeed
        self.leftEdge = self.xpos - 40

    def drawAttLabel(self):
        self.attLabel = "Attacking..."
        self.attlabelColor = red
        font = pygame.font.SysFont('arial.ttf', 20)
        label = font.render(self.attLabel, 1, self.attlabelColor)
        window.blit(label, (self.xpos+5 + (15 - label.get_width()/2), 650 + (45 - label.get_height()/2)))
    
class enemyCaveMan():
    health = 100
    damage = 0.3
    atkSpeed = 1
    walkSpeed = 0.8
    color = blue
    xpos = 1400
    rightEdge = xpos + 40
    labelColor = white
    
    #draw function
    def create(self):

        self.healthLabel = str(int(self.health))
        
        pygame.draw.rect(window, black,((self.xpos)-3,707,36,96),0)
        pygame.draw.rect(window, self.color,(self.xpos,710,30,90),0)
        
        font = pygame.font.SysFont('arial.ttf', 20)
        label = font.render(self.healthLabel, 1, self.labelColor)
        window.blit(label, (self.xpos + (15 - label.get_width()/2), 710 + (45 - label.get_height()/2)))
 
    def move(self):
        self.xpos -= self.walkSpeed
        self.rightEdge = self.xpos + 40

    def stop(self):
        self.xpos += self.walkSpeed
        self.rightEdge = self.xpos + 40

    def drawAttLabel(self):
        self.attLabel = "Attacking..."
        self.attlabelColor = red
        font = pygame.font.SysFont('arial.ttf', 20)
        label = font.render(self.attLabel, 1, self.attlabelColor)
        window.blit(label, (self.xpos+ 5 + (15 - label.get_width()/2), 650 + (45 - label.get_height()/2)))

#attacking mechanics and enemy and friendly positions

def rightMostFriendly(arr):
    if len(arr) > 0:
        return arr[0]
    else:
        return 0

def leftMostEnemy(arr):
    if len(arr) > 0:
        return arr[0]
    else:
        return width

def previousMob(cm, arr):
    i = 0
    while arr[i] != cm:
        i += 1
    return arr[i-1]

def attacking(self, other):
    self.health -= other.damage
    other.health -= self.damage
    other.labelColor = red
    self.labelColor = red
    if self.health < 0:
        other.labelColor = white
    if other.health < 0:
        self.labelColor = white
    self.stop()
    other.stop()
    self.drawAttLabel()
    other.drawAttLabel()

def attBase(self, base):
    base.health -= 0.2
    self.stop()
    self.drawAttLabel()

#function for updating the window

def redrawWin():
    window.blit(background_image, [0,0])

    #this is the ground
    pygame.draw.rect(window, black, (0,800,width,90),0)
    
    generateEnemyButton.draw(window)
    quitButton.draw(window)
    pauseButton.draw(window)
    points.draw(window)
    enemyBase.draw(window)
    homeBase.draw(window)

    #base upgrade mechanics
    
    if currBase == 1:
        caveManButton.draw(window)
        dinoRiderButton.draw(window)
        upgradeButton.draw(window)
    if currBase == 2:
        swordsmanButton.draw(window)
        musketeerButton.draw(window)
        
    if isEnemy and isFriendly and len(caveMen) > 0 and len(enemies) > 0:
        if rightMostFriendly(caveMen).xpos >  leftMostEnemy(enemies).xpos-35:
            attacking(rightMostFriendly(caveMen), leftMostEnemy(enemies))
            
    if True:
        for i in enemies:
            if i.health < 0:
                enemies.remove(i)
                points.amount += 100
                break
            if i.xpos < 170:
                attBase(i, homeBase)
                
            i.move()
            if len(enemies) > 1 and i != leftMostEnemy(enemies):
                if i.xpos < previousMob(i, enemies).rightEdge:
                    i.stop()
            i.create()
        
    if isFriendly:
        for i in caveMen:
            if i.health < 0:
                caveMen.remove(i)
                break
            if i.xpos > 1300:
                attBase(i,enemyBase)
            
            i.move()
            if len(caveMen) > 1 and i != rightMostFriendly(caveMen):
                 if i.xpos > previousMob(i, caveMen).leftEdge:
                     i.stop()
            i.create()


#initialize the infinite loop

paused = False
running = True
background_image = pygame.image.load("landscape.bmp").convert()

#all buttons and points

points = points()

buttons = []

enemyBase = enemyBase()
homeBase = homeBase()

enemies = []
generateEnemyButton = button(1385, 60, "Generate Enemy")
generateEnemyButton.width = 110
enemyCounter = 0
isEnemy = True

quitButton = button(1450,30,"Quit")
pauseButton = button(1400, 30, "Pause")
pauseButton.width = 45

#level 1
friendlies = []
isFriendly = False

caveManButton = button(30, 30, "Cave Man","Point cost: 50")
caveManButton.width = 70

isCaveMan = False
caveMen = []

dinoRiderButton = button(115, 30, "Dino Rider", "Point cost: 100")
dinoRiderButton.width = 70

isDinoRider = False

upgradeButton = button(220, 30, "Upgrade", "Point cost: 200")
upgradeButton.width = 70
currBase = 1

#level 2
swordsmanButton = button(30, 30, "Swordsman")
swordsmanButton.width = 75

musketeerButton = button(120, 30, "Musketeer")
musketeerButton.width = 70

buttons.append(generateEnemyButton)
buttons.append(quitButton)
buttons.append(pauseButton)
buttons.append(caveManButton)
buttons.append(dinoRiderButton)
buttons.append(upgradeButton)
buttons.append(swordsmanButton)
buttons.append(musketeerButton)

while running:

    if not paused:
        redrawWin()
        pygame.display.update()
        
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if quitButton.isOver(pos):
                runnning = False
                pygame.quit()

            if caveManButton.isOver(pos):
                isFriendly = True
                if points.amount < 50:
                    print ("not enough points")
                else:
                    points.amount -= 50
                    caveMen.append(caveMan())

            if dinoRiderButton.isOver(pos):
                isFriendly = True
                if points.amount < 100:
                    print ("not enough points")
                else:
                    points.amount -= 100
                    caveMen.append(dinoRider())

            if generateEnemyButton.isOver(pos):
                isEnemy = True
                enemies.append(enemyCaveMan())

            if upgradeButton.isOver(pos):
                currBase += 1
                points.amount -= 200

            if pauseButton.isOver(pos):
                if paused:
                    paused = False
                else:
                    paused = True
                
                
        if event.type == pygame.MOUSEMOTION:
            for i in buttons:
                if i.isOver(pos):
                    i.color = white
                    i.costColor = white
                else:
                    i.color = silver
                    i.costColor = black


