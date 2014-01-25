import pygame, sys
from pygame.locals import *
from sprites.pacman import *
from sprites.wall import *
from colors import *

FPS = 30

PIXELS_PER_UNIT=5

class Game():
    def __init__(self, surface):
        self.surface=surface
        self.alive_group=pygame.sprite.Group()

    def initialize(self):
        self.clock = pygame.time.Clock()
        self.border_rect=pygame.Rect(50,50,600,600)
        pygame.display.set_caption("Pacman")

        self.pacman=Pacman([self.surface.get_width()/2,self.surface.get_height()/2])
        self.alive_group.add(self.pacman)

        wall=Wall([200,200],[100,100])
        self.alive_group.add(wall)
        return True;

    def update(self):
        for sprite in self.alive_group:
            sprite.update(self.surface)

    def draw(self):
        self.surface.fill(BG_COL)
        pygame.draw.rect(self.surface,BLUE,self.border_rect,3)

        for sprite in self.alive_group.sprites():
            sprite.draw(self.surface)

        pygame.display.update()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type== KEYDOWN:
                    if event.key == K_w or event.key == K_UP:
                        self.pacman.set_direction(UP)
                    elif event.key == K_s or event.key == K_DOWN:
                        self.pacman.set_direction(DOWN)
                    elif event.key == K_a or event.key == K_LEFT:
                        self.pacman.set_direction(LEFT)
                    elif event.key == K_d or event.key == K_RIGHT:
                        self.pacman.set_direction(RIGHT)
            self.update()
                    
            self.draw()                    
            
            self.clock.tick(FPS)
