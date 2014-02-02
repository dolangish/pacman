#############################################
#this module houses all of our sprite classes
#############################################
import pygame
import colors
import directions
import math
import game

#SPRITE BASECLASS
class Sprite(pygame.sprite.Sprite):
    def __init__(self,surface,pos,size,color):
        pygame.sprite.Sprite.__init__(self)
        self.surface=surface
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

    def move(self,vector):
        self.set_x(self.get_x()+vector[0])
        self.set_y(self.get_y()+vector[1])
        
    def get_rect(self):
        return self.rect
        
    def get_width(self):
        return self.rect.width

    def get_height(self):
        return self.rect.height
    
    def update(self,surface):
          pass  

    def resolve_collision(self,vector,sprite):
        resolve_vector=[-vector[0],-vector[1]]
        while self.get_rect().colliderect(sprite.get_rect()):
            self.move(resolve_vector)
    
    def draw(self, surface):
        pygame.draw.rect(surface,self.color,self.rect)

#PACMAN CLASS
class Pacman(Sprite):
    speed=0.2
    
    def __init__(self,surface,pos,size):
        Sprite.__init__(self,surface,pos,size,colors.YELLOW)
        self.dir=directions.LEFT;

    def set_direction(self,new_direction):
        self.dir=new_direction

    def get_direction(self):
        return self.dir
        
    def move_up(self,unit):
        self.set_y(self.get_y()-(game.get_pixels_per_unit(self.surface)*unit*self.speed))
	
    def move_down(self,unit):
        self.set_y(self.get_y()+(game.get_pixels_per_unit(self.surface)*unit*self.speed))
		
    def move_right(self,unit):
        self.set_x(self.get_x()+(game.get_pixels_per_unit(self.surface)*unit*self.speed))
		
    def move_left(self,unit):
        self.set_x(self.get_x()-(game.get_pixels_per_unit(self.surface)*unit*self.speed))
	
            
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
        rect=self.rect.copy()
        rect.width=rect.width-4
        rect.x=rect.x+2
        rect.height=rect.height-4
        rect.y=rect.y+2
        pygame.draw.ellipse(surface,self.color,rect)

#WALL CLASS
class Wall(Sprite):
    def __init__(self,surface,pos,size,color):
        Sprite.__init__(self,surface,pos,size,color)
