import sys
import pygame

from constants import *
from helper import *


def new_game(font, screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_text('New Game Screen', font, WHITE, screen, 250, 250)

        # Timer
        timer = pygame.time.Clock()

        snake = [
            pygame.Rect(200, 200, 20, 20),
            pygame.Rect(180, 200, 20, 20),
            pygame.Rect(160, 200, 20, 20),
            pygame.Rect(140, 200, 20, 20),
            pygame.Rect(120, 200, 20, 20)
        ]
    
        direction = pygame.K_RIGHT

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                        direction = event.key

            # Move the snake
            if direction == pygame.K_RIGHT:
                new_head = pygame.Rect(snake[0].x + 20, snake[0].y, 20, 20)
            elif direction == pygame.K_LEFT:
                new_head = pygame.Rect(snake[0].x - 20, snake[0].y, 20, 20)
            elif direction == pygame.K_DOWN:
                new_head = pygame.Rect(snake[0].x, snake[0].y + 20, 20, 20)
            elif direction == pygame.K_UP:
                new_head = pygame.Rect(snake[0].x, snake[0].y - 20, 20, 20)

            snake.insert(0, new_head)
            snake.pop()
            
            # Clear the screen and draw the snake
            screen.fill(BLACK)
            for segment in snake:
                pygame.draw.rect(screen, SNAKE_COLOR, segment)

            timer.tick(5)
            pygame.display.flip()