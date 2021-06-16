from Game_Files.Arrows_CLASS import Arrow
from Game_Files.Arrows_CLASS import *
from Game_Files.Character_CLASS import *
from Game_Files.Enemy_CLASS import *




# GENERAL FUNCTIONS:

def centerText(imageDimensions):
    centerCoordinates = (displayWidth / 2, displayHeight / 2)
    placement = (centerCoordinates[0] - imageDimensions[0]/2 , centerCoordinates[1] - imageDimensions[1]/2)
    return placement



def RESET_GAME():
    pass




# ENEMY FUNCTIONS:

def generateEnemySpawnCoordinates():
    SpawnLocation = randint(1, 4)
    if SpawnLocation == 1:
        EnemySpawn = [randint(0, displayWidth), 0]
        return EnemySpawn
    if SpawnLocation == 2:
        EnemySpawn = [randint(0, displayWidth), displayHeight]
        return EnemySpawn
    if SpawnLocation == 3:
        EnemySpawn = [0, randint(0, displayHeight)]
        return EnemySpawn
    if SpawnLocation == 4:
        EnemySpawn = [displayWidth, randint(0, displayHeight)]
        return EnemySpawn

def generateEnemy(SpawnLocation):
    EnemySelect = randint(1, 4)
    if EnemySelect == 1:
        SelectedEnemy = Enemy(enemy_one, 2.6, 10, 13, SpawnLocation[0], SpawnLocation[1])
        return SelectedEnemy
    if EnemySelect == 2:
        SelectedEnemy = Enemy(enemy_two, 2.4, 25, 21, SpawnLocation[0], SpawnLocation[1])
        return SelectedEnemy
    if EnemySelect == 3:
        SelectedEnemy = Enemy(enemy_three, 2.9, 45, 8, SpawnLocation[0], SpawnLocation[1])
        return SelectedEnemy
    if EnemySelect == 4:
        SelectedEnemy = Enemy(enemy_four, 2.3, 65, 32, SpawnLocation[0], SpawnLocation[1])
        return SelectedEnemy





# ARROW FUNCTIONS:

Arrow_Type = Arrow(Basic_Arrow, 19, 4)
selectedArrow = "Basic_Arrow"

def arrowControl():
    for ARROW in ARROW_LIST:
        if selectedArrow == "Basic_Arrow" or "Steel_Arrow" or "HollowPoint_Arrow" or "Tri_Arrow" or "Frost_Arrow":
            Arrow_Type.Basic_Control(ARROW)

def arrowSelection():
    output = False # Not needed... just initialized 'output' variable
    if selectedArrow == "Basic_Arrow" or "Steel_Arrow":
        output = Arrow_Type.Basic_Hit()
    elif selectedArrow == "HollowPoint_Arrow":
        output = Arrow_Type.Basic_Hit()
        # Arrow_Type.HollowPoint_Hit()
    elif selectedArrow == "Tri_Arrow":
        output = Arrow_Type.Basic_Hit()
        # Arrow_Type.Tri_Hit()
    elif selectedArrow == "Frost_Arrow":
        output = Arrow_Type.Basic_Hit()
        # Arrow_Type.Frost_Hit()
    return output


def arrowAttributeSelecter(selectedArrow):
    if selectedArrow == "Basic_Arrow":
        Arrow_Type.setArrowParameters(Basic_Arrow, 19, 4)
    elif selectedArrow == "Steel_Arrow":
        Arrow_Type.setArrowParameters(Steel_Arrow, 19, 7)
    elif selectedArrow == "HollowPoint_Arrow":
        Arrow_Type.setArrowParameters(HollowPoint_Arrow, 19, 200)
    elif selectedArrow == "Tri_Arrow":
        Arrow_Type.setArrowParameters(Tri_Arrow, 19, 3)
    elif selectedArrow == "Frost_Arrow":
        Arrow_Type.setArrowParameters(Frost_Arrow, 19, 4)

