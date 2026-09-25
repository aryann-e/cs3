class Tusoktusok:
  name = ""
  sauce = None
  def __init__(self,name):
    self.name = name
  def dip(self,sauce):
    self.sauce = sauce
  def eat(self):
    print("I am eating", self.name, "with", self.sauce.name, "and it tastes", self.sauce.taste)

class Sauce:
  name = ""
  taste = ""
  def __init__(self,name,taste):
    self.name = name
    self.taste = taste

fishball = Tusoktusok("fishball")
hot_sauce = Sauce("hot sauce","spicy")
fishball.dip(hot_sauce)
fishball.eat()
