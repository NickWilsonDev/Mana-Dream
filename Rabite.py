#Rabite.py
""" Class models a rabite animal
"""

class Rabite(object, x, y):
    def __init__(self):
        self.name = "rabite"
        self.max_hp = 5
        self.current_hp = 5
        self.attack = 2
        self.defense = 2

        self.position_x = x
        self.position_y = y

    def take_damage(self):
        pass

# animation methods below
