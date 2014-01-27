from directions import *
from .collision import *

class Wall_collision(Collision):
	def __init__(self,sprite1,wall=0):
		Collision.__init__(self,sprite1,wall)
		
	def resolve(self):
		s1_dir=self.sprite1.get_direction()
		if s1_dir==UP:
			self.sprite1.move_down(1)
		elif s1_dir==DOWN:
			self.sprite1.move_up(1)
		elif s1_dir==LEFT:
			self.sprite1.move_right(1)
		elif s1_dir==RIGHT:
			self.sprite1.move_left(1)
		