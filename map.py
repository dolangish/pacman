import pygame
import sprites
import colors
import math

class Map(object):
    def __init__(self,surface,size):
        self.cells={}
        self.num_rows=size[1]
        self.num_columns=size[0]
        self.surface=surface
        cell_width=math.floor(surface.get_width()/size[0])
        cell_height=math.floor(surface.get_height()/size[1])
        self.cell_size=[cell_width,cell_height]
        for col in range(0,size[0]):
            for row in range(0,size[1]):
                rect=pygame.Rect(cell_width*col,cell_height*row,cell_width,cell_height)
                self.cells[(row*size[0])+col]=Cell(rect)
    
    def get_cell_size(self):
        return self.cell_size

    def get_num_columns(self):
        return self.num_columns
        
    def get_num_rows(self):
        return self.num_rows
        
    def check_cell(self,col,row,sprite):
        curr_cell=self.cells[(row*self.get_num_columns())+col]
        ret=False
        if(curr_cell.contains(sprite)):
            ret=True
        return ret
        
    def set_walls(self,data,color):
        ret=[]
        i=0
        for wall in data:
            if wall:
                try:
                    cell=self.cells[i]
                except KeyError:
                    print("failed on "+str(i))
                if(cell):
                    rect=cell.get_rect()
                    ret.append(sprites.Wall(self.surface,rect.topleft,rect.size,colors.BLUE))
            i=i+1
        return ret
    
    def get_start_pos(self):
        start_cell=self.cells[self.pac_start]
        ret=start_cell.get_rect().topleft
        return ret
        
    def get_map_data(self):
        ret=[]
        map_file=open("default_map.txt","r")
        while True:
            char=map_file.read(1)
            if not char:
                break;
            elif char=="W":
                ret.append(True)
            elif char=="N":
                ret.append(False)
            elif char=="S":
                ret.append(False)
                self.pac_start=len(ret)-1
        return ret
        
        
        
class Cell(object):
    def __init__(self,rect):
        self.rect=rect
    
    def get_rect(self):
        return self.rect
        
    def contains(self,sprite):
        ret=False
        if self.rect.colliderect(sprite.get_rect()):
            ret=True
        return ret