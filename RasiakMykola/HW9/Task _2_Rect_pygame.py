
# 09.2 PRACTICAL TASK / [GITHUB TOPIC 9]

# Task_2
import pygame

FPS = 60

WIDTH_DISPLAY=500
HEIGHT_DISPLAY=500

COORD_X = 50
COORD_Y = 50
WIDTH_RECTANGLE=40
HEIGHT_RECTANGLE=60
DELTA_STEP=5

BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)

pygame.init()


gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)

pygame.display.set_caption("My first game")


run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
#---------------------------------------------------------------------------------------
    if keys[pygame.K_LEFT] and COORD_X > DELTA_STEP:
        COORD_X = COORD_X-DELTA_STEP
    if keys[pygame.K_RIGHT] and COORD_X + WIDTH_RECTANGLE + DELTA_STEP < WIDTH_DISPLAY:
        COORD_X = COORD_X+DELTA_STEP
    if keys[pygame.K_UP] and  DELTA_STEP < COORD_Y: 
        COORD_Y = COORD_Y-DELTA_STEP
    if keys[pygame.K_DOWN] and COORD_Y + HEIGHT_RECTANGLE < HEIGHT_DISPLAY - DELTA_STEP:
        COORD_Y = COORD_Y+DELTA_STEP
#---------------------------------------------------------------------------------------

    gameDisplay.fill(BLACK_COLOR) 

    pygame.draw.rect(gameDisplay, WHITE_COLOR, [COORD_X, 
                                              COORD_Y, 
                                              WIDTH_RECTANGLE, 
                                              HEIGHT_RECTANGLE])
    pygame.display.update()
    clock.tick(FPS)
    

