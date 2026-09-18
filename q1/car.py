class Car:
  def __init__(self,brand,model,battery=35):
    self.brand = brand
    self.model = model
    self.battery = battery
  def go(self,distance):
    self.battery -= distance / 20
    print("You traveled",distance)
    print("You have",self.battery,"wH left")
  def charge(self,wH):
    battery += wH
    print("You recharged with", wH,"wH")

car = Car("Honda", "Civic")
while car.battery > 0:
  act = input("What do we do (g or c)?: ")
  if act == "g":
    distance = int(input("How far?: ")
    self.go(distance)
  elif act == "c":
    wH = int(input("How much?: ")
    self.charge(wH)
    
