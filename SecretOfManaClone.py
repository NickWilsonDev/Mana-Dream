# SecretOfManaClone.py
import pygame
import time
from itertools import cycle
import math

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275


magic_list = ['undine', 'salamando', 'shade', 'sylphid']
magic_dict = {
    'undine': 'water',
    'salamando': 'fire',
    'shade': 'darkness',
    'sylphid': 'lightning'
}

def load_attack_images(direction):
    images = []
    for i in range(1, 11):
        images.append(pygame.image.load("./art/dk_%s_attack%d.png" % (direction, i)).convert_alpha())
    return images

def attack_animation(direction, interval):
    """Function is called to help ensure the correct set of sprite images is 
       drawn.
       Params
            direction - last direction the player character moved
            interval  - will be index in list of attack animation images
                        so the correct image will be chosen
            Returns   - a particular image from the list of attack images
    """
    images = load_attack_images(direction)
    return images[interval]

def load_magic_images(magic_type):
    images = []
    for i in range(1, 14):
        images.append(pygame.image.load("./art/%s%d.png" % (magic_type, i)).convert_alpha())
    return images

def magic_animation(magic_type, interval):
    images = []
    magic = magic_dict[magic_type]
    images = load_magic_images(magic)
    return images[interval]

def load_walk_images(direction):
    images = []
    for i in range(1, 5):
        images.append(pygame.image.load("./art/dk_%s_walk%d.png" % (direction, i)).convert_alpha())
    return images

def walk_animation(direction, interval):
    images = load_walk_images(direction)
    return images[interval]

def get_standing_direction(direction):
    image = pygame.image.load("./art/dk_%s.png" % direction).convert_alpha()
    return image

def display_menu(rotation):
    print "rotation:: %d" % rotation
    # list = cycle(images) to cycle through circular list
    images = []
    #magic_list = ['undine', 'shade', 'sylphid', 'salamando']
    for element in magic_list:
        images.append(pygame.image.load("./art/%s.png" % element).convert_alpha())

    """ quick rotation of items if needed """
    return images[-rotation % len(images):] + images[:-rotation % len(images)]

def main():
    screen_width = 1500
    screen_height = 900

    character_x = 50
    character_y = 50

    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load("./music/Angel's Fear.mp3")
    
    #screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Mana Dream -Secret of Mana Clone')
    intro_picture = pygame.image.load("./art/Mana Tree.jpg")
    intro_picture = pygame.transform.scale(intro_picture, (1500, 900))
    picture = intro_picture
    user_control = False
    loading_screen = True
    character_facing = "down"
    character_picture = ''

    clock = pygame.time.Clock()
    menu_select = ''
    menu_index = 0
    menu_rotating_right = False
    menu_item_position_x = 0
    menu_item_position_y = 0
    start_frame = time.time()
    background_x = 0
    background_y = 0
    # Game initialization
    interval = 0
    character_walk = False
    character_attack = False
    item_menu = False
    pygame.mixer.music.play(-1, 0.0)
    stop_game = False
    while not stop_game:

        keys = pygame.key.get_pressed()
        
            # two keys pressed at the same time
        if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            character_y = character_y - 3
            character_x = character_x - 3
            
        elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
            character_y = character_y - 3
            character_x = character_x + 3

        elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            character_y = character_y + 3
            character_x = character_x - 3

        elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
            character_y = character_y + 3
            character_x = character_x + 3

        elif keys[pygame.K_UP] and not item_menu:
            character_y = character_y - 5
            character_facing = "up"
            character_walk = True

        elif keys[pygame.K_DOWN] and not item_menu:
            character_y = character_y + 5
            character_facing = "down"
            character_walk = True

        elif keys[pygame.K_LEFT] and not item_menu:
            character_x = character_x - 5
            character_facing = "left"
            character_walk = True

        elif keys[pygame.K_RIGHT] and not item_menu:
            character_x = character_x + 5
            character_facing = "right"
            character_walk = True

        elif keys[pygame.K_RIGHT] and item_menu:
            menu_rotating_right = True #not menu_rotating_right

        elif keys[pygame.K_SPACE] and not item_menu:
            character_attack = True

        for event in pygame.event.get():

            # Event handling
            if event.type == pygame.MOUSEBUTTONDOWN and loading_screen:
                #sound.play(-1, 0.0)
                pygame.mixer.music.stop()
                map_picture = pygame.image.load("./art/plains_map.png")
                picture = map_picture
                picture = pygame.transform.scale(picture, (5000, 5000))
                user_control = True
                pygame.mixer.music.load("./music/Prophecy.mp3")
                pygame.mixer.music.play(-1, 0.0)
                player_character_picture = pygame.image.load("./art/dk_down.png").convert_alpha()
                character_picture = player_character_picture

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    menu_index = 0
                    item_menu = not item_menu

                elif event.key == pygame.K_RIGHT and item_menu:
                    menu_index = (menu_index + 1) % 4 # need this to be size of menu
                    #while event.key != pygame.KEYUP:
                    menu_rotating_right = True
                    #menu_rotating_right = False
                    print "menu moved %d" % menu_index
                elif event.key == pygame.K_LEFT and item_menu:
                    menu_index = (menu_index - 1) % 4
                    menu_rotating_left = True
                elif event.key == pygame.K_SPACE and item_menu:
                    menu_select = True
                    print menu_index
                elif event.key == pygame.K_ESCAPE:
                    stop_game = True

            if event.type == pygame.QUIT:
                stop_game = True

        # Game logic

        # Draw background
        screen.blit(picture, (background_x, background_y))
        if user_control and not character_walk and not character_attack:
            screen.blit(get_standing_direction(character_facing), (character_x, character_y))
        if character_attack:
            noi = 10
            frames_per_sec = 15
            interval = int((time.time() - start_frame) * frames_per_sec % noi)
            screen.blit(attack_animation(character_facing, interval), (character_x, character_y))
            if interval >= 9:
                interval = 0
                character_attack = False

        if character_walk:
            #print "Character(x, y) (%d, %d)" % (character_x, character_y)
            noi = 4
            frames_per_sec = 10
            interval = int((time.time() - start_frame) * frames_per_sec % noi)
            screen.blit(walk_animation(character_facing, interval), (character_x, character_y))
            if interval >= 3:
                interval = 0
                character_walk = False
                screen.blit(get_standing_direction(character_facing), (character_x, character_y))
        if item_menu:
            images = display_menu(menu_index)
            print images
            # maybe instead of just displaying them we will set their inital positions
            if not menu_rotating_right:
                screen.blit(images[0], (character_x, character_y - 150))
                screen.blit(images[1], (character_x + 150, character_y))
                screen.blit(images[2], (character_x, character_y + 150))
                screen.blit(images[3], (character_x - 150, character_y))
            
            if  menu_select:
                #print start_frame
                noi = 13
                frames_per_sec = 5
                interval = int((time.time() - start_frame) * frames_per_sec % noi)
                #may change character coordinates to target coordinates later
                print magic_list
                print magic_list[menu_index]
                screen.blit(magic_animation(magic_list[menu_index], interval), (character_x, character_y))
                if interval >= 12:
                    interval = 0
                    menu_select = False
                    item_menu = False

            if menu_rotating_right:
                # increment by 15 degrees?
                two_pi = 2 * math.pi
                fifteen_degrees = math.pi / 12
                i = 1
                while i < 7: # 6 is good for 90 degrees, with 4 menu options
                    temp = two_pi - (i * (fifteen_degrees))
                    temp2 = two_pi + (i * (fifteen_degrees))
                    temp3 = two_pi - (i * fifteen_degrees)
                    menu_item_position_x = character_x + int(math.cos(temp) * 150)
                    menu_item_position_y = character_y + int(math.sin(temp) * 150)
                    
                    menu_item2_position_x = character_x + int(math.cos(temp2) * 150)
                    menu_item2_position_y = character_y + int(math.sin(temp2) * 150)

                    menu_item3_position_x = character_x - int(math.cos(temp3) * 150)
                    menu_item3_position_y = character_y - int(math.sin(temp3) * 150)

                    menu_item0_position_x = character_x - int(math.cos(temp) * 150)
                    menu_item0_position_y = character_y + int(math.sin(temp) * 150)
                   # print "item position x %d" % menu_item_position_x
                    
                    screen.blit(images[1], (menu_item_position_x, menu_item_position_y))
                    screen.blit(images[2], (menu_item2_position_x, menu_item2_position_y))
                    
                    screen.blit(images[3], (menu_item3_position_x, menu_item3_position_y))
                    screen.blit(images[0], (menu_item0_position_x, menu_item0_position_y))
                    i += 1
                menu_rotating_right = False

        # Game display background world map ect
        if character_x >= 1300:
            background_x = background_x - character_x
            character_x = 50
        if character_y >= 800:
            background_y = background_y - character_y
            character_y = 50

        if character_x < 10:
            background_x = background_x + 1400
            character_x = 50
        if character_y < 10:
            background_y = background_y + 900
            character_y = 50

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
