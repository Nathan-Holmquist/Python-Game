
"""
OG Pong as best as I can make it
"""


import pygame
pygame.init()
bg = pygame.image.load('bg.jpg')
win = pygame.display.set_mode((800, 800))

pygame.display.set_caption("First Game")

class ball(object):
    def __init__(self, x, y, thickness, radius):

        self.x = x
        self.y = y
        self.thickness = thickness
        self.radius = radius

class paddle(object):
    def __init__(self, x, y, width, height):
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 25

def drawScreen():
    win.blit(bg, (0,0))
    pygame.draw.rect(win, (255,0,0), (left_paddle.x,left_paddle.y,left_paddle.width,left_paddle.height))
    pygame.draw.rect(win, (255,0,0), (right_paddle.x,right_paddle.y,right_paddle.width,right_paddle.height))
    pygame.draw.circle(win, (0,255,0),(pongBall.x, pongBall.y), (pongBall.thickness), (pongBall.radius) )
    pygame.display.update()



# Main
pongBall = ball(400, 400, 5, 8 )
left_paddle = paddle(5, 100, 15, 100)
right_paddle = paddle(780, 100, 15, 100)

run = True
while run:
    pygame.time.delay(80)
    drawScreen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    # Move left paddle
    if keys[pygame.K_UP] and left_paddle.y > 0:
        left_paddle.y -= left_paddle.vel
    if keys[pygame.K_DOWN] and left_paddle.y < 800 - left_paddle.height:
        left_paddle.y += left_paddle.vel

    # Move right paddle
    if keys[pygame.K_w] and right_paddle.y > 0:
        right_paddle.y -= right_paddle.vel
    if keys[pygame.K_s] and right_paddle.y < 800 - right_paddle.height:
        right_paddle.y += right_paddle.vel

pygame.quit()
