class Ships:
  
  def __init__(self):
    self.ships=[]
  
  def create_ship(self, name, x, y):
    
    self.ships={
      "name":name,
      "x-pos":x,
      "y-pos":y
      }
      
  
  
  
  # def print_coordinates(self):
  #   print(f"Текущее положение Корабля по имени '{self.name}': ")
  #   print(f"По оси x: {self.x}")
  #   print(f"По оси y: {self.y}")