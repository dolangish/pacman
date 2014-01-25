import pygame
from pygame.locals import *
from game import *

def main():
   pygame.init()
   surface = pygame.display.set_mode((700, 700))
   game=Game(surface);
   if game and game.initialize():
       game.run();

if __name__=="__main__":
    main()
