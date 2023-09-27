import pygame
import os
pygame.font.init()
pygame.mixer.init()

# DISPLAY
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(">->>->| GALAXY WAR |<-<<-<")

BORDER = pygame.Rect(WIDTH//2 - 2, 0, 4, HEIGHT)

#COLORS
FONT_COLOR = (170,76,52)
BLACK = (0, 0, 0, 0)
BLUEGRAY = (73,101,123)
YELLOW = (255, 255, 0) 
RED = (255, 0, 0)

#SOUNDS
BULLET_HIT_SOUND = pygame.mixer.Sound(
    os.path.join("Assets", "hit.mp3"))
BULLET_FIRE_SOUND = pygame.mixer.Sound(
    os.path.join("Assets","fire.mp3"))

#FONTS
HEALTH_FONT = pygame.font.SysFont("comicsans", bold=20, size=20)
IN_GAME_FONT = pygame.font.SysFont("comicsans", bold=50, size=50)

#VELOCITY AND SIZE
FPS = 60        #frame per second
VEL = 5
BULLET_VEL = 15
MAX_BULLETS = 3

SPACESHIP_WIDTH , SPACESHIP_HEIGHT = 55 ,40

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

#IMAGES
YELLOW_SPACESHIIP_IMAGE = pygame.image.load(
    os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIIP_IMAGE, (SPACESHIP_WIDTH , SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH , SPACESHIP_HEIGHT)), 270)
SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join("Assets", "space.png")), (WIDTH, HEIGHT))


def draw_window(yellow, red, yellow_bullets, red_bullets, yellow_health, red_health):
    """
    Create a window to display the game
    :param yellow:
    :param red:
    :param yellow_bullets:
    :param red_bullets:
    :param yellow_health:
    :param red_health:
    :return: None
    """
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLUEGRAY, BORDER)
    
    #HEALTH 
    yellow_health_text = HEALTH_FONT.render("HEALTH: " + str(yellow_health), 1, FONT_COLOR)
    red_health_text = HEALTH_FONT.render("HEALTH: " + str(red_health), 1, FONT_COLOR)
    WIN.blit(yellow_health_text, (10, 10))
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))

    #SPACESHIPS
    WIN.blit(YELLOW_SPACESHIIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    #BULLETS
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet) 


    pygame.display.update()


#MOVEMENT CONTROLLERS FOR SPACESHIPS
def yellow_handle_movement(keys_pressed, yellow):
    """
    Handle the movement of yellow spaceship based on keys pressed.
    :param keys_pressed:
    :param yellow:
    :return: None
    """
    if keys_pressed[pygame.K_a] and yellow.x - VEL  > 0:                                #LEFT
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x + 15:      #RIGHT    
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:                                 #UP    
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL +yellow.height < HEIGHT - 15:        #DOWN   
        yellow.y += VEL 

def red_handle_movement(keys_pressed, red):
    """
    Handle the movement of red spaceship based on keys pressed.
    :param keys_pressed:
    :param red:
    :return: None
    """
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:           #LEFT
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH + 15:           #RIGHT    
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:                                   #UP    
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:          #DOWN   
        red.y += VEL  


#CREATE BULLETS
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    """
    Handle the bullets act and movement.
    :param yellow_bullets:
    :param red_bullets:
    :param yellow:
    :param red:
    :return: None
    """
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


# WINNER SCREEN
def draw_winner(text):
    """
     Display the winner's text on the game window and pause briefly.
    :param text:
    :return: None
    """
    draw_text = IN_GAME_FONT.render(text, 1, FONT_COLOR)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    
    pygame.display.update()             #restart display    

    pygame.time.delay(1500)             #show winner text for 1.5 seconds 

# START SCREEN
def start_screen():
    """
    Display the start screen with the text "PRESS SPACE TO START".
    When the space button is pressed, the game begins.
    :return:None
    """
    start_font = pygame.font.SysFont("comicsans", bold=40, size=40)
    text = start_font.render("PRESS SPACE TO START", 1, FONT_COLOR)
    WIN.blit(SPACE, (0, 0))
    WIN.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()

# MAIN FUNCTION
def main():
    yellow = pygame.Rect(200, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red = pygame.Rect(650, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    yellow_bullets = []
    red_bullets = []

    yellow_health = 5
    red_health = 5

    clock = pygame.time.Clock()
    run_game = True   # Initialize the game state to the play game screen
    run_start = True  # Initialize the game state to the start screen

    while run_game:
        clock.tick(FPS)

        if run_start:       # Start screen
            start_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_game = False
                    pygame.quit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    run_start = False       # Switch to the game screen when SPACE is pressed
                    
        else:       # Game screen
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_game = False
                    pygame.quit()

                # QUANTITY BULLET    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:    
                        bullet = pygame.Rect(yellow.x + yellow.width, 
                                            yellow.y + yellow.height//2 - 2, 10, 5)
                        yellow_bullets.append(bullet)
                        BULLET_FIRE_SOUND.play()

                    if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:    
                        bullet = pygame.Rect(red.x ,
                                            red.y + red.height//2 - 2, 10, 5)
                        red_bullets.append(bullet) 
                        BULLET_FIRE_SOUND.play()

                #HEALTH COUNT
                if event.type == YELLOW_HIT:
                    yellow_health -= 1
                    BULLET_HIT_SOUND.play()
                if event.type == RED_HIT:
                    red_health -= 1
                    BULLET_HIT_SOUND.play()

            # SHOW THE WINNER PAGE
            winner_text = ""
            if yellow_health <= 0:
                winner_text = "RED WINS!!!"
            if red_health <= 0:
                winner_text = "YELLOW WINS!!!"
            if winner_text != "":
                WIN.blit(SPACE, (0, 0))
                draw_winner(winner_text)
                pygame.display.update()

                main()      # Reset the game state to the start screen               
            
            keys_pressed = pygame.key.get_pressed()
            yellow_handle_movement(keys_pressed, yellow)
            red_handle_movement(keys_pressed, red)
            
            handle_bullets(yellow_bullets, red_bullets, yellow, red)        
            
            draw_window(yellow, red, yellow_bullets, 
                        red_bullets, yellow_health, red_health)
            
  
    
    pygame.quit()   
if __name__ == "__main__":
    main()