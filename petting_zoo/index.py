from animals import Goose
from attractions import PettingZoo


bob = Goose("Bob", "Canada goose", "watercress sandwiches")

varmint_village = PettingZoo("Varmint Village", "critters that like to dig and scurry")
varmint_village.add_animal(bob)

for animal in varmint_village.animals:
  print(animal)
