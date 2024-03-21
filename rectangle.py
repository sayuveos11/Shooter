import sys
import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

rect_wight = 100
rect_height = 200

rect_x = screen_width / 2 - rect_wight / 2
rect_y = screen_height / 2 - rect_height / 2

rect_color = pygame.Color('lightyellow')


pygame.display.set_caption("My Pygame")

STEP = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and rect_y >= STEP:
                rect_y -= STEP
            if event.key == pygame.K_s and rect_y <= screen_height - rect_height - STEP :
                rect_y += STEP
            if event.key == pygame.K_a and rect_x >= STEP:
                rect_x -= STEP
            if event.key == pygame.K_d and rect_x <= screen_width - rect_wight - STEP:
                rect_x += STEP

    screen.fill((32, 52, 71))
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_wight, rect_height))
    pygame.display.update()