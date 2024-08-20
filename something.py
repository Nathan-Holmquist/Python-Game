
"""
A simple Pygame script to create a window and draw a red rectangle.
"""


import pygame
pygame.init()

win = pygame.display.set_mode((800, 800))

pygame.display.set_caption("First Game")

left_x = 5
left_y = 100
left_width = 15
left_height = 100
left_vel = 40

right_x = 5
right_y = 100
right_width = 15
right_height = 100
right_vel = 40

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        left_y -= left_vel
    if keys[pygame.K_DOWN]:
        left_y += left_vel
    if keys[pygame.K_w]:
        right_y -= right_vel
    if keys[pygame.K_s]:
        right_y += right_vel
    
    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (left_x,left_y,left_width,left_height))
    pygame.draw.rect(win, (255,0,0), (right_x,right_y,right_width,right_height))
    pygame.display.update()

pygame.quit()
