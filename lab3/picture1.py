
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
rect(screen, (180, 180, 180), (0, 0, 400, 400))  # fill backgroung light gray
circle(screen, (255, 255, 0), (200, 200), 100)   # yellow face
circle(screen, (0, 0, 0), (200, 200), 100, 1)    # black face border


# left eye (big)
circle(screen, (255, 0, 0), (150, 175), 20)   # red
circle(screen, (0, 0, 0), (150, 175), 20, 1)    # black border
circle(screen, (0, 0, 0), (150, 175), 9)    # black circle

# right eye (big)
circle(screen, (255, 0, 0), (250, 175), 15)   # red
circle(screen, (0, 0, 0), (250, 175), 15, 1)    # black border
circle(screen, (0, 0, 0), (250, 175), 8)    # black circle

# mouth
line(screen, (0, 0, 0), (150, 250), (250, 250), 20)

# left brow
line(screen, (0, 0, 0), (100, 115), (180, 165), 12)


# right brow
line(screen, (0, 0, 0), (220, 165), (300, 135), 12)

pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True



