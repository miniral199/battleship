# version 1.0
from desk import Desk
# from ship import Ships
def introduction():
  print("Я делаю морской бой!")
  print("На данный момент это игра в которой невозможно проиграть! АХАХ")

def shoot(desk):
  print("Type coordinates to shoot!")
  try:
    x=int(input("Type x:"))
    y=int(input("Type y:"))
  
    if desk[x][y] == 1:
      print("Есть попадание!")
      desk[x][y]=0
    
    else:
      print("Мимо!")
      
  except IndexError:
    print("Что гонишь что ли? Заново давай!")


if __name__=="__main__":
  
  introduction()
  
  # testing creation of enemy's desk
  enemy_desk=Desk(3,3)
  enemy_desk.create_enemy()
  
  enemy_desk.print_enemy()
  
  
  while True:
    shoot(enemy_desk.enemy_field)
    if not enemy_desk.check_ships():
      print("Вы победили!")
      break
    enemy_desk.print_enemy()


  # ships=Ships()
  # print(ships.ships)