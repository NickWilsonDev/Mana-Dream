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
    print "direction :: %s" % direction

    images = load_attack_animation(direction)

    print "# of images %d" % (len(images))
    if interval > len(images):
        print images
        interval = 1
    return images[interval]

def main():
    width = 1500
    height = 900
    blue_color = (97, 159, 182)

    character_x = 50
    character_y = 50

    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load("./music/Angel's Fear.mp3")

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Mana Dream -Secret of Mana Clone')
    intro_picture = pygame.image.load("./art/Mana Tree.jpg")
    intro_picture = pygame.transform.scale(intro_picture, (1500, 900))
    picture = intro_picture
    user_control = False
    loading_screen = True
    character_facing = "down"
    character_picture = ''

    clock = pygame.time.Clock()

    # Game initialization
    interval = 0
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

        elif keys[pygame.K_DOWN]:
            character_y = character_y + 5
            character_facing = "down"
            player_character_picture = character_picture

        elif keys[pygame.K_LEFT]:
            character_x = character_x - 5
            character_facing = "left"

        elif keys[pygame.K_RIGHT]:
            character_x = character_x + 5
            character_facing = "right"

        elif keys[pygame.K_SPACE]:
            #global interval
            character_attack = True
            #player_character_picture = attack_animation(character_facing, character_x, character_y, screen, interval)
            #if interval > 8:
            #    interval = 0
            #else:
            #    interval += 1
            
        
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
        if user_control:
            screen.blit(player_character_picture, (character_x, character_y))
        if character_attack:
            interval = (interval + 1) % 10
            print "interval %d " % interval
            screen.blit(attack_animation(character_facing, interval), (character_x, character_y))
            if interval >= 9:
                interval = 0
                character_attack = False
        # Game display


        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
