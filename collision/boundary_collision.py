from .collision import *
from directions import *

class Boundary_collision(Collision):
    def __init__(self,sprite1,surface,dir):
        Collision.__init__(self,sprite1,0)
        self.surface=surface
        self.dir=dir
        
    def resolve(self):
        if self.dir == LEFT:
            self.sprite1.set_x(0)
        if self.dir == UP:
            self.sprite1.set_y(0)
        if self.dir == RIGHT:
            self.sprite1.set_x(self.surface.get_width()-self.sprite1.get_width())
        if self.dir == DOWN:
            self.sprite1.set_y(self.surface.get_height()-self.sprite1.get_height())
		