import random

class Ships:

  def __init__(self):
    self.ships_desk=None
     # generates enemy's desk with random ships position
  def create(self,desk):
    for y,value in enumerate(desk):
      for x,value_x in enumerate(value):
        # 0 - means there no ship
        # 1 - means there ship
        desk[y][x]=random.randint(0,1) 

    self.ships_desk=desk

    return desk
  
   # checks if there any ships?
  def check_ships(self,desk):
    for i in desk:
      if 1 in i: 
        return True
    return False 
  