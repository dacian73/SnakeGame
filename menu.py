# Main menu
import sys
from constants import *
from helper import *



def main_menu(font, screen):
    while True:
        screen.fill(BACKGROUND_COLOR)
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        # Button rectangles
        start_button = pygame.Rect(300, 150, 400, 50)
        continue_button = pygame.Rect(300, 250, 400, 50)
        options_button = pygame.Rect(300, 350, 400, 50)
        exit_button = pygame.Rect(300, 450, 400, 50)
        
        # Draw buttons
        pygame.draw.rect(screen, BUTTON_COLOR, start_button)
        pygame.draw.rect(screen, BUTTON_COLOR, continue_button)
        pygame.draw.rect(screen, BUTTON_COLOR, options_button)
        pygame.draw.rect(screen, BUTTON_COLOR, exit_button)
        
        pygame.draw.rect(screen, BORDER_COLOR, start_button, 5)
        pygame.draw.rect(screen, BORDER_COLOR, continue_button, 5)
        pygame.draw.rect(screen, BORDER_COLOR, options_button, 5)
        pygame.draw.rect(screen, BORDER_COLOR, exit_button, 5)
        
        # Draw text on buttons
        draw_text('New Game', font, TEXT_COLOR, screen, 370, 160)
        draw_text('Continue', font, TEXT_COLOR, screen, 360, 260)
        draw_text('Options', font, TEXT_COLOR, screen, 360, 360)
        draw_text('Exit', font, TEXT_COLOR, screen, 380, 460)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(mouse_x, mouse_y):
                    print("New Game")
                if continue_button.collidepoint(mouse_x, mouse_y):
                    print("Continue")
                if options_button.collidepoint(mouse_x, mouse_y):
                    print("Options")
                if exit_button.collidepoint(mouse_x, mouse_y):
                    pygame.quit()
                    sys.exit()
        
        pygame.display.flip()