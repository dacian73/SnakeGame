import sys
import pygame

from constants import *
from menu import main_menu

# PyGame Initialization
pygame.init()

# Set screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Main Menu')
# Framerate
framerate = 60
# Initialize font
font = pygame.font.Font("freesansbold.ttf", 38)

# Main menu
main_menu(font, screen)
