from .sprite import *
import colors

class Wall(Sprite):
    def __init__(self,pos,size):
        Sprite.__init__(self,pos,size,colors.BLUE)
