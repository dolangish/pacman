import pygame
import sprites
import directions

##############################################################
#this module is home to our static collision detection methods
##############################################################
def check_collisions(sprite1,group):
    ret=[]
               
    hit_list=pygame.sprite.spritecollide(sprite1,group,False)
    for sprite2 in hit_list:
        ret.append((sprite1,sprite2))
            
    return ret
        
def check_out_of_bounds(sprite,surface):
    ret=[]
    sx=sprite.get_x()
    sy=sprite.get_y()
    sw=sprite.get_width()
    sh=sprite.get_height()
    surface_width=surface.get_rect().width
    surface_height=surface.get_rect().height
    if (sx<-sw/2) or (sy<-sh/2) or (sx+sw>surface_width+(sw/2)) or (sy+sh>surface_height+(sh/2)):
        ret.append((sprite,surface))
    return ret

def resolve_collisions(collision_list):
    for collision in collision_list:
        sprite1=collision[0]
        sprite2=collision[1]
        #if we are checking pacman
        if isinstance(sprite1,sprites.Pacman):
            #against a wall
            if isinstance(sprite2,sprites.Wall):
                s1_dir=sprite1.get_direction()
                if s1_dir==directions.UP:
                    sprite1.resolve_collision([0,-1],sprite2)
                elif s1_dir==directions.DOWN:
                    sprite1.resolve_collision([0,1],sprite2)
                elif s1_dir==directions.LEFT:
                    sprite1.resolve_collision([-1,0],sprite2)
                elif s1_dir==directions.RIGHT:
                    sprite1.resolve_collision([1,0],sprite2)
            #against a boarder
            elif isinstance(sprite2,pygame.Surface):
                if sprite1.dir == directions.LEFT:
                    sprite1.set_x(sprite2.get_width()-(sprite1.get_width()/2))
                if sprite1.dir == directions.UP:
                    sprite1.set_y(sprite2.get_height()-(sprite1.get_height()/2))
                if sprite1.dir == directions.RIGHT:
                    sprite1.set_x(-(sprite1.get_width()/2))
                if sprite1.dir == directions.DOWN:
                    sprite1.set_y(-(sprite1.get_height()/2))
                
		