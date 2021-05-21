
SOURCES = (
    'https://armorgames.com/play/3642/medieval-rampage'
    'https://www.raywenderlich.com/24252/beginning-game-programming-for-teens-with-python'
    'https://www.pinterest.com/pin/288652657348582160/'
    'https://www.webucator.com/blog/2015/03/python-color-constants-module/'
    'https://stackoverflow.com/questions/20044791/how-to-make-an-enemy-follow-the-player-in-pygame'
    'https://gamedev.stackexchange.com/questions/106457/move-an-enemy-towards-the-player-in-pygame'
    'https://docs.python.org/3/library/math.html#hyperbolic-functions'
)

from Image_Imports import *
from Character_CLASS import *
from Enemy_CLASS import *
from Arrows_CLASS import *

def GetSpawnCoordinates():
    SpawnLocation = randint(1, 4)
    if SpawnLocation == 1:
        EnemySpawn = [randint(0, displayWidth), 0]
        return EnemySpawn
    if SpawnLocation == 2:
        EnemySpawn = [randint(0, displayWidth), displayHeigth]
        return EnemySpawn
    if SpawnLocation == 3:
        EnemySpawn = [0, randint(0, displayHeigth)]
        return EnemySpawn
    if SpawnLocation == 4:
        EnemySpawn = [displayWidth, randint(0, displayHeigth)]
        return EnemySpawn

def PauseGame():
    return 0

def RUN_GAMEPLAY(Selected_Arrow, EnemyCount, enemySpawnTimer, Countdown, MaximumEnemies):
    screen.fill(0)
    screen.blit(highResBackground, (0, 0))

    Player1.PlayerSetup()
    arrowControl()

    if enemySpawnTimer <= 0:
        SpawnLocation = GetSpawnCoordinates()
        enemyList.append(Get_Enemy(SpawnLocation))
        EnemyCount += 1
        enemySpawnTimer = 200
    elif enemySpawnTimer != 0:
        enemySpawnTimer -= Countdown

    if EnemyCount == MaximumEnemies:
        enemySpawnTimer = 50
        Countdown = 0

    arrowSelection()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                move[0] = True
            elif event.key == K_a:
                move[2] = True
            elif event.key == K_s:
                move[1] = True
            elif event.key == K_d:
                move[3] = True
            if event.key == K_1:
                Selected_Arrow = "Basic_Arrow"
                arrowAttributeSelecter(Selected_Arrow)
            if event.key == K_2:
                Selected_Arrow = "Steel_Arrow"
                arrowAttributeSelecter(Selected_Arrow)
            if event.key == K_3:
                Selected_Arrow = "HollowPoint_Arrow"
                arrowAttributeSelecter(Selected_Arrow)
            if event.key == K_4:
                Selected_Arrow = "Tri_Arrow"
                arrowAttributeSelecter(Selected_Arrow)
            if event.key == K_5:
                Selected_Arrow = "Frost_Arrow"
                arrowAttributeSelecter(Selected_Arrow)
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                move[0] = False
            elif event.key == K_a:
                move[2] = False
            elif event.key == K_s:
                move[1] = False
            elif event.key == K_d:
                move[3] = False
            if event.key == K_1:
                Selected_Arrow = "Basic_Arrow"
                arrowAttributeSelecter(Selected_Arrow)
            if event.key == K_2:
                Selected_Arrow = "Steel_Arrow"
                arrowAttributeSelecter(Selected_Arrow)
            if event.key == K_3:
                Selected_Arrow = "HollowPoint_Arrow"
                arrowAttributeSelecter(Selected_Arrow)
            if event.key == K_4:
                Selected_Arrow = "Tri_Arrow"
                arrowAttributeSelecter(Selected_Arrow)
            if event.key == K_5:
                Selected_Arrow = "Frost_Arrow"
                arrowAttributeSelecter(Selected_Arrow)
        if event.type == MOUSEBUTTONDOWN:
            if Selected_Arrow == "Basic_Arrow" or "Steel_Arrow" or "HollowPoint_Arrow" or "Tri_Arrow" or "Frost_Arrow":
                Arrow_Type.Basic_Coordinates()
    if move[0]:
        playerInitialpos[1] += -Player1.playerSpeed
    elif move[1]:
        playerInitialpos[1] += Player1.playerSpeed
    if move[2]:
        playerInitialpos[0] += -Player1.playerSpeed
    elif move[3]:
        playerInitialpos[0] += Player1.playerSpeed

    if playerInitialpos[0] <= 0:
        move[2] = False
    if playerInitialpos[1] <= 0:
        move[0] = False
    if playerInitialpos[0] >= displayWidth:
        move[3] = False
    if playerInitialpos[1] >= displayHeigth:
        move[1] = False

    pygame.display.update()
    clock.tick(120)


    return EnemyCount, enemySpawnTimer, Countdown, MaximumEnemies



EnemyCount = 0
enemySpawnTimer = 100
Countdown = 1
MaximumEnemies = 5

move = [False, False, False, False]

Run_Game = True
while Run_Game:

    RUN_GAMEPLAY(Selected_Arrow, EnemyCount, enemySpawnTimer, Countdown, MaximumEnemies)

    EnemyCount = RUN_GAMEPLAY(Selected_Arrow, EnemyCount, enemySpawnTimer, Countdown, MaximumEnemies)[0]
    enemySpawnTimer = RUN_GAMEPLAY(Selected_Arrow, EnemyCount, enemySpawnTimer, Countdown, MaximumEnemies)[1]
    Countdown = RUN_GAMEPLAY(Selected_Arrow, EnemyCount, enemySpawnTimer, Countdown, MaximumEnemies)[2]
    MaximumEnemies = RUN_GAMEPLAY(Selected_Arrow, EnemyCount, enemySpawnTimer, Countdown, MaximumEnemies)[3]




























# EnemyCount = 0
# enemySpawnTimer = 50
# Countdown = 1
# MaximumEnemies = 0
#
# move = [False, False, False, False]
#
# Run_Game = True
# while Run_Game:
#
#     screen.fill(0)
#
#     screen.blit(highResBackground, (0,0))
#
#     Player1.PlayerSetup()
#
#     arrowControl()
#
#     if enemySpawnTimer <= 0:
#         SpawnLocation = GetSpawnCoordinates()
#         enemyList.append(Get_Enemy())
#         EnemyCount += 1
#         enemySpawnTimer = 200
#     elif enemySpawnTimer != 0:
#         enemySpawnTimer = enemySpawnTimer - Countdown
#
#     if EnemyCount == MaximumEnemies:
#         enemySpawnTimer = 50
#         Countdown = 0
#
#     arrowSelection()
#
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         if event.type == pygame.KEYDOWN:
#             if event.key == K_w:
#                 move[0] = True
#             elif event.key == K_a:
#                 move[2] = True
#             elif event.key == K_s:
#                 move[1] = True
#             elif event.key == K_d:
#                 move[3] = True
#             if event.key == K_1:
#                 Selected_Arrow = "Basic_Arrow"
#                 arrowAttributeSelecter(Selected_Arrow)
#             if event.key == K_2:
#                 Selected_Arrow = "Steel_Arrow"
#                 arrowAttributeSelecter(Selected_Arrow)
#             if event.key == K_3:
#                 Selected_Arrow = "HollowPoint_Arrow"
#                 arrowAttributeSelecter(Selected_Arrow)
#             if event.key == K_4:
#                 Selected_Arrow = "Tri_Arrow"
#                 arrowAttributeSelecter(Selected_Arrow)
#             if event.key == K_5:
#                 Selected_Arrow = "Frost_Arrow"
#                 arrowAttributeSelecter(Selected_Arrow)
#         if event.type == pygame.KEYUP:
#             if event.key == K_w:
#                 move[0] = False
#             elif event.key == K_a:
#                 move[2] = False
#             elif event.key == K_s:
#                 move[1] = False
#             elif event.key == K_d:
#                 move[3] = False
#             if event.key == K_1:
#                 Selected_Arrow = "Basic_Arrow"
#                 arrowAttributeSelecter(Selected_Arrow)
#             if event.key == K_2:
#                 Selected_Arrow = "Steel_Arrow"
#                 arrowAttributeSelecter(Selected_Arrow)
#             if event.key == K_3:
#                 Selected_Arrow = "HollowPoint_Arrow"
#                 arrowAttributeSelecter(Selected_Arrow)
#             if event.key == K_4:
#                 Selected_Arrow = "Tri_Arrow"
#                 arrowAttributeSelecter(Selected_Arrow)
#             if event.key == K_5:
#                 Selected_Arrow = "Frost_Arrow"
#                 arrowAttributeSelecter(Selected_Arrow)
#         if event.type == MOUSEBUTTONDOWN:
#             if Selected_Arrow == "Basic_Arrow" or "Steel_Arrow" or "HollowPoint_Arrow" or "Tri_Arrow" or "Frost_Arrow":
#                 Arrow_Type.Basic_Coordinates()
#     if move[0]:
#         playerInitialpos[1] += -Player1.playerSpeed
#     elif move[1]:
#         playerInitialpos[1] += Player1.playerSpeed
#     if move[2]:
#         playerInitialpos[0] += -Player1.playerSpeed
#     elif move[3]:
#         playerInitialpos[0] += Player1.playerSpeed
#
#     if playerInitialpos[0] <= 0:
#         move[2] = False
#     if playerInitialpos[1] <= 0:
#         move[0] = False
#     if playerInitialpos[0] >= displayWidth:
#         move[3] = False
#     if playerInitialpos[1] >= displayHeigth:
#         move[1] = False
#
#     pygame.display.update()
#     clock.tick(120)