import random

from Game_Files.Arrows_CLASS import Arrow
from Game_Files.Arrows_CLASS import *
from Game_Files.Character_CLASS import *
from Game_Files.Enemy_CLASS import *
from Game_Files.Items_CLASS import *
import random



# GENERAL FUNCTIONS:
def centerText(imageDimensions):
    centerCoordinates = (displayWidth / 2, displayHeight / 2)
    placement = (centerCoordinates[0] - imageDimensions[0]/2 , centerCoordinates[1] - imageDimensions[1]/2)
    return placement

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
        SelectedEnemy = EnemyONE(enemy_one, 6, 10, 13, 10, ['NONE', 'Gold_1', 'Health_Potion'], [100, 25, 5], SpawnLocation[0], SpawnLocation[1])
        return SelectedEnemy
    if EnemySelect == 2:
        SelectedEnemy = EnemyTWO(enemy_two, 4.5, 25, 21, 15, ['NONE', 'Gold_1', 'Gold_2', 'Health_Potion'], [100, 50, 5, 5], SpawnLocation[0], SpawnLocation[1])
        return SelectedEnemy
    if EnemySelect == 3:
        SelectedEnemy = EnemyTHREE(enemy_three, 7.5, 45, 8, 20, ['NONE', 'Gold_1', 'Gold_2', 'Health_Potion'], [100, 25, 15, 10], SpawnLocation[0], SpawnLocation[1])
        return SelectedEnemy
    if EnemySelect == 4:
        SelectedEnemy = EnemyFOUR(enemy_four, 3.5, 65, 32, 30, ['NONE', 'Gold_2', 'Gold_3', 'Health_Potion'], [100, 50, 5, 10], SpawnLocation[0], SpawnLocation[1])
        return SelectedEnemy


# ARROW FUNCTIONS:
def SHOOT_CONTROL(selectedArrow):
    if selectedArrow == "Iron_Arrows":
        currentArrow = IronArrow(Iron_Arrow, 24, 4, Player1.playerAngle)
        ARROW_LIST.append(currentArrow)

    elif selectedArrow == "Steel_Arrows":
        currentArrow = SteelArrow(Steel_Arrow, 24, 7, Player1.playerAngle)
        ARROW_LIST.append(currentArrow)

        Player1.INVENTORY["Steel_Arrows"] -= 1
        if Player1.INVENTORY.get("Steel_Arrows") == 0:
            selectedArrow = "Iron_Arrows"

    elif selectedArrow == "Hollowpoint_Arrows":
        currentArrow = HollowpointArrow(Hollowpoint_Arrow, 24, 5, Player1.playerAngle)
        ARROW_LIST.append(currentArrow)

        Player1.INVENTORY["Hollowpoint_Arrows"] -= 1
        if Player1.INVENTORY.get("Hollowpoint_Arrows") == 0:
            selectedArrow = "Iron_Arrows"

    elif selectedArrow == "Tri_Arrows":
        currentArrow = TriArrow(Tri_Arrow, 24, 4, Player1.playerAngle)
        ARROW_LIST.append(currentArrow)

        Player1.INVENTORY["Tri_Arrows"] -= 1
        if Player1.INVENTORY.get("Tri_Arrows") == 0:
            selectedArrow = "Iron_Arrows"

    elif selectedArrow == "Frost_Arrows":
        currentArrow = FrostArrow(Frost_Arrow, 35, 4, Player1.playerAngle)
        ARROW_LIST.append(currentArrow)

        Player1.INVENTORY["Frost_Arrows"] -= 1
        if Player1.INVENTORY.get("Frost_Arrows") == 0:
            selectedArrow = "Iron_Arrows"

    return selectedArrow

def COLLISION_CHECK(pos1, pos2, hitBox1, hitBox2):
    dist = math.sqrt(((pos2[0] - pos1[0]) ** 2) + ((pos2[1] - pos1[1]) ** 2))
    if dist <= (hitBox1 + hitBox2):
        return True
    else:
        return False

def COLLISION_CONTROL():

    playerDied = False

    enemyIndex = 0
    for enemy in ENEMY_LIST:

        if enemy.currentEnemySpeed == 0:
            enemy.idleTimer -= 1
            if enemy.idleTimer == 0:
                enemy.idleTimer = 50
                enemy.currentEnemyDamage = enemy.activeDamage
                enemy.currentEnemySpeed = enemy.activeSpeed

        enemy.drawEnemy()  # DRAWS ENEMIES ON THE SCREEN AT INITIAL SPAWN COORDINATES

        if enemy.currentEnemyPos != Player1.spawnPos:
            enemy.enemyMove()  # MOVES ENEMIES TOWARDS THE PLAYER

        # HANDLES ENEMY<->PLAYER COLLISION:
        EnemyPlayerCollide = COLLISION_CHECK(Player1.hitEpicenter, enemy.hitEpicenter, Player1.hitBox, enemy.hitBox)
        if EnemyPlayerCollide:
            Player1.getDamage(enemy.currentEnemyDamage)
            enemy.currentEnemySpeed = enemy.idleSpeed
            enemy.currentEnemyDamage = enemy.idleDamage

            if Player1.targetHealth <= 0:
                playerDied = True
                return playerDied

        # HANDLES ARROW<->ENEMY COLLISION:
        arrowIndex = 0
        for arrow in ARROW_LIST:

            ArrowEnemyCollide = COLLISION_CHECK(enemy.hitEpicenter, arrow.hitEpicenter, enemy.hitBox, arrow.hitBox)
            if ArrowEnemyCollide:
                enemyHealth = enemy.enemyHealth - arrow.arrowDamage
                ARROW_LIST.pop(arrowIndex)
                if enemyHealth <= 0:
                    Player1.playerScore += enemy.enemyScore
                    killedEnemy = ENEMY_LIST.pop(enemyIndex)
                    getNewItem(killedEnemy)
                elif enemyHealth > 0:
                    enemy.setEnemyHealth(enemyHealth)
            arrowIndex += 1
        enemyIndex += 1

    return playerDied


# ITEM FUNCTIONS:

def getNewItem(killedEnemy):

    droppedItem = random.choices(killedEnemy.potentialItemDrops, weights=killedEnemy.dropRates, k=1)
    if droppedItem == ['Gold_1']:
        newItem = Gold(Gold_1, 22, killedEnemy.hitEpicenter, 10)
        ITEM_LIST.append(newItem)
    if droppedItem == ['Gold_2']:
        newItem = Gold(Gold_2, 22, killedEnemy.hitEpicenter, 20)
        ITEM_LIST.append(newItem)
    if droppedItem == ['Gold_3']:
        newItem = Gold(Gold_3, 22, killedEnemy.hitEpicenter, 50)
        ITEM_LIST.append(newItem)
    if droppedItem == ['Health_Potion']:
        newItem = HealthPotion(Health_Potion, 22, killedEnemy.hitEpicenter, 50)
        ITEM_LIST.append(newItem)

def ITEM_COLLISION_CONTROL():

    itemIndex = 0

    for item in ITEM_LIST:

        item.drawItem()

        PlayerItemCollide = COLLISION_CHECK(Player1.hitEpicenter, item.hitEpicenter, Player1.hitBox, item.hitBox)
        if PlayerItemCollide:
            item.applyEffect()
            ITEM_LIST.pop(itemIndex)

        item.spawnDuration -= 1
        if item.spawnDuration <= 0:
            ITEM_LIST.pop(itemIndex)

        itemIndex += 1

