# SecretOfManaClone.py
import pygame

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275


def attack_animation(direction):
    pass


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

    clock = pygame.time.Clock()

    # Game initialization

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

        elif keys[pygame.K_LEFT]:
            character_x = character_x - 5
            character_facing = "left"

        elif keys[pygame.K_RIGHT]:
            character_x = character_x + 5
            character_facing = "right"

        elif keys[pygame.K_SPACE]:
            attack_animation(character_facing)

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
                player_character_picture = pygame.image.load("./art/DarkKnight.png").convert_alpha()

            
            if event.type == pygame.QUIT:
                stop_game = True

        # Game logic

        # Draw background
        screen.blit(picture, (0, 0))
        if user_control:
            screen.blit(player_character_picture, (character_x, character_y))
            pass
        # Game display


        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
