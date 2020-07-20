from attractions import PettingZoo
from attractions import SnakePit
from attractions import Wetlands
from animals import Llama
from animals import Goat
from animals import Donkey
from animals import Duck
from animals import Horse
from animals import Copperheads
from animals import Rat_Snakes
from animals import Cobras
from animals import Vipers
from animals import Anaconda
from animals import Mallards
from animals import Goldfish
from animals import Eels
from animals import Carps
from animals import Catfish



patrick = Catfish("Patrick", "catfish", "smaller fish", 12456)


candace = Llama("Candace", "Suri Alpaca", "morning", "Llama Chow", 12345)
print(candace)

slither_inn = SnakePit("Slither Inn", "fun filled snake themed ride")

bitey = Cobras("Bitey", "cobra", "snake bites", 123456) 

fango = Copperheads("Fango", "copperhead", "snake treats", 88898)

gertie = Rat_Snakes("Gertie", "ratsnake", "rat snake treats", 99998)

slither_inn.add_animals(bitey)

slither_inn.add_animals(fango)

slither_inn.add_animals(gertie)

varmint_village = PettingZoo("Varmint Village", "a petting zoo filled with your favorite animals")

swooney = Goat("Swooney", "goat", "morning", "grass", 8985)

wilbur = Horse("Wilbur", "horse", "evening", "grass treats", 6574)


varmint_village.add_animals(swooney)

varmint_village.add_animals(wilbur)

print("last critter function", varmint_village.last_critter_added)

for animal in varmint_village.animals:
  print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}')

for animal in slither_inn.animals:
  print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}')


# bill = Catfish("Bill", "Blue catfish")

# vinny = Vipers("Vinny", "Horned desert viper")




