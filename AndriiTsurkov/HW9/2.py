import pygame

FPS = 60

WIDTH_DISPLAY=500
HEIGHT_DISPLAY=500

COORD_X=50
COORD_Y=50
WIDTH_RECTANGLE=400
HEIGHT_RECTANGLE=430
DELTA_STEP=5

BLACK_COLOR = (0, 0, 0)
RED_COLOR = (250, 0, 0)

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
    
    if COORD_X > 10 and keys[pygame.K_LEFT]:
        COORD_X = COORD_X-DELTA_STEP

    if COORD_X + WIDTH_RECTANGLE < WIDTH_DISPLAY - 10 and keys[pygame.K_RIGHT]:
        COORD_X = COORD_X+DELTA_STEP

    if COORD_Y > 10 and keys[pygame.K_UP]:
        COORD_Y = COORD_Y-DELTA_STEP
    
    if COORD_Y + HEIGHT_RECTANGLE < WIDTH_DISPLAY - 10 and keys[pygame.K_DOWN]:
        COORD_Y = COORD_Y+DELTA_STEP


    gameDisplay.fill(BLACK_COLOR) 

    pygame.draw.rect(gameDisplay, RED_COLOR, [COORD_X, 
                                              COORD_Y, 
                                              WIDTH_RECTANGLE, 
                                              HEIGHT_RECTANGLE])
    pygame.display.update()
    clock.tick(FPS)
    

