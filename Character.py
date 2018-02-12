#Character.py
"""This class will model the player character in the Mana-Dream game."""

import pygame

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


    def display_menu(self, rotation):
        print "rotation:: %d" % rotation
        images = []
        for element in self.magic_list:
            images.append(pygame.image.load("./art/%s.png" % element).convert_alpha())

        """ quick rotation of items if needed """
        return images[-rotation % len(images):] + images[:-rotation % len(images)]


    def load_magic_images(self, magic_type):
        images = []
        for i in range(1, 14):
            images.append(pygame.image.load("./art/%s%d.png" % (magic_type, i)).convert_alpha())
        return images

    def magic_animation(self, magic_type, interval):
        images = []
        magic = self.magic_dict[magic_type]
        images = self.load_magic_images(magic)
        return images[interval]

