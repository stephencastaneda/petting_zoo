from datetime import date
from attractions import SnakePit
from attractions import PettingZoo


class Llama:
  def __init__(self, name, species, shift, food):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.walking = True
    self.shift = shift
    self.food = food

  def feed(self):
    print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
  
  def __str__(self):
    return f"{self.name} is a {self.species}"
class Goat:
  def __init__(self, name, species, shift, food):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.walking = True
    self.shift = shift
    self.food = food
  def feed(self):
    print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
  def __str__(self):
    return f"{self.name} is a {self.species}"
class Donkey:
  def __init__(self, name, species, shift, food):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.walking = True
    self.shift = shift
    self.food = food
  def feed(self):
    print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
  def __str__(self):
    return f"{self.name} is a {self.species}"
class Duck:
  def __init__(self, name, species, shift, food):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.walking = True
    self.shift = shift
    self.food = food
  def feed(self):
    print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
  def __str__(self):
    return f"{self.name} is a {self.species}"
class Horse:
  def __init__(self, name, species, shift, food):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.walking = True
    self.shift = shift
    self.food = food
  def feed(self):
    print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
  def __str__(self):
    return f"{self.name} is a {self.species}"
class Copperheads:
  def __init__(self, name, species, food):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.slithering = True
    self.food = food
  def feed(self):
    print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
  def __str__(self):
    return f"{self.name} is a {self.species}"
class Rat_Snakes:
  def __init__(self, name, species, food):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.slithering = True
    self.food = food
  def feed(self):
    print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
  def __str__(self):
    return f"{self.name} is a {self.species}"
class Cobras:
  def __init__(self, name, species, food):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.slithering = True
    self.food = food
  def feed(self):
    print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
  def __str__(self):
    return f"{self.name} is a {self.species}"
class Vipers:
  def __init__(self, name, species, food):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.slithering = True
    self.food = food
  def feed(self):
    print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
  def __str__(self):
    return f"{self.name} is a {self.species}"
class Anaconda:
  def __init__(self, name, species, food):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.slithering = True
    self.food = food
  def feed(self):
    print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
  def __str__(self):
    return f"{self.name} is a {self.species}"
class Mallards:
  def __init__(self, name, species, food):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.swimming = True
    self.food = food
  def feed(self):
    print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
  def __str__(self):
    return f"{self.name} is a {self.species}"
class Goldfish:
  def __init__(self, name, species, food):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.swimming = True
    self.food = food
  def feed(self):
    print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
  def __str__(self):
    return f"{self.name} is a {self.species}"
class Eels:
  def __init__(self, name, species, food):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.swimming = True
    self.food = food
  def feed(self):
    print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
  def __str__(self):
    return f"{self.name} is a {self.species}"
class Carps:
  def __init__(self, name, species, food):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.swimming = True
    self.food = food
  def feed(self):
    print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
  def __str__(self):
    return f"{self.name} is a {self.species}"
class Catfish:
  def __init__(self, name, species, food, chip_num):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.swimming = True
    self.food = food
    self.__chip_number = chip_num
  def feed(self):
    print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
  def __str__(self):
    return f"{self.name} is a {self.species}"

  @property 
  def chip_num(self):
    return self.__chip_number

  @chip_num.setter
  def chip_num(self, number):
      pass 
  
patrick = Catfish("Patrick", "catfish", "smaller fish", 12456)


candace = Llama("Candace", "Suri Alpaca", "morning", "Llama Chow")
print(candace)

slither_inn = SnakePit("Slither Inn", "fun filled snake themed ride")

bitey = Cobras("Bitey", "cobra", "snake bites") 

fango = Copperheads("Fango", "copperhead", "snake treats")

gertie = Rat_Snakes("Gertie", "ratsnake", "rat snake treats")

slither_inn.add_animals(bitey)

slither_inn.add_animals(fango)

slither_inn.add_animals(gertie)

varmint_village = PettingZoo("Varmint Village", "a petting zoo filled with your favorite animals")

swooney = Goat("Swooney", "goat", "morning", "grass")

wilbur = Horse("Wilbur", "horse", "evening", "grass treats")

linda = Llama("Linda", "llama", "afternoon", "tacos")

varmint_village.add_animals(swooney)

varmint_village.add_animals(wilbur)

varmint_village.add_animals(linda)

print("last critter function", varmint_village.last_critter_added)

for animal in varmint_village.animals:
  print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}')

for animal in slither_inn.animals:
  print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}')



# bill = Catfish("Bill", "Blue catfish")

# vinny = Vipers("Vinny", "Horned desert viper")




