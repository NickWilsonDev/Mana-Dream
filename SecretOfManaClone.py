# SecretOfManaClone.py
import pygame
import time

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275


def load_attack_animation(direction):
    images = []
    if direction == "down":
        images.append(pygame.image.load("./art/dk_down_attack1.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_down_attack2.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_down_attack3.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_down_attack4.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_down_attack5.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_down_attack6.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_down_attack7.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_down_attack8.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_down_attack9.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_down_attack10.png").convert_alpha())

    elif direction == "up":
        images.append(pygame.image.load("./art/dk_up_attack1.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_up_attack2.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_up_attack3.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_up_attack4.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_up_attack5.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_up_attack6.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_up_attack7.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_up_attack8.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_up_attack9.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_up_attack10.png").convert_alpha())

    elif direction == "left":
        images.append(pygame.image.load("./art/dk_left_attack1.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_left_attack2.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_left_attack3.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_left_attack4.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_left_attack5.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_left_attack6.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_left_attack7.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_left_attack8.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_left_attack9.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_left_attack10.png").convert_alpha())

    elif direction == "right":
        images.append(pygame.image.load("./art/dk_right_attack1.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_right_attack2.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_right_attack3.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_right_attack4.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_right_attack5.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_right_attack6.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_right_attack7.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_right_attack8.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_right_attack9.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_right_attack10.png").convert_alpha())
    return images

def attack_animation(direction, interval):
    images = load_attack_animation(direction)
    #if interval > len(images):
    #    print images
    #    interval = 1
    return images[interval]

def load_walk_animation(direction):
    images = []
    if direction == "up":
        images.append(pygame.image.load("./art/dk_up_walk1.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_up_walk2.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_up_walk3.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_up_walk4.png").convert_alpha())
    
    elif direction == "down":
        images.append(pygame.image.load("./art/dk_down_walk1.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_down_walk2.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_down_walk3.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_down_walk4.png").convert_alpha())

    elif direction == "right":
        images.append(pygame.image.load("./art/dk_right_walk1.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_right_walk2.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_right_walk3.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_right_walk4.png").convert_alpha())

    elif direction == "left":
        images.append(pygame.image.load("./art/dk_left_walk1.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_left_walk2.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_left_walk3.png").convert_alpha())
        images.append(pygame.image.load("./art/dk_left_walk4.png").convert_alpha())
    return images

def walk_animation(direction, interval):
    images = load_walk_animation(direction)
    #if interval > len(images):
    #    interval = 1

    return images[interval]

def get_standing_direction(direction):
    if direction == "up":
        image = pygame.image.load("./art/dk_up.png").convert_alpha()
    elif direction == "down":
        image = pygame.image.load("./art/dk_down.png").convert_alpha()
    elif direction == "right":
        image = pygame.image.load("./art/dk_right.png").convert_alpha()
    elif direction == "left":
        image = pygame.image.load("./art/dk_left.png").convert_alpha()
    return image

def main():
    screen_width = 1500
    screen_height = 900
    blue_color = (97, 159, 182)

    character_x = 50
    character_y = 50

    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load("./music/Angel's Fear.mp3")

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

    start_frame = time.time()
    # Game initialization
    interval = 0
    character_facing = "down"
    character_walk = False
    character_attack = False
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

        elif keys[pygame.K_UP]:
            character_y = character_y - 5
            character_facing = "up"
            character_walk = True

        elif keys[pygame.K_DOWN]:
            character_y = character_y + 5
            character_facing = "down"
            character_walk = True
            #player_character_picture = character_picture

        elif keys[pygame.K_LEFT]:
            character_x = character_x - 5
            character_facing = "left"
            character_walk = True

        elif keys[pygame.K_RIGHT]:
            character_x = character_x + 5
            character_facing = "right"
            character_walk = True

        elif keys[pygame.K_SPACE]:
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
            
            if event.type == pygame.QUIT:
                stop_game = True

        # Game logic

        # Draw background
        screen.blit(picture, (0, 0))
        #screen.blit(picture, (-200, -300))
        if user_control:
            #screen.blit(player_character_picture, (character_x, character_y))
            screen.blit(get_standing_direction(character_facing), (character_x, character_y))
        if character_attack:
            #interval = (interval + 1) % 10
            #print "interval %d " % interval
            noi = 10
            frames_per_sec = 15
            interval = int((time.time() - start_frame) * frames_per_sec % noi)
            screen.blit(attack_animation(character_facing, interval), (character_x, character_y))
            if interval >= 9:
                interval = 0
                character_attack = False

        if character_walk:
            print "Character(x, y) (%d, %d)" % (character_x, character_y)
            
            #interval = (interval + 1) % 4
            noi = 4
            frames_per_sec = 10
            interval = int((time.time() - start_frame) * frames_per_sec % noi)
            screen.blit(walk_animation(character_facing, interval), (character_x, character_y))
            if interval >= 3:
                interval = 0
                character_walk = False
                screen.blit(get_standing_direction(character_facing), (character_x, character_y))
        # Game display
        if character_x >= 1400:
            character_x = 50
            screen.blit(picture, (character_x - screen_width, screen_height))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
