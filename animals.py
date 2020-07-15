from datetime import date


class Llama:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.walking = True
class Goat:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.walking = True
class Donkey:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.walking = True
class Duck:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.walking = True
class Horse:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.walking = True
class Copperheads:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.slithering = True
class Rat_Snakes:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.slithering = True
class Cobras:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.slithering = True
class Vipers:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.slithering = True
class Anaconda:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.slithering = True
class Mallards:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.swimming = True
class Goldfish:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.swimming = True
class Eels:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.swimming = True
class Carps:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.swimming = True
class Catfish:
   def __init__(self, name, species):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.swimming = True
    
candace = Llama("Candace", "Suri Alpaca")

bill = Catfish("Bill", "Blue catfish")

vinny = Vipers("Vinny", "Horned desert viper")



for prop, value in candace.__dict__.items():
    print(f'{prop}:\n{value}\n')

for prop, value in bill.__dict__.items():
    print(f'{prop}:\n{value}\n')

for prop, value in vinny.__dict__.items():
    print(f'{prop}:\n{value}\n')

