from .pokemon import *

class Trainer:
    def __init__(self, name, line, roster, potions, pokeballs):
        self.name = name
        self.line = line
        self.roster = roster
        self.potions = potions
        self.pokeballs = pokeballs


trainers = [
    Trainer(input('Hva vil du Hete?'), 'Lets do this!', [], 3, 0),
    Trainer('Red', '...', [pokemon[1], pokemon[2], pokemon[3]], 0, 0)
]