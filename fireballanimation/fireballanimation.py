import pygame
pygame.init()  
pygame.display.set_caption("sprite sheet")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

Link = pygame.image.load('gio.jpg') #load your spritesheet
Link.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)

#player variables
xpos = 500 #xpos of player
ypos = 765-232 #ypos of player
vx = 0 #x velocity of player
keys = [False, False, False, False] #this list holds whether each key has been pressed

LEFT=0
RIGHT = 1

#animation variables variables
frameWidth = 60
frameHeight = 65
RowNum = 0 #for left animation, this will need to change for other animations
frameNum = 0
ticker = 0

while not gameover:
    clock.tick(60) #FPS
    
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[0]=True
            elif event.key == pygame.K_RIGHT:
                keys[1]=True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[0]=False
            elif event.key == pygame.K_RIGHT:
                keys[1]=False
          

    #LEFT MOVEMENT
    if keys[0]==True:
        vx=-3
        direction = 0
    #RIGHT MOVEMENT
    elif keys[1] == True:
        vx = 3
    #turn off velocity
    else:
        vx = 0
        
    #UPDATE POSITION BASED ON VELOCITY
        
    xpos+=vx #update player xpos
        
    #ANIMATION-------------------------------------------------------------------
        
    # Update Animation Information
    # Onyl animate when in motion
    
    if vx < 0: #left animation
        RowNum = 1
        ticker+=1
        if ticker%10==0: 
          frameNum+=1
        if frameNum>3: 
           frameNum = 0
    if vx > 0:
        RowNum = 2
        ticker+=1
        if ticker%10==0: 
          frameNum+=1
        if frameNum>3: 
           frameNum = 0
  
    # RENDER--------------------------------------------------------------------------------
    # Once we've figured out what frame we're on and where we are, time to render.
            
    screen.fill((255,255,255)) #wipe screen so it doesn't smear
    screen.blit(Link, (xpos, ypos), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight))
    pygame.draw.rect(screen, (244, 114, 9), (0, 600, 800, 500))
    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------
pygame.quit()

