4# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Make a player
player1 =  [200, 150, 20, 20]
vel1 = [0, 0]
player1_speed = 5
score1 = 0

# make walls
'''outside layer'''
wall8 =  [30, 30, 10, 50]
wall1 =  [30, 30, 50, 10]
wall2 =  [30, 100, 10, 50]
wall9 =  [30, 170, 10, 50]
wall10 =  [30, 240, 10, 50]
wall11 =  [30, 310, 10, 50]
wall12 =  [30, 380, 10, 50]
wall13 =  [30, 520, 10, 50]
wall14 =  [30, 450, 10, 50]
wall15 =  [30, 590, 10, 50]
wall16 =  [100, 30, 50, 10]
wall17 =  [170, 30, 50, 10]
wall18 =  [240, 30, 50, 10]
wall19 =  [310, 30, 50, 10]
wall20 =  [380, 30, 50, 10]
wall21 =  [450, 30, 50, 10]
wall22 =  [520, 30, 50, 10]
wall23 =  [590, 30, 50, 10]
wall24 =  [660, 30, 50, 10]
wall25 =  [730, 30, 40, 10]

#BOTTOM
wall26 =  [100, 560, 50, 10]
wall27 =  [170, 560, 50, 10]
wall28 =  [240, 560, 50, 10]
wall29 =  [310, 560, 50, 10]
wall30 =  [380, 560, 50, 10]
wall31 =  [450, 560, 50, 10]
wall32 =  [520, 560, 50, 10]
wall33 =  [590, 560, 50, 10]
wall34 =  [660, 560, 50, 10]
wall35 =  [730, 560, 30, 10]
wall36 =  [30, 560, 50, 10]

#RIGHT
wall37 =  [760, 100, 10, 50]
wall38 =  [760, 170, 10, 50]
wall39 =  [760, 240, 10, 50]
wall40 =  [760, 310, 10, 50]
wall41 =  [760, 380, 10, 50]
wall42 =  [760, 520, 10, 50]
wall43 =  [760, 450, 10, 50]
wall44 =  [760, 590, 10, 50]
wall45 =  [760, 30, 10, 50]


'''1st Inside Layer'''
#LEFT
wall3 =  [60, 60, 10, 50]
#Boarders
wall4 =  [0, 0, 800, 10]
wall5 =  [0, 0, 10, 600]
wall6 =  [0, 590, 800, 10]
wall7 =  [790, 0, 10, 600]


walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7,
         wall8, wall9, wall10, wall11, wall12, wall13, wall14, wall15,
         wall16, wall17, wall18, wall19, wall20, wall21, wall22, wall23, wall24,
         wall25, wall26, wall27, wall28, wall29, wall30, wall31, wall32, wall33,
         wall34, wall35, wall36, wall37, wall38, wall39, wall40, wall41, wall42,
         wall43, wall44, wall45]

# Make coins
coin1 = [300, 500, 20, 20]
coin2 = [400, 200, 20, 20]
coin3 = [150, 150, 20, 20]

coins = [coin1, coin2, coin3]


# Game loop
win = False
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    up = pressed[pygame.K_UP]
    down = pressed[pygame.K_DOWN]
    left = pressed[pygame.K_LEFT]
    right = pressed[pygame.K_RIGHT]

    if left:
        vel1[0] = -player1_speed
    elif right:
        vel1[0] = player1_speed
    else:
        vel1[0] = 0

    if up:
        vel1[1] = -player1_speed
    elif down:
        vel1[1] = player1_speed
    else:
        vel1[1] = 0
        
        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the player in horizontal direction '''
    player1[0] += vel1[0]

    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player1, w):        
            if vel1[0] > 0:
                player1[0] = w[0] - player1[2]
            elif vel1[0] < 0:
                player1[0] = w[0] + w[2]

    ''' move the player in vertical direction '''
    player1[1] += vel1[1]
    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(player1, w):                    
            if vel1[1] > 0:
                player1[1] = w[1] - player1[3]
            if vel1[1]< 0:
                player1[1] = w[1] + w[3]


    ''' here is where you should resolve player collisions with screen edges '''




    ''' get the coins '''
    hit_list = []

    for c in coins:
        if intersects.rect_rect(player1, c):
            hit_list.append(c)
     
    hit_list = [c for c in coins if intersects.rect_rect(player1, c)]
    
    for hit in hit_list:
        coins.remove(hit)
        score1 += 1
        print("sound!")
        
    if len(coins) == 0:
        win = True

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, player1)
    
    for w in walls:
        pygame.draw.rect(screen, BLUE, w)

    for c in coins:
        pygame.draw.rect(screen, YELLOW, c)
        
    if win:
        font = pygame.font.Font(None, 48)
        text = font.render("You Win!", 1, GREEN)
        screen.blit(text, [400, 200])

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
