import random

class Desk:
  def __init__(self,size_x,size_y):
    self.x=size_x
    self.y=size_y
    # количество клеток
    self.cells=size_x*size_y
    self.enemy_field=[[""]*size_x for _ in range(size_y)]
    # self.enemy_field=[
    #   ['','',''],['','','']
    # ]

  # generates enemy's desk with random ships position
  def create_enemy(self):
    for y,value in enumerate(self.enemy_field):
      for x,value_x in enumerate(value):
        # 0 - means there no ship
        # 1 - means there ship
        self.enemy_field[y][x]=random.randint(0,1)



  def print_enemy(self):
    for a,b in enumerate(self.enemy_field):
      print(b)
    # print(self.enemy_field[0][1]) #x=0 y=1
  
  # checks if there any ships?
  def check_ships(self):
    for i in self.enemy_field:
      if 1 in i: 
        return True
    return False
  