class Desk:

  def __init__(self,size_x,size_y):
    self.x=size_x
    self.y=size_y
    # количество клеток
    self.cells=size_x*size_y
    self.desk=[[""]*size_x for _ in range(size_y)]
    
  def get(self):
    return self.desk
  
  def set(self,desk):
    self.desk=desk
    
  
  def print_desk(self):
    for a,b in reversed(list(enumerate(self.desk))):
  
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

    print("\nY/X")
  