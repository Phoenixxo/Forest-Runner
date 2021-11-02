"""A side scroller game made by <3Phoenix#9996 on discord. A small project for experience and fun!"""

# Imports
import sys
import pygame
from pygame.locals import Rect
from player import Player
from enemy import Enemy

# Contstants
SIZE = (1280, 720)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
BROWN = (90, 80, 65)
TARGET_FPS = 60.0

# Creating background

bkgnd = pygame.image.load("D:\\Projects\\SideScroller\\background.jpg")
BACKGROUND = bkgnd.get_rect()

# Sprites

bat_f = pygame.image.load("D:\\Projects\\SideScroller\\batF.png")
bat_r = pygame.image.load("D:\\Projects\\SideScroller\\batR.png")
bat_l = pygame.image.load("D:\\Projects\\SideScroller\\batL.png")
grass = pygame.image.load("D:\\Projects\\SideScroller\\grass-transparent1.png")
grass = pygame.transform.scale(grass, (1280, 115))
bat_f = pygame.transform.scale(bat_f, (50, 50))
bat_r = pygame.transform.scale(bat_r, (50, 50))
bat_l = pygame.transform.scale(bat_l, (50, 50))


entities = pygame.sprite.Group()


player = Player()


player.position.x, player.position.y = 25, 580
# Display

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Side Scroller")

bear_sheet = pygame.image.load("D:\\Projects\\SideScroller\\bears.png").convert_alpha()

# Utility Functions
def get_image(sheet, frame, width, height, scale=0, color=None):
    image = pygame.Surface(SIZE).convert_alpha()
    image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color)

    return image


def create_fonts(font_sizes_list):
    "Creates different fonts with one list"
    pygame.font.init()
    fonts = []
    for size in font_sizes_list:
        fonts.append(pygame.font.SysFont("comicsansms", size))
    return fonts


def render(fnt, what, color, where):
    "Renders the fonts as passed from display_fps"
    text_to_show = fnt.render(what, 0, pygame.Color(color))
    screen.blit(text_to_show, where)


def display_fps():
    "Data that will be rendered and blitted in _display"
    render(fonts[0], what=str(int(clock.get_fps())), color="white", where=(0, 0))


fonts = create_fonts([32, 16, 14, 8])

frame_0 = get_image(bear_sheet, 0, 53, 32, 25, BLACK)
frame_1 = get_image(bear_sheet, 1, 53, 32, 25, BLACK)

enemy1 = Enemy(565, frame_0, frame_1)
enemy2 = Enemy(470, bat_l)

OUTPUT = False

entities.add(player)
entities.add(enemy1)

# Game Loop

clock = pygame.time.Clock()


if __name__ == "__main__":
    OUTPUT = True

while OUTPUT:

    dt = clock.tick(60) * 0.001 * TARGET_FPS

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if (
            event.type == pygame.QUIT  # pylint: disable=no-member
            or event.type == pygame.KEYDOWN  # pylint: disable=no-member
            and event.key == pygame.K_q  # pylint: disable=no-member
        ):  # Press the X in the top right or press Q to exit the game.
            print("Exiting...")
            sys.exit()

        if event.type == pygame.KEYDOWN:  # pylint: disable=no-member
            if event.key == pygame.K_LEFT:  # pylint: disable=no-member
                player.LEFT_KEY = True
                player.image = bat_l
            elif event.key == pygame.K_RIGHT:  # pylint: disable=no-member
                player.RIGHT_KEY = True
                player.image = bat_r
            elif event.key == pygame.K_SPACE:  # pylint: disable=no-member
                player.jump()

        if event.type == pygame.KEYUP:  # pylint: disable=no-member
            if event.key == pygame.K_LEFT:  # pylint: disable=no-member
                player.LEFT_KEY = False
            elif event.key == pygame.K_RIGHT:  # pylint: disable=no-member
                player.RIGHT_KEY = False
            elif event.key == pygame.K_SPACE:  # pylint: disable=no-member
                if player.is_jumping:
                    player.velocity.y *= 0.25
                    player.is_jumping = False

    screen.fill(BLUE)
    screen.blit(bkgnd, BACKGROUND)
    display_fps()
    ground = pygame.draw.rect(screen, BROWN, Rect(0, 600, 1280, 150))
    screen.blit(grass, (0, 550))
    player.update(dt)
    enemy1.update()
    enemy2.update()
    # entities.draw(screen)

    pygame.display.update()
