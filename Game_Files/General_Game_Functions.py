
from Game_Files.Arrows_CLASS import Arrow
from Game_Files.Arrows_CLASS import *
from Game_Files.Character_CLASS import *
from Game_Files.Enemy_CLASS import *



# GENERAL FUNCTIONS:

def centerText(imageDimensions):
    centerCoordinates = (displayWidth / 2, displayHeight / 2)
    placement = (centerCoordinates[0] - imageDimensions[0]/2 , centerCoordinates[1] - imageDimensions[1]/2)
    return placement


def SHOOT(Selected_Arrow):
    if Selected_Arrow == "Basic_Arrow" or "Steel_Arrow" or "HollowPoint_Arrow" or "Tri_Arrow" or "Frost_Arrow":
        Arrow_Type.Basic_Coordinates()


def DISPLAY_WAVE(currentRound):

    currentRoundText = "Wave " + str(currentRound)
    FONT = pygame.font.SysFont( "Times New Roman, Ariel", 200 )
    CurrentWave_TEXT = FONT.render( currentRoundText, True, RED )

    drawWaveCount = True
    drawWaveCountTimer = 250 # Sets how long to draw 'Wave #' for each round

    while drawWaveCount:
        screen.blit( CurrentWave_TEXT, ( displayWidth / 2 - CurrentWave_TEXT.get_rect().width / 2, displayHeight / 2 - CurrentWave_TEXT.get_rect().height/2 - 300) )
        drawWaveCountTimer -= 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if drawWaveCountTimer == 0:
            drawWaveCount = False

        pygame.display.update()
        clock.tick(120)


def RESET():
    ENEMY_LIST.clear()
    Player1.spawnPos = [displayWidth * 0.5, displayHeight * 0.5]
    Player1.currentHealth = Player1.maximumHealth
    Player1.targetHealth = Player1.maximumHealth
    Player1.playerSpeed = Player1.resetPlayerSpeed
    Player1.playerScore = 0
    ARROW_LIST.clear()



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
        SelectedEnemy = EnemyONE(enemy_one, 6, 10, 13, 10, SpawnLocation[0], SpawnLocation[1])
        return SelectedEnemy
    if EnemySelect == 2:
        SelectedEnemy = EnemyTWO(enemy_two, 4, 25, 21, 15, SpawnLocation[0], SpawnLocation[1])
        return SelectedEnemy
    if EnemySelect == 3:
        SelectedEnemy = EnemyTHREE(enemy_three, 7.5, 45, 8, 20, SpawnLocation[0], SpawnLocation[1])
        return SelectedEnemy
    if EnemySelect == 4:
        SelectedEnemy = EnemyFOUR(enemy_four, 3, 65, 32, 30, SpawnLocation[0], SpawnLocation[1])
        return SelectedEnemy



# ARROW FUNCTIONS:

Arrow_Type = Arrow(Basic_Arrow, 24, 4)
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


def arrowAttributeSelecter(arrowInUse):
    if arrowInUse == "Basic_Arrow":
        Arrow_Type.setArrowParameters(Basic_Arrow, 24, 4)
    elif arrowInUse == "Steel_Arrow":
        Arrow_Type.setArrowParameters(Steel_Arrow, 24, 7)
    elif arrowInUse == "HollowPoint_Arrow":
        Arrow_Type.setArrowParameters(HollowPoint_Arrow, 24, 200)
    elif arrowInUse == "Tri_Arrow":
        Arrow_Type.setArrowParameters(Tri_Arrow, 24, 3)
    elif arrowInUse == "Frost_Arrow":
        Arrow_Type.setArrowParameters(Frost_Arrow, 24, 4)

