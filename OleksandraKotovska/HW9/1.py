import pygame
import random
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 550, 200
LIGHT_BLUE = (193, 216, 251)
BLUE = (0, 0, 255)
GRAY_BLUE = (136, 184, 253) # Background color for empty user input
LIGHT_GRAY_BLUE = (175, 205, 248)  # Background color for active user input
ERROR_RED = (255, 0, 0)  # Background color for error message
FONT = pygame.font.Font(None, 36)
SECRET_NUMBER = random.randint(1, 100)
MAX_ATTEMPTS = 10

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Number Guessing Game")

# Game variables
attempts = 0
user_guess = ""
active_input = False  # Track whether the user is actively typing
error_message = ""

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_RETURN:
                try:
                    guess = int(user_guess)
                    attempts += 1
                    if guess == SECRET_NUMBER:
                        result_message = "Congratulations! You guessed the number!"
                        running = False
                    elif guess < SECRET_NUMBER:
                        result_message = "The secret number is greater. Try again."
                    else:
                        result_message = "The secret number is smaller. Try again."
                    if attempts == 10:
                        result_message = "You used all 10 tries."
                        running = False
                    user_guess = ""
                    active_input = False  # Reset active input state
                    error_message = ""  # Reset error message
                except ValueError:
                    error_message = "Invalid input. Please enter a valid number."
            elif event.key == pygame.K_BACKSPACE:
                user_guess = user_guess[:-1]
                active_input = True  # User is actively typing
            else:
                user_guess += event.unicode
                active_input = True  # User is actively typing

    screen.fill(LIGHT_BLUE)

    # Display instructions and user input
    instructions_text = FONT.render("Guess the number (1-100):", True, BLUE)
    
    # Determine the background color based on user input activity or error
    if error_message:
        user_input_bg_color = ERROR_RED
    elif active_input:
        user_input_bg_color = LIGHT_GRAY_BLUE
    else:
        user_input_bg_color = GRAY_BLUE
        
    pygame.draw.rect(screen, user_input_bg_color, (15, 55, 520, 40))  # Adjust the position and size of the input box
    user_input_text = FONT.render(user_guess, True, BLUE)
    
    screen.blit(instructions_text, (20, 20))
    screen.blit(user_input_text, (20, 60))

    # Display error message or result message
    if error_message:
        error_text = FONT.render(error_message, True, ERROR_RED)
        screen.blit(error_text, (20, 100))
    elif attempts > 0:
        result_text = FONT.render(result_message, True, BLUE)
        screen.blit(result_text, (20, 100))

    pygame.display.flip()

# Game over loop
game_over = True
while game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game_over = False

pygame.quit()
sys.exit()
