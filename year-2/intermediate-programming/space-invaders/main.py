
importcode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-pythonpygame, sys, random

pygame.init()
#definecode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-pythoncolors 
whitecode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python= 255, 255, 255
redcode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python= 255, 0, 0

#setcode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-pythonfps
clockcode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python= pygame.time.Clock()

#setcode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-pythonsize of canvas
screenWidthcode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python= 1000
screenHeightcode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python= 700

#setcode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-pythonbackground image
backgroundcode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python= pygame.image.load('Intermediate Programming (CS2513)\\CA2\\images\\background.jpg')
backgroundcode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python= pygame.transform.scale(background, (1000, 700))

#opencode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-pythonwindow
screenSizecode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python= screenWidth, screenHeight
#setcode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-pythonscreensize
screencode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python= pygame.display.set_mode(screenSize)
#setcode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-pythontitle
pygame.display.set_caption("Spacecode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-pythonInvaders")

#createcode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-pythonsprite groups
spriteListcode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python= pygame.sprite.Group()
playerListcode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python= pygame.sprite.GroupSingle()
enemyListcode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python= pygame.sprite.Group()
bulletListcode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python= pygame.sprite.Group()

#definecode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-pythonclasses
classcode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-pythonPlayer(pygame.sprite.Sprite):

code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   def __init__(self, speed):
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #super from sprite class
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       super().__init__()

code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #set player width
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       playerWidth = 50
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #set player height
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       playerHeight = 10
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #set speed
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self.speed = speed
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #set score counter
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self.score = 0

code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #set image and colour
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self.image = pygame.Surface([playerWidth, playerHeight])
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self.image.fill(white)

code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #draw the rect
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       pygame.draw.rect(self.image, white, [0, 0, playerWidth, playerHeight])
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self.rect = self.image.get_rect()
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #set base xPos
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self.rect.x = 476
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #set base yPos
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self.rect.y = 600

code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   #function to move right
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   def moveRight(self):
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #if collides with right wall
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       if self.rect.x == screenWidth-60:
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           #stay in place
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           self.rect.x == self.rect.x
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #else move right
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       else:
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           #update xPos
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           self.rect.x += self.speed

code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   #function to move left
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   def moveLeft(self):
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #if collides with left wall
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       if self.rect.x == 0:
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           #stay in place
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           self.rect.x == self.rect.x
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #else move left
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       else:
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           #update xPos
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           self.rect.x -= self.speed

code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   #method to see if player has collided with enemy
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   def enemyCollision(self):
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       collided = pygame.sprite.groupcollide(enemyList, playerList, True, False)
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       return collided



#enemycode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-pythonclass
classcode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-pythonEnemy(pygame.sprite.Sprite):
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   #to log instances of enemy class
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   _registry = []

code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   def __init__(self, speed):
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #add itself to enemy class
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self._registry.append(self)
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #super from sprite class
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       super().__init__()
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #set size
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self.enemySize = 40
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #set speed
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self.speed = speed

code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #load the image
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self.image = pygame.image.load('Intermediate Programming (CS2513)\\CA2\\images\\invaderGIF.gif')
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self.image = pygame.transform.scale(self.image, (40, 40))
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #define the rect
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self.rect = self.image.get_rect()
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       screen.blit(self.image, self.rect)
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #xPos
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self.rect.x = 0
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #yPos
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self.rect.y = 50

code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   #update the enemies position
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   def update(self):
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self.rect.x += self.speed
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self.rect.y = self.rect.y


#bulletcode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-pythonclass
classcode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-pythonBullet(pygame.sprite.Sprite):
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   #to log instances of bullet class
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   _registry = []
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   def __init__(self, x, y):
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #add itself to bullet class
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self._registry.append(self)
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       super().__init__()
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #set height
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self.height = 25
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #set width
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self.width = 5
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #set speed
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self.speed = 10

code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #set image and colour
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self.image = pygame.Surface([self.width, self.height])
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self.image.fill(red)

code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #draw the rect
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       pygame.draw.rect(self.image, red, [0, 0, self.width, self.height])
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self.rect = self.image.get_rect()
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #xPos
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self.rect.x = x
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #yPos
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self.rect.y = y
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   #method to check if bullet has collided
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   def collision(self):
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       hit = pygame.sprite.groupcollide(bulletList, enemyList, True, True)
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #if bullet goes off screen, it is killed
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       if self.rect.y == 100:
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           self.kill()
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           #return from the function
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           return
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #return the bool from hit
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       return hit

code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   #update method
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   def update(self):
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self.rect.x = self.rect.x
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self.rect.y -= 10

#gamecode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-pythonclass
classcode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-pythonGame():

code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   def __init__(self):
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #set counters for creating enemies
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self.counterY = 50
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self.counterX = 50
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   #function to create enemies
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   def createEnemies(self, enemySpeed):
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #loop to create enemies
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       for i in range(1, 12):
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           e = Enemy(enemySpeed)
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           # sets their x and y values
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           e.rect.x = self.counterX * i
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           e.rect.y += self.counterY
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           #add to sprite group
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           enemyList.add(e)
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           spriteList.add(e)
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #update counters
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self.counterY += 50
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       self.counterX == 50
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #if required enemies created, exit
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       if len(enemyList) == 55:
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           return enemyList
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #else, create new
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       else:
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           self.createEnemies(enemySpeed)


#instancecode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-pythonof game class
gcode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python= Game()

#functioncode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-pythonfor game loop
defcode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-pythongameplayLoop():

code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   #instance of player class
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   p = Player(4)
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   #add it to sprite list
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   playerList.add(p)
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   spriteList.add(p)

code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   #create enemies
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   g.createEnemies(1)
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   #set reload timer
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   pygame.time.set_timer(pygame.USEREVENT, 1000)
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   #set finished flag to know when to exit loop
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   finished = False
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   #set shotReady flag to true, so shot is available to be fired
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   shotReady = True

code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   #main gameplay loop
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   while not finished:
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #check if user clicked close window
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       for event in pygame.event.get():
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           if event.type == pygame.QUIT:
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python               finished = True
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           #if timer has reached 1 second, shot ready
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           if event.type == pygame.USEREVENT:
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python               shotReady = True
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           #check if user pressed a key
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           if event.type == pygame.KEYDOWN:
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python               #if user clicks space
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python               if event.key == pygame.K_SPACE and shotReady:
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python                   #cooldown for next shot
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python                   shotReady = False
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python                   #create an instance of the bullet class
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python                   b = Bullet(p.rect.x+20, p.rect.y-20)
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python                   #add to bullet list
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python                   bulletList.add(b)
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python                   #add to sprite list
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python                   spriteList.add(b)

code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #check for holding down keys to move
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       keys = pygame.key.get_pressed()
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       if keys[pygame.K_RIGHT]:
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           #jump to player move right func
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           p.moveRight()
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       if keys[pygame.K_LEFT]:
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           #jump to player move left func
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           p.moveLeft()

code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #check collision for all bullets
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       for b in Bullet._registry:
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           #if there is a bullet collision, increase score
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           if b.collision():
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python               p.score += 5

code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #check if enemies have collided with wall
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #iterate over all instances of Enemy class
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       for e in Enemy._registry:
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           #if an enemy collides with right border
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           if e.rect.x == screenWidth-50:
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python               #update placement and change direction
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python               for e in Enemy._registry:
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python                   e.rect.x -= 1
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python                   e.rect.y += 50
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python                   e.speed -= 2
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python               break
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           #if collides with left border
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           elif e.rect.x == 10:
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python               #update placement and change direction
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python               for e in Enemy._registry:
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python                   e.rect.x += 1
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python                   e.rect.y += 50
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python                   e.speed += 2
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python               break

code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #if theres no enemies left, increase speed and spawn again
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       if len(enemyList) == 0:
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           g.counterY = 50
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           g.counterX = 50
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           #create enemy function
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           g.createEnemies(1)

code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #check if player collides with enemy
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       if p.enemyCollision():
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           #if they have, finish the game
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python           finished = True
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #update all sprites
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       spriteList.update()

code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #load background image
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       screen.blit(background, (0, 0))

code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #define font
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       font = pygame.font.Font(None, 40)
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #set up score counter for display
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       score = font.render('Score = '+str(p.score), 1, white)
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #display score counter
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       screen.blit(score, (30, 30))
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #set up title for display
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       title = font.render('Space Invaders!', 1, white)
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #display title
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       screen.blit(title, (700, 30))

code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #draw the spriteLists
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       spriteList.draw(screen)

code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #flip display
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       pygame.display.flip()

code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       #fps counter
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python       clock.tick(60)

code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   #exit
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   pygame.quit()

#startcode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-pythongame
ifcode taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python__name__ == "__main__":
code taken from https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python   gameplayLoop()