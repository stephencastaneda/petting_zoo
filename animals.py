from datetime import date

class Animal:
  def __init__(self, name, species, food, chip_num):
    self.name = name
    self.species = species
    self.food = food
    self.__chi_number = chip_num
    self.date_added = date.today()
  
  def feed(self):
    print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

  @property
  def chip_number(self):
    return self.__chip_number

  @chip_number.setter
  def chip_number(self, num):
    pass


class Llama(Animal):
  def __init__(self, name, species, shift, food, chip_num):
    super().__init__(name, species, food, chip_num)
    self.shift = shift
    self.walking = True

  def feed(self):
    print(f'on {date.today()}, {self.name} had "Rockytop" sung to it so it would eat its {self.food}')

class Goat(Animal):
  def __init__(self, name, species, shift, food, chip_num):
    super().__init__(name, species, food, chip_num)
    self.shift = shift
    self.walking = True

class Donkey(Animal):
  def __init__(self, name, species, shift, food, chip_num):
    super().__init__(name, species, food, chip_num)
    self.shift = shift
    self.walking = True

class Duck(Animal):
  def __init__(self, name, species, shift, food, chip_num):
    super().__init__(name, species, food, chip_num)
    self.shift = shift
    self.walking = True

  def feed(self):
    print(f'on {date.today()}, {self.name} we read its favorite rubber duck kids book to eat so it would eat its {self.food}')

class Horse(Animal):
  def __init__(self, name, species, shift, food, chip_num):
    super().__init__(name, species, food, chip_num)
    self.shift = shift
    self.walking = True

  def feed(self):
    print(f'on {date.today()}, {self.name} had "Old Town Road" sung to it so it would eat its {self.food}')

class Copperheads(Animal):
 def __init__(self, name, species, food, chip_num):
    super().__init__(name, species, food, chip_num)
    self.slithering = True

class Rat_Snakes(Animal):
   def __init__(self, name, species, food, chip_num):
    super().__init__(name, species, food, chip_num)
    self.slithering = True

class Cobras(Animal):
   def __init__(self, name, species, food, chip_num):
    super().__init__(name, species, food, chip_num)
    self.slithering = True

class Vipers(Animal):
   def __init__(self, name, species, food, chip_num):
    super().__init__(name, species, food, chip_num)
    self.slithering = True

class Anaconda(Animal):
   def __init__(self, name, species, food, chip_num):
    super().__init__(name, species, food, chip_num)
    self.slithering = True

class Mallards(Animal):
  def __init__(self, name, species, food, chip_num):
    super().__init__(name, species, food, chip_num)
    self.swimming = True

  def feed(self):
    print(f'on {date.today()}, {self.name} had Finding Nemo played for it so it would eat its {self.food}')

class Goldfish(Animal):
  def __init__(self, name, species, food, chip_num):
    super().__init__(name, species, food, chip_num)
    self.swimming = True

class Eels(Animal):
  def __init__(self, name, species, food, chip_num):
    super().__init__(name, species, food, chip_num)
    self.swimming = True

class Carps(Animal):
  def __init__(self, name, species, food, chip_num):
    super().__init__(name, species, food, chip_num)
    self.swimming = True

class Catfish(Animal):
  def __init__(self, name, species, food, chip_num):
    super().__init__(name, species, food, chip_num)
    self.swimming = True
  
