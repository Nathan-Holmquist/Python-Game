
"""
OG Pong as best as I can make it
"""


import pygame
pygame.init()
bg = pygame.image.load('bg.jpg')
win = pygame.display.set_mode((800, 800))

pygame.display.set_caption("First Game")

# left paddle
left_x = 5
left_y = 100
left_width = 15
left_height = 100
left_vel = 40

# right paddle
right_x = 780
right_y = 100
right_width = 15
right_height = 100
right_vel = 40

# pong ball
dot_x = 400
dot_y = 400
dot_thickness = 200
dot_radius = 5


def drawScreen():
    win.blit(bg, (0,0))
    pygame.draw.rect(win, (255,0,0), (left_x,left_y,left_width,left_height))
    pygame.draw.rect(win, (255,0,0), (right_x,right_y,right_width,right_height))
    pygame.draw.circle(win, (0,255,0),(dot_x, dot_y), (dot_radius), (dot_thickness) )
    pygame.display.update()



# Main
run = True
while run:
    pygame.time.delay(80)
    drawScreen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    # Move left paddle
    if keys[pygame.K_UP] and left_y > 0:
        left_y -= left_vel
    if keys[pygame.K_DOWN] and left_y < 800 - left_height:
        left_y += left_vel

    # Move right paddle
    if keys[pygame.K_w] and right_y > 0:
        right_y -= right_vel
    if keys[pygame.K_s] and right_y < 800 - right_height:
        right_y += right_vel

pygame.quit()
