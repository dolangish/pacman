import pygame, sys
from pygame.locals import *

FPS = 30

BROWN = (205,133,63)
GRAY = (155,155,155)
BG_COL = (0,0,0)
PURPLE = (160,32,240)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

class Entity():
    
    def __init__(self, color):
        self.color=color
        self.rect=pygame.Rect(100,100,200,200)

    def update(self):
        if self.rect.x < 300:
            self.rect.x=self.rect.x+1        

    def draw(self, surface):
        pygame.draw.rect(surface,self.color,self.rect)

class Game():

    def __init__(self, surface):
        self.surface=surface
        self.entity_list=[]

    def initialize(self):
        self.clock = pygame.time.Clock()
        self.border_rect=pygame.Rect(50,50,600,600)
        pygame.display.set_caption("Pacman")
        
        self.entity_list.append(Entity(RED))
        return True;

    def update(self):
        for entity in self.entity_list:
            entity.update()

    def draw(self):
        self.surface.fill(BG_COL)
        pygame.draw.rect(self.surface,BLUE,self.border_rect,3)

        for entity in self.entity_list:
            entity.draw(self.surface)

        pygame.display.update()

    def run(self):
        while True: # main game loop
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                    
            self.update()
                    
            self.draw()                    
            
            self.clock.tick(FPS)

def main():
   pygame.init()
   surface = pygame.display.set_mode((700, 700))
   game=Game(surface);
   if game and game.initialize():
       game.run();

if __name__=="__main__":
    main()
