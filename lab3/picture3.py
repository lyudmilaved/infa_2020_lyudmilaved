
import pygame
from pygame.draw import *


pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 700))

# draw background
rect(screen, (110, 110, 110), (0, 0, 500, 300))  #  upper grey part
rect(screen, (0, 0, 0), (0, 300, 500, 400))  # lower black part


# draw the clouds behind the buildings
ellipse(screen, (45, 45, 45), (253, 150, 300, 45)) #forth cloud
ellipse(screen, (70, 70, 70), (120, 275, 400, 40)) #fifth cloud


#draw the lowest cloud behind the building
ellipse(screen, (45, 45, 45), (253, 150, 300, 45))

# draw building
building_surf = pygame.Surface((310, 500))
building_surf.set_colorkey((0, 0, 0,), 0)

rect(building_surf, (55, 50, 12), (30, 150, 250, 350))  #the main part coloured "Army" color
polygon(building_surf, (1, 1, 1), ((0, 150), (310, 150), (250, 120), (60, 120))) # black roof
rect(building_surf, (80, 80, 80), (50, 153, 30, 145))  # 1 left upper window
rect(building_surf, (80, 80, 80), (100, 153, 30, 145))  # 2 upper window
rect(building_surf, (80, 80, 80), (160, 153, 30, 145))  # 3 upper window
rect(building_surf, (80, 80, 80), (220, 153, 30, 145))  # 4 right upper window
rect(building_surf, (53, 23, 12), (60, 400, 50, 60))  # 1 left lower window
rect(building_surf, (53, 23, 12), (135, 400, 50, 60))  # 2 lower window
rect(building_surf, (245, 208, 41), (210, 400, 50, 60))  # 3 right yellow lower window

# draw dark grey balcony
rect(building_surf, (30, 30, 30), (0, 300, 310, 40))  # lower part of balcony
rect(building_surf, (30, 30, 30), (20, 250, 270, 15))  # upper part of balcony
rect(building_surf, (30, 30, 30), (10, 265, 10, 35))  # 1 (left) column
rect(building_surf, (30, 30, 30), (50, 265, 20, 35))  # 2 column
rect(building_surf, (30, 30, 30), (100, 265, 20, 35))  # 3 column
rect(building_surf, (30, 30, 30), (150, 265, 15, 35))  # 4 column
rect(building_surf, (30, 30, 30), (195, 265, 20, 35))  # 5 column
rect(building_surf, (30, 30, 30), (245, 265, 20, 35))  # 6 column
rect(building_surf, (30, 30, 30), (290, 265, 10, 35))  # 7 (right) column

# draw the tubes on the roof behind the clouds
rect(building_surf, (30, 30, 30), (90, 90, 10, 50))  # 1 (left) tube
rect(building_surf, (30, 30, 30), (190, 90, 10, 30))  # 3 tube

# draw the tubes on the roof above the clouds
rect(building_surf, (30, 30, 30), (110, 40, 20, 100))  # 2  tube
rect(building_surf, (30, 30, 30), (220, 90, 10, 50))  # 4 tube



# draw the white moon
circle(screen, (255, 255, 255), (450, 60), 40)

# draw the clouds
ellipse(screen, (73, 73, 73), (30, 65, 400, 50))
ellipse(screen, (90, 90, 90), (200, 40, 300, 45))


# draw the goast
goast_surf = pygame.Surface((150, 170))
goast_surf.set_colorkey((0, 0, 0,), 0)
goast_surf.set_alpha(170)

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
circle(goast_surf, (1, 1, 1), (117, 11), 2) # left black
ellipse(goast_surf, (255, 255, 255), (118, 10, 5, 2)) # left white

circle(goast_surf, (176, 224, 230), (133, 20), 6) # right blue
circle(goast_surf, (1, 1, 1), (132, 19), 2) # right black
ellipse(goast_surf, (255, 255, 255), (133, 18, 5, 2)) # left white

# create and draw small goasts
small_goast_look_left1 = pygame.Surface.copy(pygame.transform.scale
             (goast_surf, (goast_surf.get_width()//2, goast_surf.get_height()//2)))
small_goast_look_left1.set_alpha(120) # the first small goast (left)
small_goast_look_left2 = pygame.Surface.copy(small_goast_look_left1)
small_goast_look_left2.set_alpha(120)
small_goast_look_left3 = pygame.Surface.copy(small_goast_look_left1)
small_goast_look_left3.set_alpha(120)

small_goast_look_right1 = pygame.transform.flip(small_goast_look_left1, True, False)
small_goast_look_right1.set_alpha(120)
small_goast_look_right2 = pygame.transform.flip(small_goast_look_left1, True, False)
small_goast_look_right2.set_alpha(120)

screen.blit(pygame.transform.rotate(goast_surf, 45), (255, 520))
screen.blit(pygame.transform.rotate(small_goast_look_left1, 45), (250, 540))
screen.blit(pygame.transform.rotate(small_goast_look_left2, 45), (390, 440))
screen.blit(pygame.transform.rotate(small_goast_look_left3, 45), (410, 470))
screen.blit(pygame.transform.rotate(small_goast_look_right1, -45), (10, 550))
screen.blit(pygame.transform.rotate(small_goast_look_right2, -45), (30, 590))

# create and draw three buildings
building_surf_final = pygame.transform.scale(building_surf, (building_surf.get_width()//2, building_surf.get_height()//2))
first_building_surf = pygame.Surface.copy(building_surf_final)
second_building_surf = pygame.Surface.copy(building_surf_final)
second_building_surf.set_alpha(150)
third_building_surf = pygame.Surface.copy(building_surf_final)
third_building_surf.set_alpha(100)




screen.blit(second_building_surf, (150, 180))
screen.blit(third_building_surf, (345, 90))

# draw the third cloud above the third building
ellipse(screen, (90, 90, 90), (270, 105, 400, 35))

# draw sixth and seventh clouds
sixth_seventh_cloud_surf = pygame.Surface((600, 75))
sixth_seventh_cloud_surf.set_colorkey((0, 0, 0))
sixth_seventh_cloud_surf.set_alpha(120)
ellipse(sixth_seventh_cloud_surf, (70, 70, 70), (200, 0, 400, 45)) # sixth cloud
ellipse(sixth_seventh_cloud_surf, (70, 70, 70), (0, 30, 200, 45)) # seventh cloud
screen.blit(sixth_seventh_cloud_surf, (0, 320))

screen.blit(first_building_surf, (0, 270))  # add left (first) building



pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

