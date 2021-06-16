
# Basic imports
import pygame, sys
import ctypes
from pygame.locals import *
from random import *
import math

# Creates the display for pygame
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

ctypes.windll.user32.SetProcessDPIAware()

displayWidth = ctypes.windll.user32.GetSystemMetrics(0) - 200
displayHeight = ctypes.windll.user32.GetSystemMetrics(1) - 200
screen = pygame.display.set_mode((displayWidth, displayHeight))

pygame.display.set_caption('Crossbow Battle')






# These are the two script paths, one for the local drive and one for one drive, which should be added to the pygame load function if using pycharm as your IDE.
ScriptPath_OneDrive = "C:/Users/Chris.Carmona18/Desktop/Coding Stuff/Chris/"
ScriptPath_SurfaceBook2 = "C:/Users/_Chris_Carmona_/Desktop/Python_Coding_Files/"
# FULL DIRECTORY:   C:/Users/_Chris_Carmona_/Desktop/Coding_Stuff/resources/CrossbowGameImages/Dirt_Background_1200x800_HighRes.png

# Load all Colors:
DARKGREY = (64, 64, 64)
LIGHTGREY = (160, 160, 160)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLDENROD = (255, 205, 0)
RED = (255, 51, 51)
GREEN = (102, 255, 102)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (127, 0, 255)
ORANGE = (255, 153, 51)

# Loads all the game images:
highResBackground = pygame.image.load(ScriptPath_SurfaceBook2 + "resources/CrossbowGameImages/Dirt_Background_1200x800_HighRes.png").convert()
lowResBackground = pygame.image.load(ScriptPath_SurfaceBook2 + "resources/CrossbowGameImages/Low_Res_Dirt_Background.png")
mainMenuBackground = GOLDENROD

#healthBar = pygame.image.load(ScriptPath_SurfaceBook2 + "resources/CrossbowGameImages/healthbar.png")
#health = pygame.image.load(ScriptPath_SurfaceBook2 + "resources/CrossbowGameImages/Healthbar.png")

player = pygame.image.load(ScriptPath_SurfaceBook2 + "resources/CrossbowGameImages/PixelGunman_84x59.png")

Basic_Arrow = pygame.image.load(ScriptPath_SurfaceBook2 + "resources/CrossbowGameImages/Basic_Arrow_32x7.png")
Steel_Arrow = pygame.image.load(ScriptPath_SurfaceBook2 + "resources/CrossbowGameImages/Steel_Arrow_32x7.png")
HollowPoint_Arrow = pygame.image.load(ScriptPath_SurfaceBook2 + "resources/CrossbowGameImages/HollowPoint_Arrow_32x7.png")
Tri_Arrow = pygame.image.load(ScriptPath_SurfaceBook2 + "resources/CrossbowGameImages/Tri_Arrow_32x7.png")
Frost_Arrow = pygame.image.load(ScriptPath_SurfaceBook2 + "resources/CrossbowGameImages/Frost_Arrow_32x7.png")

fireball = pygame.image.load(ScriptPath_SurfaceBook2 + "resources/CrossbowGameImages/Fireball_60x23.png")

enemy_one = pygame.image.load(ScriptPath_SurfaceBook2 + "resources/CrossbowGameImages/PixelEnemy_1_48x56.png")
enemy_two = pygame.image.load(ScriptPath_SurfaceBook2 + "resources/CrossbowGameImages/PixelEnemy_2_62x62.png")
enemy_three = pygame.image.load(ScriptPath_SurfaceBook2 + "resources/CrossbowGameImages/PixelEnemy_3_140x54.png")
enemy_four = pygame.image.load(ScriptPath_SurfaceBook2 + "resources/CrossbowGameImages/PixelEnemy_4_58x72.png")

# enemy_Boss_one = pygame.image.load(ScriptPath_Local + "resources/CrossbowGameImages/").convert()
# enemy_Boss_two = pygame.image.load(ScriptPath_Local + "resources/CrossbowGameImages/").convert()
# enemy_Boss_three = pygame.image.load(ScriptPath_Local + "resources/CrossbowGameImages/")




# RESIZING IMAGES:

highResBackground = pygame.transform.scale(highResBackground, (displayWidth, displayHeight)).convert()

player = pygame.transform.scale( player, ( round(player.get_rect()[2] * 1.3) ,  round(player.get_rect()[3] * 1.3) ) )

Basic_Arrow = pygame.transform.scale( Basic_Arrow, ( round(Basic_Arrow.get_rect()[2] * 2.5) , round(Basic_Arrow.get_rect()[3] * 2.5) ) )
Steel_Arrow = pygame.transform.scale( Steel_Arrow, ( round(Steel_Arrow.get_rect()[2] * 2.5) , round(Steel_Arrow.get_rect()[3] * 2.5) ) )
HollowPoint_Arrow = pygame.transform.scale( HollowPoint_Arrow, ( round(HollowPoint_Arrow.get_rect()[2] * 2.5) , round(HollowPoint_Arrow.get_rect()[3] * 2.5) ) )
Tri_Arrow = pygame.transform.scale( Tri_Arrow, ( round(Tri_Arrow.get_rect()[2] * 2.5) , round(Tri_Arrow.get_rect()[3] * 2.5) ) )
Frost_Arrow = pygame.transform.scale( Frost_Arrow, ( round(Frost_Arrow.get_rect()[2] * 2.5) , round(Frost_Arrow.get_rect()[3] * 2.5) ) )

enemy_one = pygame.transform.scale( enemy_one, ( round(enemy_one.get_rect()[2] * 1.5) , round(enemy_one.get_rect()[3] * 1.5) ) )
enemy_two = pygame.transform.scale( enemy_two, ( round(enemy_two.get_rect()[2] * 1.5) , round(enemy_two.get_rect()[3] * 1.5) ) )
enemy_three = pygame.transform.scale( enemy_three, ( round(enemy_three.get_rect()[2] * 1.5) , round(enemy_three.get_rect()[3] * 1.5) ) )
enemy_four = pygame.transform.scale( enemy_four, ( round(enemy_four.get_rect()[2] * 1.5) , round(enemy_four.get_rect()[3] * 1.5) ) )