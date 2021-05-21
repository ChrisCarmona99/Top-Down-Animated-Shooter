
# Basic imports
import pygame, sys
from pygame.locals import *
from random import *
import math

# Creates the display for pygame
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
displayWidth = 1200
displayHeigth = 800
screen = pygame.display.set_mode((displayWidth, displayHeigth))
pygame.display.set_caption('Crossbow Battle')


# These are the two script paths, one for the local drive and one for one drive, which should be added to the pygame load function if using pycharm as your IDE.
ScriptPath_OneDrive = "C:/Users/Chris.Carmona18/Desktop/Coding Stuff/Chris/"
ScriptPath_SurfaceBook2 = "C:/Users/_Chris_Carmona_/Desktop/Python_Coding_Files/"
# FULL DIRECTORY:   C:/Users/_Chris_Carmona_/Desktop/Coding_Stuff/resources/CrossbowGameImages/Dirt_Background_1200x800_HighRes.png

# Loads all the game images:
highResBackground = pygame.image.load(ScriptPath_SurfaceBook2 + "resources/CrossbowGameImages/Dirt_Background_1200x800_HighRes.png").convert()
lowResBackground = pygame.image.load(ScriptPath_SurfaceBook2 + "resources/CrossbowGameImages/Low_Res_Dirt_Background.png")
healthbar = pygame.image.load(ScriptPath_SurfaceBook2 + "resources/CrossbowGameImages/healthbar.png")
health = pygame.image.load(ScriptPath_SurfaceBook2 + "resources/CrossbowGameImages/Healthbar.png")

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