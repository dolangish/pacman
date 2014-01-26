import pygame

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
