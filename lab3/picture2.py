
import pygame
from pygame.draw import *


pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 700))

# draw background
rect(screen, (0, 0, 0), (0, 300, 500, 400))  # fill backgroung black
rect(screen, (110, 110, 110), (0, 0, 500, 300))  # fill backgroung  grey

#draw the lowest cloud behind the building
ellipse(screen, (45, 45, 45), (253, 150, 300, 45))

# draw building
rect(screen, (55, 50, 12), (30, 150, 250, 350))  #the main part coloured "Army" color
polygon(screen, (0, 0, 0), ((0, 150), (310, 150), (250, 120), (60, 120))) # black roof
rect(screen, (80, 80, 80), (50, 153, 30, 145))  # 1 left upper window
rect(screen, (80, 80, 80), (100, 153, 30, 145))  # 2 upper window
rect(screen, (80, 80, 80), (160, 153, 30, 145))  # 3 upper window
rect(screen, (80, 80, 80), (220, 153, 30, 145))  # 4 right upper window
rect(screen, (53, 23, 12), (60, 400, 50, 60))  # 1 left lower window
rect(screen, (53, 23, 12), (135, 400, 50, 60))  # 2 lower window
rect(screen, (245, 208, 41), (210, 400, 50, 60))  # 3 right yellow lower window

# draw dark grey balcony
rect(screen, (30, 30, 30), (0, 300, 310, 40))  # lower part of balcony
rect(screen, (30, 30, 30), (20, 250, 270, 15))  # upper part of balcony
rect(screen, (30, 30, 30), (10, 265, 10, 35))  # 1 (left) column
rect(screen, (30, 30, 30), (50, 265, 20, 35))  # 2 column
rect(screen, (30, 30, 30), (100, 265, 20, 35))  # 3 column
rect(screen, (30, 30, 30), (150, 265, 15, 35))  # 4 column
rect(screen, (30, 30, 30), (195, 265, 20, 35))  # 5 column
rect(screen, (30, 30, 30), (245, 265, 20, 35))  # 6 column
rect(screen, (30, 30, 30), (290, 265, 10, 35))  # 7 (right) column

# draw the tubes on the roof behind the clouds
rect(screen, (30, 30, 30), (90, 90, 10, 50))  # 1 (left) tube
rect(screen, (30, 30, 30), (190, 90, 10, 30))  # 3 tube

# draw the white moon
circle(screen, (255, 255, 255), (450, 60), 40) 

# draw the clouds
ellipse(screen, (73, 73, 73), (30, 65, 400, 50))
ellipse(screen, (90, 90, 90), (200, 40, 300, 45))
ellipse(screen, (90, 90, 90), (270, 105, 400, 35))

# draw the tubes on the roof above the clouds
rect(screen, (30, 30, 30), (110, 40, 20, 100))  # 2  tube
rect(screen, (30, 30, 30), (220, 90, 10, 50))  # 4 tube

# draw the goast
goast_surf = pygame.Surface((150, 170))
goast_surf.fill((0, 0, 0))

# body
circle(goast_surf, (255, 255, 255), (145, 20), 120, 0, draw_bottom_left=True)
circle(goast_surf, (255, 255, 255), (113, 47), 35)
ellipse(goast_surf, (0, 0, 0), (63, 14, 30, 8))
ellipse(goast_surf, (0, 0, 0), (30, 14, 35, 8))
ellipse(goast_surf, (255, 255, 255), (140, 65, 7, 35))
ellipse(goast_surf, (255, 255, 255), (140, 100, 7, 35))

# dress_bottom
circle(goast_surf, (0, 0, 0), (7, 48), 27)
circle(goast_surf, (0, 0, 0), (20, 63), 20)
circle(goast_surf, (255, 255, 255), (52, 77), 15)
circle(goast_surf, (0, 0, 0), (58, 110), 18)
circle(goast_surf, (255, 255, 255), (90, 117), 15)
ellipse(goast_surf, (0, 0, 0), (91, 130, 30, 17))



# head
circle(goast_surf, (255, 255, 255), (125, 20), 20)


# eyes
circle(goast_surf, (176, 224, 230), (118, 12), 6) # left blue 
circle(goast_surf, (0, 0, 0), (117, 11), 2) # left black
ellipse(goast_surf, (255, 255, 255), (118, 10, 5, 2)) # left white

circle(goast_surf, (176, 224, 230), (133, 20), 6) # right blue
circle(goast_surf, (0, 0, 0), (132, 19), 2) # right black
ellipse(goast_surf, (255, 255, 255), (133, 18, 5, 2)) # left white





screen.blit(pygame.transform.rotate(goast_surf, 45), (255, 520))



pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

