from datetime import date

class Animal:
  def __init__(self, name, species, food):
    self.name = name
    self.species = species
    self.food = food
    self.__chip_number = 0
    self.date_added = date.today()
  
  def feed(self):
    print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

  @property
  def chip_number(self):
    return self.__chip_number

  @chip_number.setter
  def chip_number(self, num):
    pass



















