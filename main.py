# version 1.0
from desk import Desk
from ship import Ships
def introduction():
  print("Я делаю морской бой!")



if __name__=="__main__":
  
  introduction()
  
  # testing creation of enemy's desk
  enemy_desk=Desk(11,13)
  enemy_desk.create_enemy()
  
  enemy_desk.print_enemy()
  
  
  # ships=Ships()
  
  
  # print(ships.ships)