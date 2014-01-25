from colors import YELLOW
from .sprite import *
from directions import *
import math
import game

class Pacman(Sprite):
    def __init__(self,pos):
        Sprite.__init__(self,pos,[100,100],YELLOW)
        self.dir=LEFT;

    def set_direction(self,new_direction):
        self.dir=new_direction

    def update(self,surface):
        if self.dir==UP:
            self.set_y(self.get_y()-game.PIXELS_PER_UNIT)
        elif self.dir==DOWN:
            self.set_y(self.get_y()+game.PIXELS_PER_UNIT)
        elif self.dir==LEFT:
            self.set_x(self.get_x()-game.PIXELS_PER_UNIT)
        elif self.dir==RIGHT:
            self.set_x(self.get_x()+game.PIXELS_PER_UNIT)
        if self.get_x() < 0:
            self.set_x(0)
        if self.get_y() < 0:
            self.set_y(0)
        if self.get_x()+self.get_width() > surface.get_width():
            self.set_x(surface.get_width()-self.get_width())
        if self.get_y()+self.get_height() > surface.get_height():
            self.set_y(surface.get_height()-self.get_height())

    def get_radius(self):
        return math.floor(self.get_width()/2)

    def get_position(self):
        return (self.rect.midtop[0],self.rect.midleft[1])

    def draw(self,surface):
        pygame.draw.circle(surface,self.color,self.get_position(),self.get_radius(),0)
