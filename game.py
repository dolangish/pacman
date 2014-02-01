############################################################
#this is the main game class that our engine is based around
############################################################
import pygame, sys
from pygame.locals import *
import sprites
import collision
import colors
import directions

FPS = 30

class Game():
    def __init__(self, surface):
        self.surface=surface
        self.alive_group=pygame.sprite.Group()
        self.wall_group=pygame.sprite.Group()

    def initialize(self):
        self.clock = pygame.time.Clock()
        self.border_rect=pygame.Rect(50,50,600,600)
        pygame.display.set_caption("Pacman")

        self.pacman=sprites.Pacman([self.surface.get_width()/2,self.surface.get_height()/2])
        self.alive_group.add(self.pacman)

        wall=sprites.Wall([200,200],[100,100])
        self.alive_group.add(wall)
        self.wall_group.add(wall)
        return True;

    def update(self):
        #update each object's movement
        for sprite in self.alive_group:
            sprite.update(self.surface)
			
        #collision detection
        collision_list=collision.check_out_of_bounds(self.pacman,self.surface)
        collision_list=collision_list+collision.check_collisions(self.pacman,self.wall_group)
        
        #collision resolution
        collision.resolve_collisions(collision_list)
           		   
    def draw(self):
        self.surface.fill(colors.BG_COL)
        pygame.draw.rect(self.surface,colors.BLUE,self.border_rect,3)

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
                        self.pacman.set_direction(directions.UP)
                    elif event.key == K_s or event.key == K_DOWN:
                        self.pacman.set_direction(directions.DOWN)
                    elif event.key == K_a or event.key == K_LEFT:
                        self.pacman.set_direction(directions.LEFT)
                    elif event.key == K_d or event.key == K_RIGHT:
                        self.pacman.set_direction(directions.RIGHT)
            self.update()
                    
            self.draw()                    
            
            self.clock.tick(FPS)
