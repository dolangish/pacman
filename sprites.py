#############################################
#this module houses all of our sprite classes
#############################################
import pygame
import colors
import directions
import math

PIXELS_PER_UNIT=5

#SPRITE BASECLASS
class Sprite(pygame.sprite.Sprite):
    def __init__(self,pos,size,color):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(pos,size)
        self.color=color

    def set_x(self,x):
        if self.rect.x != x:
            self.rect.x=x

    def set_y(self,y):
        if self.rect.y != y:
            self.rect.y=y

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def get_width(self):
        return self.rect.width

    def get_height(self):
        return self.rect.height
    
    def update(self,surface):
          pass   

    def draw(self, surface):
        pygame.draw.rect(surface,self.color,self.rect)

#PACMAN CLASS
class Pacman(Sprite):
    def __init__(self,pos):
        Sprite.__init__(self,pos,[100,100],colors.YELLOW)
        self.dir=directions.LEFT;

    def set_direction(self,new_direction):
        self.dir=new_direction

    def get_direction(self):
        return self.dir
        
    def move_up(self,unit):
        self.set_y(self.get_y()-(PIXELS_PER_UNIT*unit))
	
    def move_down(self,unit):
        self.set_y(self.get_y()+(PIXELS_PER_UNIT*unit))
		
    def move_right(self,unit):
        self.set_x(self.get_x()+(PIXELS_PER_UNIT*unit))
		
    def move_left(self,unit):
        self.set_x(self.get_x()-(PIXELS_PER_UNIT*unit))
	
            
    def update(self,surface):
        if self.dir==directions.UP:
            self.move_up(1)
        elif self.dir==directions.DOWN:
            self.move_down(1)
        elif self.dir==directions.LEFT:
            self.move_left(1)
        elif self.dir==directions.RIGHT:
            self.move_right(1)

    def get_radius(self):
        return int(math.floor(self.get_width()/2))

    def get_position(self):
        return (self.rect.midtop[0],self.rect.midleft[1])

    def draw(self,surface):
        pygame.draw.circle(surface,self.color,self.get_position(),self.get_radius(),0)

#WALL CLASS
class Wall(Sprite):
    def __init__(self,pos,size):
        Sprite.__init__(self,pos,size,colors.BLUE)
