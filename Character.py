#Character.py
"""This class will model the player character in the Mana-Dream game."""

class Character(object):

    def __init__(self):
        self.name = "Knight"
        self.level = 1
        self.max_hp = 20
        self.current_hp = self.max_hp
        self.xp = 0
        self.xp_to_next_level = ((self.level + 1) * 10) - self.xp
        self.max_mp = 10
        self.current_mp = self.max_mp
        self.attack = 5
        self.defense = 5
        self.magic_list = ['undine', 'salamando', 'shade', 'sylphid']
        self.magic_dict = {
            'undine': 'water',
            'salamando': 'fire',
            'shade': 'darkness',
            'sylphid': 'lightning'
        }

        self.character_x = 100
        self.character_y = 100
        self.current_direction = 'down'
        # may go ahead and load up animation images

    def level_up(self):
        self.level += 1
        self.max_hp = self.max_hp + 5 + self.level
        self.current_hp = self.max_hp
        self.max_mp = self.max_mp + 5 + self.level
        self.current_mp = self.max_mp
        self.attack += self.level
        #probably not done

    def take_damage(self):
        pass
