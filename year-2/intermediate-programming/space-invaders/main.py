
import pygame, sys, random

pygame.init()
#define colors 
white = 255, 255, 255
red = 255, 0, 0

#set fps
clock = pygame.time.Clock()

#set size of canvas
screenWidth = 1000
screenHeight = 700

#set background image
background = pygame.image.load('images/background.jpg')
background = pygame.transform.scale(background, (1000, 700))

#open window
screenSize = screenWidth, screenHeight
#set screensize
screen = pygame.display.set_mode(screenSize)
#set title
pygame.display.set_caption("Space Invaders")

#create sprite groups
spriteList = pygame.sprite.Group()
playerList = pygame.sprite.GroupSingle()
enemyList = pygame.sprite.Group()
bulletList = pygame.sprite.Group()

#define classes
class Player(pygame.sprite.Sprite):

    def __init__(self, speed):
        #super from sprite class
        super().__init__()

        #set player width
        playerWidth = 50
        #set player height
        playerHeight = 10
        #set speed
        self.speed = speed
        #set score counter
        self.score = 0

        #set image and colour
        self.image = pygame.Surface([playerWidth, playerHeight])
        self.image.fill(white)

        #draw the rect
        pygame.draw.rect(self.image, white, [0, 0, playerWidth, playerHeight])
        self.rect = self.image.get_rect()
        #set base xPos
        self.rect.x = 476
        #set base yPos
        self.rect.y = 600

    #function to move right
    def moveRight(self):
        #if collides with right wall
        if self.rect.x == screenWidth-60:
            #stay in place
            self.rect.x == self.rect.x
        #else move right
        else:
            #update xPos
            self.rect.x += self.speed

    #function to move left
    def moveLeft(self):
        #if collides with left wall
        if self.rect.x == 0:
            #stay in place
            self.rect.x == self.rect.x
        #else move left
        else:
            #update xPos
            self.rect.x -= self.speed

    #method to see if player has collided with enemy
    def enemyCollision(self):
        collided = pygame.sprite.groupcollide(enemyList, playerList, True, False)
        return collided



#enemy class
class Enemy(pygame.sprite.Sprite):
    #to log instances of enemy class
    _registry = []

    def __init__(self, speed):
        #add itself to enemy class
        self._registry.append(self)
        #super from sprite class
        super().__init__()
        #set size
        self.enemySize = 40
        #set speed
        self.speed = speed

        #load the image
        self.image = pygame.image.load('images/invaderGIF.gif')
        self.image = pygame.transform.scale(self.image, (40, 40))
        
        #define the rect
        self.rect = self.image.get_rect()
        screen.blit(self.image, self.rect)
        #xPos
        self.rect.x = 0
        #yPos
        self.rect.y = 50

    #update the enemies position
    def update(self):
        self.rect.x += self.speed
        self.rect.y = self.rect.y


#bullet class
class Bullet(pygame.sprite.Sprite):
    #to log instances of bullet class
    _registry = []
    def __init__(self, x, y):
        #add itself to bullet class
        self._registry.append(self)
        super().__init__()
        #set height
        self.height = 25
        #set width
        self.width = 5
        #set speed
        self.speed = 10

        #set image and colour
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(red)

        #draw the rect
        pygame.draw.rect(self.image, red, [0, 0, self.width, self.height])
        self.rect = self.image.get_rect()
        #xPos
        self.rect.x = x
        #yPos
        self.rect.y = y
    
    #method to check if bullet has collided
    def collision(self):
        hit = pygame.sprite.groupcollide(bulletList, enemyList, True, True)
        #if bullet goes off screen, it is killed
        if self.rect.y == 100:
            self.kill()
            #return from the function
            return
        #return the bool from hit
        return hit

    #update method
    def update(self):
        self.rect.x = self.rect.x
        self.rect.y -= 10

#game class
class Game():

    def __init__(self):
        #set counters for creating enemies
        self.counterY = 50
        self.counterX = 50
    
    #function to create enemies
    def createEnemies(self, enemySpeed):
        #loop to create enemies
        for i in range(1, 12):
            e = Enemy(enemySpeed)
            # sets their x and y values
            e.rect.x = self.counterX * i
            e.rect.y += self.counterY
            #add to sprite group
            enemyList.add(e)
            spriteList.add(e)
        #update counters
        self.counterY += 50
        self.counterX == 50
        #if required enemies created, exit
        if len(enemyList) == 55:
            return enemyList
        #else, create new
        else:
            self.createEnemies(enemySpeed)


#instance of game class
g = Game()

#function for game loop
def gameplayLoop():

    #instance of player class
    p = Player(4)
    #add it to sprite list
    playerList.add(p)
    spriteList.add(p)

    #create enemies
    g.createEnemies(1)
    #set reload timer
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    #set finished flag to know when to exit loop
    finished = False
    #set shotReady flag to true, so shot is available to be fired
    shotReady = True

    #main gameplay loop
    while not finished:
        #check if user clicked close window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            #if timer has reached 1 second, shot ready
            if event.type == pygame.USEREVENT:
                shotReady = True
            #check if user pressed a key
            if event.type == pygame.KEYDOWN:
                #if user clicks space
                if event.key == pygame.K_SPACE and shotReady:
                    #cooldown for next shot
                    shotReady = False
                    #create an instance of the bullet class
                    b = Bullet(p.rect.x+20, p.rect.y-20)
                    #add to bullet list
                    bulletList.add(b)
                    #add to sprite list
                    spriteList.add(b)

        #check for holding down keys to move
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            #jump to player move right func
            p.moveRight()
        if keys[pygame.K_LEFT]:
            #jump to player move left func
            p.moveLeft()

        #check collision for all bullets
        for b in Bullet._registry:
            #if there is a bullet collision, increase score
            if b.collision():
                p.score += 5

        #check if enemies have collided with wall
        #iterate over all instances of Enemy class
        for e in Enemy._registry:
            #if an enemy collides with right border
            if e.rect.x == screenWidth-50:
                #update placement and change direction
                for e in Enemy._registry:
                    e.rect.x -= 1
                    e.rect.y += 50
                    e.speed -= 2
                break
            #if collides with left border
            elif e.rect.x == 10:
                #update placement and change direction
                for e in Enemy._registry:
                    e.rect.x += 1
                    e.rect.y += 50
                    e.speed += 2
                break

        #if theres no enemies left, increase speed and spawn again
        if len(enemyList) == 0:
            g.counterY = 50
            g.counterX = 50
            #create enemy function
            g.createEnemies(1)

        #check if player collides with enemy
        if p.enemyCollision():
            #if they have, finish the game
            finished = True
        
        #update all sprites
        spriteList.update()

        #load background image
        screen.blit(background, (0, 0))

        #define font
        font = pygame.font.Font(None, 40)
        #set up score counter for display
        score = font.render('Score = '+str(p.score), 1, white)
        #display score counter
        screen.blit(score, (30, 30))
        #set up title for display
        title = font.render('Space Invaders!', 1, white)
        #display title
        screen.blit(title, (700, 30))

        #draw the spriteLists
        spriteList.draw(screen)

        #flip display
        pygame.display.flip()

        #fps counter
        clock.tick(60)

    #exit
    pygame.quit()

#start game
if __name__ == "__main__":
    gameplayLoop()