class Mallards(Animal):
  def __init__(self, name, species, food, chip_num):
    super().__init__(name, species, food, chip_num)
    self.swimming = True

  def feed(self):
    print(f'on {date.today()}, {self.name} had Finding Nemo played for it so it would eat its {self.food}')
