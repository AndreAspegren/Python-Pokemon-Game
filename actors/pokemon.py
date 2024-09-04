class Pokemon:
    def __init__(self, name, max_hp, hp, attack, base_attack, speed, movelist, sprite):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.attack = attack
        self.base_attack = base_attack
        self.movelist = movelist
        self.speed = speed
        self.sprite = sprite

pokemon = [
    Pokemon("Pikachu", 35, 35, 55, 50, 90, ['tackle', 'recover', 'swords dance'], """
        (\__/)
        (o.o )
        (")(")
        """),
    Pokemon("Charmander", 39, 39, 52, 60, 65, ['tackle', 'swords dance'],"""
        _._.
       (o o)
       /'`'\\
      |     |
      |     |
       \\_._/
        """),
    Pokemon("Bulbasaur", 45, 45, 49, 65, 45, ['tackle', 'growl'],"""
        _._ 
       /o.o\\
      (    )
       |  |
       |  |
        """),
    Pokemon("Squirtle", 44, 44, 48, 50, 43, ['tackle', 'recover'],  """
        _._
       /o o\\
      /  -  \\
     |      |
     |      |
      \\____/
        """),
    Pokemon("Bidoof", 60, 60, 55, 60, 50, ['swords dance', 'hyper beam'], """
        /\\_/\\
       ( o.o )
        > ^ <
        """
    )
]