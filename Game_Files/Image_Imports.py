
# Basic imports
import pygame
import os
import sys
import ctypes

from pygame.locals import *
from random import *
import math


# Creates the display for pygame
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

ctypes.windll.user32.SetProcessDPIAware()

displayWidth = ctypes.windll.user32.GetSystemMetrics(0)
displayHeight = ctypes.windll.user32.GetSystemMetrics(1)
# displayWidth = ctypes.windll.user32.GetSystemMetrics(0) - 200
# displayHeight = ctypes.windll.user32.GetSystemMetrics(1) - 200
flags = FULLSCREEN | DOUBLEBUF
# flags = FULLSCREEN | SCALED
screen = pygame.display.set_mode( (displayWidth, displayHeight), flags, 16)

screen.set_alpha(None)

pygame.display.set_caption('Crossbow Battle')


# Initialize all Colors:
DARKGREY = (64, 64, 64)
LIGHTGREY = (160, 160, 160)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLDENROD = (255, 205, 0)
DARKORANGE = (176, 129, 0)
REALLYDARKORANGE = (103, 56, 0)
RED = (255, 51, 51)
DARKRED = (102, 0, 0)
GREEN = (102, 255, 102)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
LIGHTBLUE = (0, 255, 255)
PURPLE = (127, 0, 255)
ORANGE = (255, 153, 51)
BROWN = (139, 69, 19) # "saddlebrown"



# Loads all the game images:
basePath = os.path.dirname(__file__)

highResBackground = pygame.image.load( os.path.join(basePath, "GameResources/Dirt_Background_1200x800_HighRes.png") ).convert()
Help_PIC = pygame.image.load( os.path.join(basePath, "GameResources/Help_PIC.png") ).convert()

player = pygame.image.load( os.path.join(basePath, "GameResources/PixelGunman_84x59.png") )

Gold_1 = pygame.image.load( os.path.join(basePath, "GameResources/Gold_1.png") )
Gold_2 = pygame.image.load( os.path.join(basePath, "GameResources/Gold_2.png") )
Gold_3 = pygame.image.load( os.path.join(basePath, "GameResources/Gold_3.png") )

Health_Potion = pygame.image.load( os.path.join(basePath, "GameResources/Health_Potion.png") )

Iron_Arrow = pygame.image.load( os.path.join(basePath, "GameResources/Basic_Arrow_32x7.png") )
Steel_Arrow = pygame.image.load( os.path.join(basePath, "GameResources/Steel_Arrow_32x7.png") )
Hollowpoint_Arrow = pygame.image.load(os.path.join(basePath, "GameResources/HollowPoint_Arrow_32x7.png"))
Tri_Arrow = pygame.image.load( os.path.join(basePath, "GameResources/Tri_Arrow_32x7.png") )
Frost_Arrow = pygame.image.load( os.path.join(basePath, "GameResources/Frost_Arrow_32x7.png") )

fireball = pygame.image.load( os.path.join(basePath, "GameResources/Fireball_60x23.png") )

# enemy_Boss_one = pygame.image.load( os.path.join(basePath, "GameResources/") )
# enemy_Boss_two = pygame.image.load( os.path.join(basePath, "GameResources/") )
# enemy_Boss_three = pygame.image.load( os.path.join(basePath, "GameResources/") )

enemy_one = pygame.image.load( os.path.join(basePath, "GameResources/PixelEnemy_1_48x56.png") )
enemy_two = pygame.image.load( os.path.join(basePath, "GameResources/PixelEnemy_2_62x62.png") )
enemy_three = pygame.image.load( os.path.join(basePath, "GameResources/PixelEnemy_3_140x54.png") )
enemy_four = pygame.image.load( os.path.join(basePath, "GameResources/PixelEnemy_4_58x72.png") )



highResBackground = pygame.transform.scale(highResBackground, (displayWidth, displayHeight)).convert()
Help_PIC = pygame.transform.scale(Help_PIC, ( round(Help_PIC.get_rect()[2] * (displayHeight/Help_PIC.get_rect()[3]) ), round(Help_PIC.get_rect()[3] * (displayHeight/Help_PIC.get_rect()[3])) ) ).convert()

player = pygame.transform.scale( player, ( round(player.get_rect()[2] * 1.3) ,  round(player.get_rect()[3] * 1.3) ) ).convert_alpha()

Health_Potion = pygame.transform.scale( Health_Potion, (round(Health_Potion.get_rect()[2] * 0.4), round(Health_Potion.get_rect()[3] * 0.4)) ).convert_alpha()
Gold_1 = pygame.transform.scale( Gold_1, (round(Gold_1.get_rect()[2] * 1.4), round(Gold_1.get_rect()[3] * 1.4)) ).convert_alpha()
Gold_2 = pygame.transform.scale( Gold_2, (round(Gold_2.get_rect()[2] * 1.3), round(Gold_2.get_rect()[3] * 1.3)) ).convert_alpha()
Gold_3 = pygame.transform.scale( Gold_3, (round(Gold_3.get_rect()[2] * 1.4), round(Gold_3.get_rect()[3] * 1.4)) ).convert_alpha()

Iron_Arrow = pygame.transform.scale(Iron_Arrow, (round(Iron_Arrow.get_rect()[2] * 3) , round(Iron_Arrow.get_rect()[3] * 3))).convert_alpha()
Steel_Arrow = pygame.transform.scale( Steel_Arrow, ( round(Steel_Arrow.get_rect()[2] * 3) , round(Steel_Arrow.get_rect()[3] * 3) ) ).convert_alpha()
Hollowpoint_Arrow = pygame.transform.scale(Hollowpoint_Arrow, (round(Hollowpoint_Arrow.get_rect()[2] * 2.5) , round(Hollowpoint_Arrow.get_rect()[3] * 3))).convert_alpha()
Tri_Arrow = pygame.transform.scale( Tri_Arrow, ( round(Tri_Arrow.get_rect()[2] * 3) , round(Tri_Arrow.get_rect()[3] * 3) ) ).convert_alpha()
Frost_Arrow = pygame.transform.scale( Frost_Arrow, ( round(Frost_Arrow.get_rect()[2] * 3) , round(Frost_Arrow.get_rect()[3] * 3) ) ).convert_alpha()

Iron_Arrow_ARMORY = pygame.transform.scale(Iron_Arrow, (round(Iron_Arrow.get_rect()[2] * (4/3) ) , round(Iron_Arrow.get_rect()[3] * (4/3) ) ) ).convert_alpha()
Steel_Arrow_ARMORY = pygame.transform.scale( Steel_Arrow, ( round(Steel_Arrow.get_rect()[2] * (4/3) ) , round(Steel_Arrow.get_rect()[3] * (4/3) ) ) ).convert_alpha()
Hollowpoint_Arrow_ARMORY = pygame.transform.scale(Hollowpoint_Arrow, (round(Hollowpoint_Arrow.get_rect()[2] * (4/3) ) , round(Hollowpoint_Arrow.get_rect()[3] * (4/3) ) ) ).convert_alpha()
Tri_Arrow_ARMORY = pygame.transform.scale( Tri_Arrow, ( round(Tri_Arrow.get_rect()[2] * (4/3) ) , round(Tri_Arrow.get_rect()[3] * (4/3) ) ) ).convert_alpha()
Frost_Arrow_ARMORY = pygame.transform.scale( Frost_Arrow, ( round(Frost_Arrow.get_rect()[2] * (4/3) ) , round(Frost_Arrow.get_rect()[3] * (4/3) ) ) ).convert_alpha()

arrowDict = {"Iron_Arrows" : Iron_Arrow_ARMORY, "Steel_Arrows" : Steel_Arrow_ARMORY, "Hollowpoint_Arrows" : Hollowpoint_Arrow_ARMORY, "Tri_Arrows" : Tri_Arrow_ARMORY, "Frost_Arrows" : Frost_Arrow_ARMORY}

enemy_one = pygame.transform.scale( enemy_one, ( round(enemy_one.get_rect()[2] * 1.5) , round(enemy_one.get_rect()[3] * 1.5) ) ).convert_alpha()
enemy_two = pygame.transform.scale( enemy_two, ( round(enemy_two.get_rect()[2] * 1.5) , round(enemy_two.get_rect()[3] * 1.5) ) ).convert_alpha()
enemy_three = pygame.transform.scale( enemy_three, ( round(enemy_three.get_rect()[2] * 1.5) , round(enemy_three.get_rect()[3] * 1.5) ) ).convert_alpha()
enemy_four = pygame.transform.scale( enemy_four, ( round(enemy_four.get_rect()[2] * 1.5) , round(enemy_four.get_rect()[3] * 1.5) ) ).convert_alpha()



### INITIALIZE BUTTON/BACKGROUND DIMENSIONS:

# Main Menu Buttons:
PLAY = (700, 250)
HELP = (700, 250)
EXIT_GAME = (700, 250)

# Help Menu Buttons:
HELP_MENU_BACK = (500, 250)

# Armory Buttons:
CONTINUE = (500, 150)

ARROW_BUTTON = (300, 200)
BUY_BUTTON = ( 150, 100 )
EQUIP_BUTTON = ( 150, 100 )
SELL_BUTTON = ( 150, 100 )

ARMORY_ITEM_SLOT = (200, 200)
GAMEPLAY_ITEM_SLOT = ( 120, 120 )

HOTBAR_ARMORY_BORDER = 10

# Pause Menu Buttons/Background Dimensions:
PAUSE_BACKGROUND = (700, 1000)
RESUME = (650, 250)
QUIT = (650, 250)

# Game Over Buttons/Background Dimensions:
YOU_DIED_BACKGROUND = (900, 300)
GAMEOVER_BACKGROUND = (700, 1000)
PLAY_AGAIN = (650, 250)
EXIT = (650, 250)



### ARMORY CONSTANTS:

# INITIALIZE FONTS:
BUTTON_FONT = pygame.font.SysFont( "Times New Roman, Ariel", 100 )
PRICE_FONT = pygame.font.SysFont( "Times New Roman, Ariel", 50 )


# INITIALIZE BUTTON TEXTS:
Continue_TEXT = BUTTON_FONT.render( "Continue", True, RED )

SteelName_TEXT = PRICE_FONT.render( "Steel", True, DARKRED )
HollowpointName_TEXT = PRICE_FONT.render( "Hollowpoint", True, DARKRED )
FrostName_TEXT = PRICE_FONT.render( "Frost", True, DARKRED )
TriName_TEXT = PRICE_FONT.render( "Tri", True, DARKRED )

BuyQuantity_TEXT = PRICE_FONT.render( "x50", True, DARKRED )

SteelPrice_TEXT = PRICE_FONT.render( "$25", True, DARKRED )
HollowpointPrice_TEXT = PRICE_FONT.render( "$30", True, DARKRED )
FrostPrice_TEXT = PRICE_FONT.render( "$35", True, DARKRED )
TriPrice_TEXT = PRICE_FONT.render( "$35", True, DARKRED )

Buy_TEXT = PRICE_FONT.render( "Buy", True, WHITE )
Equip_TEXT = PRICE_FONT.render( "Equip", True, WHITE )
Sell_TEXT = PRICE_FONT.render( "Sell", True, WHITE )


# INITIALIZE BUTTON COORDINATES:
CONTINUE_COOR = ( displayWidth - CONTINUE[0] - 50, displayHeight - CONTINUE[1] - 50 )
Continue_TEXT_COOR = ( displayWidth - CONTINUE[0] / 2 - Continue_TEXT.get_rect().width / 2 - 50, displayHeight - CONTINUE[1] / 2 - Continue_TEXT.get_rect().height / 2 - 50 )
ARROW_BUTTON_COOR = ( 200, 1100 ) # Sets the top left button... all other buttons are oriented to this button for rearrangement simplicity
BUY_BUTTON_COOR = ( 400, 800 )
SELL_BUTTON_COOR = (650, 800)
EQUIP_BUTTON_COOR = ( 900, 800 )

HOTBAR_ARMORY_COOR = (450, 300)
ITEM_SLOT1_COOR = (HOTBAR_ARMORY_COOR[0], HOTBAR_ARMORY_COOR[1])
ITEM_SLOT2_COOR = (HOTBAR_ARMORY_COOR[0] + ARMORY_ITEM_SLOT[0], HOTBAR_ARMORY_COOR[1])
ITEM_SLOT3_COOR = (HOTBAR_ARMORY_COOR[0] + ARMORY_ITEM_SLOT[0] * 2, HOTBAR_ARMORY_COOR[1])
ITEM_SLOT4_COOR = (HOTBAR_ARMORY_COOR[0] + ARMORY_ITEM_SLOT[0] * 3, HOTBAR_ARMORY_COOR[1])

    # Gameplay HotBar coordinates:
HOTBAR_GAMEPLAY_COOR = (displayWidth / 2 - GAMEPLAY_ITEM_SLOT[0] * 2, displayHeight - 150)
ITEM_SLOT1_GAMEPLAY_COOR = (HOTBAR_GAMEPLAY_COOR[0], HOTBAR_GAMEPLAY_COOR[1])
ITEM_SLOT2_GAMEPLAY_COOR = (HOTBAR_GAMEPLAY_COOR[0] + GAMEPLAY_ITEM_SLOT[0], HOTBAR_GAMEPLAY_COOR[1])
ITEM_SLOT3_GAMEPLAY_COOR = (HOTBAR_GAMEPLAY_COOR[0] + GAMEPLAY_ITEM_SLOT[0] * 2, HOTBAR_GAMEPLAY_COOR[1])
ITEM_SLOT4_GAMEPLAY_COOR = (HOTBAR_GAMEPLAY_COOR[0] + GAMEPLAY_ITEM_SLOT[0] * 3, HOTBAR_GAMEPLAY_COOR[1])
