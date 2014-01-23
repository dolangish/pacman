import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

border_rect=pygame.Rect(50,50,600,600)
DISPLAYSURF = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Pacman")

BROWN = (205,133,63)
GRAY = (155,155,155)
BG_COL = (0,0,0)
PURPLE = (160,32,240)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        
    DISPLAYSURF.fill(BG_COL)
    pygame.draw.rect(DISPLAYSURF,BLUE,border_rect,3);

    pygame.display.update()
    fpsClock.tick(FPS)

