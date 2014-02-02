############################################################
#this is the main game class that our engine is based around
############################################################
import pygame, sys
from pygame.locals import *
import sprites
import collision
import colors
import directions
import math
import map

FPS = 30

def get_pixels_per_unit(surface):
    return math.floor(surface.get_height()/30);

class Game():
    
    def __init__(self, surface):
        self.surface=surface
        self.alive_group=pygame.sprite.Group()
        self.wall_group=pygame.sprite.Group()
        
    def initialize(self):
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Pacman")

        #init the map
        self.map=map.Map(self.surface,[19,21])
        data=self.map.get_map_data()
        walls=self.map.set_walls(data,colors.BLUE)
        for wall in walls:
            self.alive_group.add(wall)
            self.wall_group.add(wall)
        
        #init pacman        
        pacman_size=self.map.get_cell_size()
        self.pacman=sprites.Pacman(self.surface,self.map.get_start_pos(),self.map.get_cell_size())
        self.alive_group.add(self.pacman)
        
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
