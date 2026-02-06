# version 1.2
from enemy import Enemy

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
  # testing creation of enemy's desk (almost empty,object)
  enemy=Enemy(max_x,max_y)


  # logic
  enemy.desk.set(enemy.ships.create(enemy.desk.get()))
  
  enemy.desk.print_desk()
  

  
  
  while True:
    shoot(enemy.desk.get())
    if not enemy.ships.check_ships(enemy.desk.get()):
      print("\nПобеда!")
      input("\nНажмите Enter чтобы выйти:")
      break
    enemy.desk.print_desk()
