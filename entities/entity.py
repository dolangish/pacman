import pygame

class Entity(object):
    def __init__(self,pos,size,color):
        self.color=color
        self.rect=pygame.Rect(pos[0],pos[1],size[0],size[1])

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
    
    def update(self):
        pass      

    def draw(self, surface):
        pygame.draw.rect(surface,self.color,self.rect)
