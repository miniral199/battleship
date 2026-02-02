from ship import Ships
def introduction():
  print("Я делаю морской бой!")


if __name__=="__main__":
  
  introduction()
  ship=Ships()

  ship.create_ship('Galleon34',11,123)
  ship.create_ship('Galleon3',112,122)
  ship.create_ship('Galleon1',111,125)
  ship.create_ship('Galleon22',1,124)
  