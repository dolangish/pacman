from colors import YELLOW
from .sprite import *
from directions import *
import math
import game
from collision.boundary_collision import *
from collision.wall_collision import *

class Pacman(Sprite):
    def __init__(self,pos):
        Sprite.__init__(self,pos,[100,100],YELLOW)
        self.dir=LEFT;

    def set_direction(self,new_direction):
        self.dir=new_direction

    def get_direction(self):
        return self.dir
        
    def move_up(self,unit):
        self.set_y(self.get_y()-(game.PIXELS_PER_UNIT*unit))
	
    def move_down(self,unit):
        self.set_y(self.get_y()+(game.PIXELS_PER_UNIT*unit))
		
    def move_right(self,unit):
        self.set_x(self.get_x()+(game.PIXELS_PER_UNIT*unit))
		
    def move_left(self,unit):
        self.set_x(self.get_x()-(game.PIXELS_PER_UNIT*unit))
	
    def check_collisions(self,surface, wall_group):
        ret=[]
        
        #detect out of bounds
        ret=ret+self.check_out_of_bounds(surface,ret)
               
        #detect level walls
        walls_hit=pygame.sprite.spritecollide(self,wall_group,False)
        for wall in walls_hit:
            ret.append(Wall_collision(self,wall))
            
        return ret
        
    def check_out_of_bounds(self,surface,collision_list):
        ret=[]
        if self.get_x()<0:
            ret.append(Boundary_collision(self,surface,LEFT))
        if self.get_y()<0:
            ret.append(Boundary_collision(self,surface,UP))
        if self.get_x()+self.get_width()>surface.get_rect().width:
            ret.append(Boundary_collision(self,surface,RIGHT))
        if self.get_y()+self.get_height()>surface.get_rect().height:
            ret.append(Boundary_collision(self,surface,DOWN))
        return ret
            
    def update(self,surface):
        if self.dir==UP:
            self.move_up(1)
        elif self.dir==DOWN:
            self.move_down(1)
        elif self.dir==LEFT:
            self.move_left(1)
        elif self.dir==RIGHT:
            self.move_right(1)

    def get_radius(self):
        return math.floor(self.get_width()/2)

    def get_position(self):
        return (self.rect.midtop[0],self.rect.midleft[1])

    def draw(self,surface):
        pygame.draw.circle(surface,self.color,self.get_position(),self.get_radius(),0)
