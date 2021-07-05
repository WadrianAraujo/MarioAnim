import pygame
from pygame.locals import *

screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Mario")

UP = 0
RIGHT = 1
LEFT = 2
direction = 1

walk = [pygame.image.load("assets/walk1.png"),
        pygame.image.load("assets/walk2.png"),
        pygame.image.load("assets/walk3.png"),
        pygame.image.load("assets/walk1.png"),
        pygame.image.load("assets/walk2.png"),
        pygame.image.load("assets/walk3.png")]

walk1 = [pygame.image.load("assets/walk1.png"),
        pygame.image.load("assets/walk1.png"),
        pygame.image.load("assets/walk2.png"),
        pygame.image.load("assets/walk2.png"),
        pygame.image.load("assets/walk3.png"),
        pygame.image.load("assets/walk3.png")]

jump = [pygame.image.load("assets/jump1.png"),
        pygame.image.load("assets/jump2.png"),
        pygame.image.load("assets/jump1.png"),
        pygame.image.load("assets/jump2.png"),
        pygame.image.load("assets/jump2.png"),
        pygame.image.load("assets/jump1.png")]

cont_image = 0

clock = pygame.time.Clock()

mario = pygame.image.load("assets/walk1.png")

def update():
    global walk, jump , cont_image, direction

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                direction = UP
            if event.key == K_RIGHT:
                direction = RIGHT
            if event.key == K_LEFT:
                direction = LEFT

    cont_image += 1
    print(cont_image)
    if cont_image >= 6:
        cont_image = 0


    if direction == RIGHT:
        mario = walk[cont_image]
    if direction == UP:
        mario = jump[cont_image]
    if direction == LEFT:
        mario = walk1[cont_image]    
    

    screen.fill((255,255,255))
    mario = pygame.transform.scale(mario, (400, 400))
    screen.blit(mario,(100,100))
    
    pygame.display.update()

while True:
    update()
    clock.tick(7)