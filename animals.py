from datetime import date


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
    
candace = Llama("Candace", "Suri Alpaca", "morning", "Llama Chow")
print(candace)

# bill = Catfish("Bill", "Blue catfish")

# vinny = Vipers("Vinny", "Horned desert viper")




