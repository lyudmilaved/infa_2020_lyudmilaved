import pygame
from pygame.draw import *

pygame.init()

width_screen = 500
height_screen = 700

FPS = 30

def draw_background(screen, width_screen, height_screen):
    """ Draws the background and fills it's parts.
    screen: surface on which the background will be drawn
    width_screen: width of the background
    height_screen: height of the background
    """
    rect(screen, (110, 110, 110), (0, 0, width_screen, height_screen * 0.4))  # upper grey part
    rect(screen, (0, 0, 0), (0, height_screen * 0.4, width_screen, height_screen - height_screen * 0.4))  # lower black part

def draw_cloud(screen, color, x, y, width, height, alpha=255):
    """ Draws the first cloud (if count from up to down)
    screen: the mail surface
    color: the color of the cloud
    x: left side on axis x
    y: upper side on axis y
    width: width along axis x
    height: height along axis y
    """
    cloud_surf = pygame.Surface((width, height))
    cloud_surf.set_alpha(alpha)
    cloud_surf.set_colorkey((0, 0, 0,), 0)
    ellipse(cloud_surf, color, (0, 0, width, height))
    screen.blit(cloud_surf, (x, y))

def draw_building(screen, x, y, width_building, height_building, alpha=255):
    """ Draws the main building
    x: middle of the lower side of the building, center axis of the whole building
    y: the level of the lower side of the building
    width_building: width of the building including the balcony and the roof
    height_building: height of the building including the tubes on the roof
    """
    width_main_building = width_building // 1.24
    height_main_building = height_building // 1.68
    x_on_surf = width_building // 2
    y_on_surf = height_building
    building_surf = pygame.Surface((width_building, height_building))
    building_surf.set_alpha(alpha)
    building_surf.set_colorkey((0, 0, 0,), 0)
    def draw_main_building(building_surf, x, y, width_main_building, height_main_building):
        rect(building_surf, (55, 50, 12), (x - width_main_building//2, y - height_main_building,
                                    width_main_building, height_main_building))

    def draw_roof(building_surf, x, y, width_building, height_building, height_main_building):
        """ Draws the roof of the main building"""
        width_roof = width_building
        height_roof = height_building // 19.6
        polygon(building_surf, (1, 1, 1), ((x - width_roof//2, y - height_main_building),
                                    (x + width_roof//2, y - height_main_building),
                                    (x + width_roof//3.26, y - height_roof - height_main_building),
                                    (x - width_roof//3.26, y - height_roof - height_main_building)))

    def draw_upper_windows(building_surf, x, y, width_building, height_building, height_main_building):
        """ Draws four upper windows of the main building"""
        width_upper_window = width_building // 12
        height_upper_window = height_building // 4.55
        rect(building_surf, (80, 80, 80),
             (x - width_building // 3, y - height_main_building, width_upper_window, height_upper_window)) # 1
        rect(building_surf, (80, 80, 80),
             (x - width_building // 6, y - height_main_building, width_upper_window, height_upper_window)) # 2
        rect(building_surf, (80, 80, 80),
             (x + width_building // 14.57, y - height_main_building, width_upper_window, height_upper_window)) # 3
        rect(building_surf, (80, 80, 80),
             (x + width_building // 4.3, y - height_main_building, width_upper_window, height_upper_window)) # 4

    def draw_lower_windows(building_surf, x, y, width_building, width_main_building, height_main_building):
        """ Draws three lower windows of the main building"""
        width_lower_window = width_main_building // 5
        height_lower_window = height_main_building // 5.7
        rect(building_surf, (53, 23, 12),
                            (x - width_building // 3.26, y - height_main_building // 3.5, width_lower_window, height_lower_window))  # 1
        rect(building_surf, (53, 23, 12),
                            (x - width_building // 15.5, y - height_main_building // 3.5, width_lower_window, height_lower_window))  # 2
        rect(building_surf, (245, 208, 41),
                            (x + width_building // 6, y - height_main_building // 3.5, width_lower_window, height_lower_window))  # 3

    def draw_balcony(building_surf, x, y, width_building, height_building):
        """ Draws a balcony of the main building"""
        width_lower_part_balcony = width_building
        height_lower_part_balcony = height_building // 14.75
        width_upper_part_balcony = width_building // 1.15
        height_upper_part_balcony = height_building // 39.33
        width_column1_balcony = width_building // 39
        height_column1_balcony = height_building // 20
        width_column2_balcony = width_building // 15.5
        height_column2_balcony = height_building // 20
        width_column3_balcony = width_building // 15.5
        height_column3_balcony = height_building // 20
        width_column4_balcony = width_building // 20.66
        height_column4_balcony = height_building / 20
        width_column5_balcony = width_building // 15.5
        height_column5_balcony = height_building // 20
        width_column6_balcony = width_building // 15.5
        height_column6_balcony = height_building // 20
        width_column7_balcony = width_building // 39
        height_column7_balcony = height_building // 20

        rect(building_surf, (30, 30, 30), (x - width_lower_part_balcony // 2, y - height_building // 2.67,
                                    width_lower_part_balcony, height_lower_part_balcony))  # lower part of balcony
        rect(building_surf, (30, 30, 30), (x - width_lower_part_balcony // 2.25, y - height_building // 2.25,
                                    width_upper_part_balcony, height_upper_part_balcony))  # upper part of balcony
        rect(building_surf, (30, 30, 30), (x - width_building // 2.14, y - height_building // 2.38,
                                    width_column1_balcony, height_column1_balcony))  # 1 (left) column
        rect(building_surf, (30, 30, 30), (x - width_building // 2.95, y - height_building // 2.38,
                                    width_column2_balcony, height_column2_balcony))  # 2 column
        rect(building_surf, (30, 30, 30), (x - width_building // 5.64, y - height_building // 2.38,
                                    width_column3_balcony, height_column3_balcony))  # 3 column
        rect(building_surf, (30, 30, 30), (x - width_building // 62, y - height_building // 2.38,
                                    width_column4_balcony, height_column4_balcony))  # 4 column
        rect(building_surf, (30, 30, 30), (x + width_building // 7.75, y - height_building // 2.38,
                                    width_column5_balcony, height_column5_balcony))  # 5 column
        rect(building_surf, (30, 30, 30), (x + width_building // 3.44, y - height_building // 2.38,
                                    width_column6_balcony, height_column6_balcony))  # 6 column
        rect(building_surf, (30, 30, 30), (x + width_building // 2.35, y - height_building // 2.38,
                                    width_column7_balcony, height_column7_balcony))  # 7 (right) column

    def draw_tube1(building_surf, x, y, width_building, height_building):
        """ Draws the first tube (if count from left to right) of the main building"""
        width_tube1 = width_building // 31
        height_tube1 = height_building // 11.8
        rect(building_surf, (30, 30, 30), (x - width_building // 4.77, y - height_building // 1.43,
                                     width_tube1, height_tube1))
    def draw_tube2(building_surf, x, y, width_building, height_building):
        """ Draws the second tube (if count from left to right) of the main building"""
        width_tube2 = width_building // 15.5
        height_tube2 = height_building // 9
        rect(building_surf, (30, 30, 30), (x - width_building // 6.88, y - height_building // 1.35,
                                    width_tube2, height_tube2))
    def draw_tube3(building_surf, x, y, width_building, height_building):
        """ Draws the third tube (if count from left to right) of the main building"""
        width_tube3 = width_building // 31
        height_tube3 = height_building // 19.6
        rect(building_surf, (30, 30, 30), (x + width_building // 8.86, y - height_building // 1.44,
                                    width_tube3, height_tube3))
    def draw_tube4(building_surf, x, y, width_building, height_building):
        """ Draws the fourth tube (if count from left to right) of the main building"""
        width_tube4 = width_building // 31
        height_tube4 = height_building // 11.8
        rect(building_surf, (30, 30, 30), (x + width_building // 4.76, y - height_building // 1.44,
                                    width_tube4, height_tube4))

    draw_main_building(building_surf, x_on_surf, y_on_surf, width_main_building, height_main_building)
    draw_upper_windows(building_surf, x_on_surf, y_on_surf, width_building, height_building, height_main_building)
    draw_lower_windows(building_surf, x_on_surf, y_on_surf, width_building, width_main_building, height_main_building)
    draw_roof(building_surf, x_on_surf, y_on_surf, width_building, height_building, height_main_building)
    draw_balcony(building_surf, x_on_surf, y_on_surf, width_building, height_building)
    draw_tube1(building_surf, x_on_surf, y_on_surf, width_building, height_building)
    draw_tube2(building_surf, x_on_surf, y_on_surf, width_building, height_building)
    draw_tube3(building_surf, x_on_surf, y_on_surf, width_building, height_building)
    draw_tube4(building_surf, x_on_surf, y_on_surf, width_building, height_building)
    screen.blit(building_surf, (x - width_building // 2, y - height_building))

def draw_moon(screen, x, y, moon_radius):
    """ Draws the moon"""
    circle(screen, (255, 255, 255), (450, 60), moon_radius)

def draw_ghost(screen, x, y, head_radius, alpha=255, flip_x=False, flip_y=False):
    """ Draws the ghost based on head_radius
    x, y: coordinates of the head center on the main drawing
    screen: based screen
    """
    width_surf = head_radius * 7
    height_surf = head_radius * 8
    ghost_surf = pygame.Surface((width_surf, height_surf))
    ghost_surf.set_alpha(alpha)
    ghost_surf.set_colorkey((0, 0, 0,), 0)
    x_head_center_on_surf = width_surf - head_radius * 2 # recount x coord to surface x coord
    y_head_center_on_surf = head_radius * 2 # recount y coord to surface y coord
    def draw_ghost_dress(ghost_surf, x, y):
        """ Draws the ghost's dress"""
        circle(ghost_surf, (255, 255, 255), (x + head_radius, y), head_radius * 6, 0, draw_bottom_left=True)
        circle(ghost_surf, (255, 255, 255), (x - head_radius * 0.6, y + head_radius * 1.35), head_radius * 1.75)
        ellipse(ghost_surf, (0, 0, 0), (x - head_radius * 3.1, y - head_radius * 0.3,
                                    head_radius * 1.5, head_radius * 0.4))
        ellipse(ghost_surf, (0, 0, 0), (x - head_radius * 4.75, y - head_radius * 0.3,
                                    head_radius * 1.75, head_radius * 0.4))
        ellipse(ghost_surf, (255, 255, 255), (x + head_radius * 0.75, y + head_radius * 2.25,
                                          head_radius * 0.35, head_radius * 1.75))
        ellipse(ghost_surf, (255, 255, 255), (x + head_radius * 0.75, y + head_radius * 4,
                                          head_radius * 0.35, head_radius * 1.75))
    def draw_ghost_dress_bottom(ghost_surf, x, y):
        """ Draws the ghost's dress bottom"""
        circle(ghost_surf, (0, 0, 0), (x - head_radius * 5.9, y + head_radius * 1.4),
               head_radius * 1.35)
        circle(ghost_surf, (0, 0, 0), (x - head_radius * 5.25, y + head_radius * 2.15),
               head_radius)
        circle(ghost_surf, (255, 255, 255), (x - head_radius * 3.65, y + head_radius * 2.85),
               head_radius // 1.33)
        circle(ghost_surf, (0, 0, 0), (x - head_radius * 3.35, y + head_radius * 4.5),
               head_radius // 1.11)
        circle(ghost_surf, (255, 255, 255), (x - head_radius * 1.75, y + head_radius * 4.85),
               head_radius // 1.33)
        ellipse(ghost_surf, (0, 0, 0), (x - head_radius * 1.7, y + head_radius * 5.5,
                                    head_radius * 1.5, head_radius // 1.18))
    def draw_ghost_head(ghost_surf, x, y):
        """ Draws the ghost's head"""
        circle(ghost_surf, (255, 255, 255), (x, y), head_radius)
    def draw_ghost_eyes(ghost_surf, x, y):
        """ Draws the ghost's eyes"""
        circle(ghost_surf, (176, 224, 230), (x - head_radius * 0.35, y - head_radius * 0.4), head_radius * 0.3)  # left blue
        circle(ghost_surf, (1, 1, 1), (x - head_radius * 0.4, y - head_radius * 0.45), head_radius * 0.1)  # left black
        ellipse(ghost_surf, (255, 255, 255), (x - head_radius * 0.35, y - head_radius * 0.5,
                                          head_radius * 0.25, head_radius * 0.1))  # left white
        circle(ghost_surf, (176, 224, 230), (x + head_radius * 0.4, y), head_radius * 0.3)  # right blue
        circle(ghost_surf, (1, 1, 1), (x + head_radius * 0.35, y - head_radius * 0.05), head_radius * 0.1)  # right black
        ellipse(ghost_surf, (255, 255, 255), (x + head_radius * 0.4, y - head_radius * 0.1,
                                          head_radius * 0.1, head_radius * 0.1))  # left white
    draw_ghost_dress(ghost_surf, x_head_center_on_surf, y_head_center_on_surf)
    draw_ghost_dress_bottom(ghost_surf, x_head_center_on_surf, y_head_center_on_surf)
    draw_ghost_head(ghost_surf, x_head_center_on_surf, y_head_center_on_surf)
    draw_ghost_eyes(ghost_surf, x_head_center_on_surf, y_head_center_on_surf)
    ghost_surf_rotate = pygame.transform.rotate(ghost_surf, 55)
    ghost_surf_flip = pygame.transform.flip(ghost_surf_rotate, flip_x, flip_y)
    screen.blit(ghost_surf_flip, (x - head_radius * 5, y - head_radius * 2))

screen = pygame.display.set_mode((width_screen, height_screen))

draw_background(screen, 500, 700)
draw_moon(screen, 450, 60, 40)

draw_ghost(screen, 380, 500, 20, 150)
draw_ghost(screen, 320, 530, 10, 150)
draw_ghost(screen, 450, 430, 10, 150)
draw_ghost(screen, 470, 460, 10, 150)
draw_ghost(screen, 100, 550, 10, 150, True)
draw_ghost(screen, 120, 580, 10, 150, True)

# clouds is counted from up to down
# buildings are counted from left to right
draw_cloud(screen, (60, 60, 60), 40, 60, 380, 40) # 1
draw_cloud(screen, (90, 90, 90), 240, 40, 250, 35) # 2
draw_cloud(screen, (73, 73, 73), 300, 90, 400, 35) # 3
draw_cloud(screen, (10, 10, 10), 250, 130, 380, 40, 200) # 4
draw_cloud(screen, (80, 80, 80), 100, 260, 500, 45) # 5
draw_building(screen, 230, 420, 150, 300, 170) # 2
draw_building(screen, 430, 320, 150, 300, 150) # 3 (right)
draw_cloud(screen, (70, 70, 70), -70, 350, 300, 40, 150) # 6
draw_cloud(screen, (70, 70, 70), 200, 320, 350, 45, 130) # 7
draw_building(screen, 75, 500, 150, 300) # 1 (left)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
