# version 1.0
from desk import Desk
# from ship import Ships
def introduction(x,y):
  print("Я делаю морской бой!")
  print("На данный момент это игра в которой возможно только победить (проиграть невозможно)!")
  print("\nType coordinates to shoot!")
  print(f"X can only be in range[0..{x-1}(included)]")
  print(f"Y can only be in range[0..{y-1}(included)]\n")

def shoot(desk):
  print("\nTo shoot:")
  try:
    x=int(input("Type x: "))
    y=int(input("Type y: "))
    
    print()
    
    if desk[y][x] == 1:
      print("Есть попадание!")
      desk[y][x]=0
    
    else:
      print("Мимо!")
      
  except IndexError:
    print("Что гонишь что ли? Заново давай!")
  except ValueError:
    print("А ну ка давай только числа вводи!")


if __name__=="__main__":

  # field size example 3x5
  max_x=3
  max_y=5
  
  introduction(max_x,max_y)
  # testing creation of enemy's desk
  enemy_desk=Desk(max_x,max_y)
  enemy_desk.create_enemy()
  
  enemy_desk.print_enemy()
  
  
  while True:
    shoot(enemy_desk.enemy_field)
    if not enemy_desk.check_ships():
      print("\nПобеда!")
      break
    enemy_desk.print_enemy()


  # ships=Ships()
  # print(ships.ships)