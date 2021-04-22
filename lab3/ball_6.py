import pygame
from pygame.draw import *
from random import randint, choice
pygame.init()

FPS = 1
screen = pygame.display.set_mode((900, 700))

total_score = 0

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    """ Draws the ball"""
    global x, y, r
    x = randint(100,800)
    y = randint(100,600)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def new_ellipse():
    """ Draws the ellipse"""
    global x, y, width, height
    x = randint(100,800)
    y = randint(100,600)
    width = randint(50,100)
    height = width // randint(2,3)
    color = COLORS[randint(0, 5)]
    ellipse(screen, color, (x, y, width, height))

def figure_to_draw():
    global figure_number
    all_figuries = [new_ball, new_ellipse]
    figure_number = randint(0, 1)
    all_figuries[figure_number]()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            print("Finish! Your total score:", total_score)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            pos = event.pos
            score = 0
            if figure_number == 0:
                if (abs(pos[0] - x)**2 + abs(pos[1] - y)**2)**0.5 <= r:
                    score = 5
            if figure_number == 1:
                if (pos[0] - (x + width /2)) **2 / width**2 + (pos[1] - (y + height / 2)) **2 / height**2 <= 1:
                    score = 7
            total_score += score
            print("Score:", score)
            print("Total score:", total_score)

    figure_to_draw()
    pygame.display.update()
    screen.fill(BLACK)



pygame.quit()