import random

class Desk:
  def __init__(self,size_x,size_y):
    self.x=size_x
    self.y=size_y
    # количество клеток
    self.cells=size_x*size_y
    self.enemy_field=[[""]*size_x for _ in range(size_y)]

  # generates enemy's desk with random ships position
  def create_enemy(self):
    for y,value in enumerate(self.enemy_field):
      for x,value_x in enumerate(value):
        # 0 - means there no ship
        # 1 - means there ship
        self.enemy_field[y][x]=random.randint(0,1)



  def print_enemy(self):
    for a,b in reversed(list(enumerate(self.enemy_field))):
  
      print(f"{a}| ",end=" ")
      
      for x in b:
        
        print(x,end=" ")
      
      print()
      if a==0:
        print(self.x*" ",end="")
        for i in range(len(b)):
          print("———",end="")
          
        print()
        print((self.x+1)*" ",end="")
        for num in range(len(b)):
          
          print(num,end=" ")


    # print("—"*5)
    print("\nY/X")
  
  # checks if there any ships?
  def check_ships(self):
    for i in self.enemy_field:
      if 1 in i: 
        return True
    return False
  