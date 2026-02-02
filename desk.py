import random

class Desk:
  def __init__(self,size_x,size_y):
    self.x=size_x
    self.y=size_y
    # количество клеток
    self.cells=size_x*size_y
    self.enemy_field=[[""]*size_x]*size_y
    # self.enemy_field=[
    #   ['','',''],['','','']
    # ]

  # generates enemy's desk with random ships position
  def create_enemy(self):
    for y,value in enumerate(self.enemy_field):
      for x,value_x in enumerate(value):
        self.enemy_field[y][x]=random.randint(0,1)


  def print_enemy(self):
    for a,b in enumerate(self.enemy_field):
      print(a,b)