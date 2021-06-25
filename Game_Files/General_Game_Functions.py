
import random

# from Game_Files.Arrows_CLASS import Arrow
from Game_Files.Arrows_CLASS import *
from Game_Files.Character_CLASS import *
from Game_Files.Enemy_CLASS import *
from Game_Files.Items_CLASS import *
import random


# GENERAL FUNCTIONS:
def centerText(imageDimensions):
    centerCoordinates = (displayWidth / 2, displayHeight / 2)
    placement = (centerCoordinates[0] - imageDimensions[0] / 2, centerCoordinates[1] - imageDimensions[1] / 2)
    return placement


def DISPLAY_WAVE(currentRound):
    currentRoundText = "Wave " + str(currentRound)
    FONT = pygame.font.SysFont("Times New Roman, Ariel", 200)
    CurrentWave_TEXT = FONT.render(currentRoundText, True, RED)

    drawWaveCount = True
    drawWaveCountTimer = 250  # Sets how long to draw 'Wave #' for each round

    while drawWaveCount:
        screen.blit(CurrentWave_TEXT, (displayWidth / 2 - CurrentWave_TEXT.get_rect().width / 2,
                                       displayHeight / 2 - CurrentWave_TEXT.get_rect().height / 2 - 300))
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


# PLAYER FUNCTIONS:
def DRAW_GAMEPLAY_HOTBAR(selectedHotBarArrows, currentlySelectedItemSlot):
    pygame.draw.rect(screen, LIGHTGREY, [ITEM_SLOT1_GAMEPLAY_COOR[0], ITEM_SLOT1_GAMEPLAY_COOR[1], GAMEPLAY_ITEM_SLOT[0], GAMEPLAY_ITEM_SLOT[1]])
    pygame.draw.rect(screen, LIGHTGREY, [ITEM_SLOT2_GAMEPLAY_COOR[0], ITEM_SLOT2_GAMEPLAY_COOR[1], GAMEPLAY_ITEM_SLOT[0], GAMEPLAY_ITEM_SLOT[1]])
    pygame.draw.rect(screen, LIGHTGREY, [ITEM_SLOT3_GAMEPLAY_COOR[0], ITEM_SLOT3_GAMEPLAY_COOR[1], GAMEPLAY_ITEM_SLOT[0], GAMEPLAY_ITEM_SLOT[1]])
    pygame.draw.rect(screen, LIGHTGREY, [ITEM_SLOT4_GAMEPLAY_COOR[0], ITEM_SLOT4_GAMEPLAY_COOR[1], GAMEPLAY_ITEM_SLOT[0], GAMEPLAY_ITEM_SLOT[1]])

    BORDER = 6
    pygame.draw.rect(screen, BLACK, [ITEM_SLOT1_GAMEPLAY_COOR[0], ITEM_SLOT1_GAMEPLAY_COOR[1], GAMEPLAY_ITEM_SLOT[0], GAMEPLAY_ITEM_SLOT[1]], BORDER)
    pygame.draw.rect(screen, BLACK, [ITEM_SLOT2_GAMEPLAY_COOR[0], ITEM_SLOT2_GAMEPLAY_COOR[1], GAMEPLAY_ITEM_SLOT[0], GAMEPLAY_ITEM_SLOT[1]], BORDER)
    pygame.draw.rect(screen, BLACK, [ITEM_SLOT3_GAMEPLAY_COOR[0], ITEM_SLOT3_GAMEPLAY_COOR[1], GAMEPLAY_ITEM_SLOT[0], GAMEPLAY_ITEM_SLOT[1]], BORDER)
    pygame.draw.rect(screen, BLACK, [ITEM_SLOT4_GAMEPLAY_COOR[0], ITEM_SLOT4_GAMEPLAY_COOR[1], GAMEPLAY_ITEM_SLOT[0], GAMEPLAY_ITEM_SLOT[1]], BORDER)

    index = 1
    for arrow in selectedHotBarArrows:
        if arrow is not None:
            if index == 1:
                screen.blit(arrowDict[arrow.getName()],
                            (ITEM_SLOT1_GAMEPLAY_COOR[0] + GAMEPLAY_ITEM_SLOT[0] / 2 - arrowDict[arrow.getName()].get_rect()[2] / 2,
                             ITEM_SLOT1_GAMEPLAY_COOR[1] + GAMEPLAY_ITEM_SLOT[1] / 2 - arrowDict[arrow.getName()].get_rect()[3] / 2))
            if index == 2:
                screen.blit(arrowDict[arrow.getName()],
                            (ITEM_SLOT2_GAMEPLAY_COOR[0] + GAMEPLAY_ITEM_SLOT[0] / 2 - arrowDict[arrow.getName()].get_rect()[2] / 2,
                             ITEM_SLOT2_GAMEPLAY_COOR[1] + GAMEPLAY_ITEM_SLOT[1] / 2 - arrowDict[arrow.getName()].get_rect()[3] / 2))
            if index == 3:
                screen.blit(arrowDict[arrow.getName()],
                            (ITEM_SLOT3_GAMEPLAY_COOR[0] + GAMEPLAY_ITEM_SLOT[0] / 2 - arrowDict[arrow.getName()].get_rect()[2] / 2,
                             ITEM_SLOT3_GAMEPLAY_COOR[1] + GAMEPLAY_ITEM_SLOT[1] / 2 - arrowDict[arrow.getName()].get_rect()[3] / 2))
            if index == 4:
                screen.blit(arrowDict[arrow.getName()],
                            (ITEM_SLOT4_GAMEPLAY_COOR[0] + GAMEPLAY_ITEM_SLOT[0] / 2 - arrowDict[arrow.getName()].get_rect()[2] / 2,
                             ITEM_SLOT4_GAMEPLAY_COOR[1] + GAMEPLAY_ITEM_SLOT[1] / 2 - arrowDict[arrow.getName()].get_rect()[3] / 2))
        index += 1

    HIGHLIGHT = 8
    if currentlySelectedItemSlot.slotNum == 1:
        pygame.draw.rect(screen, WHITE, [ITEM_SLOT1_GAMEPLAY_COOR[0], ITEM_SLOT1_GAMEPLAY_COOR[1], GAMEPLAY_ITEM_SLOT[0], GAMEPLAY_ITEM_SLOT[1]], HIGHLIGHT)
    if currentlySelectedItemSlot.slotNum == 2:
        pygame.draw.rect(screen, WHITE, [ITEM_SLOT2_GAMEPLAY_COOR[0], ITEM_SLOT2_GAMEPLAY_COOR[1], GAMEPLAY_ITEM_SLOT[0], GAMEPLAY_ITEM_SLOT[1]], HIGHLIGHT)
    if currentlySelectedItemSlot.slotNum == 3:
        pygame.draw.rect(screen, WHITE, [ITEM_SLOT3_GAMEPLAY_COOR[0], ITEM_SLOT3_GAMEPLAY_COOR[1], GAMEPLAY_ITEM_SLOT[0], GAMEPLAY_ITEM_SLOT[1]], HIGHLIGHT)
    if currentlySelectedItemSlot.slotNum == 4:
        pygame.draw.rect(screen, WHITE, [ITEM_SLOT4_GAMEPLAY_COOR[0], ITEM_SLOT4_GAMEPLAY_COOR[1], GAMEPLAY_ITEM_SLOT[0], GAMEPLAY_ITEM_SLOT[1]], HIGHLIGHT)


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
        SelectedEnemy = EnemyONE(enemy_one, 6, 10, 13, 10, ['NONE', 'Gold_1', 'Health_Potion'], [100, 25, 5],
                                 SpawnLocation[0], SpawnLocation[1])
        return SelectedEnemy
    if EnemySelect == 2:
        SelectedEnemy = EnemyTWO(enemy_two, 4.5, 25, 21, 15, ['NONE', 'Gold_1', 'Gold_2', 'Health_Potion'],
                                 [100, 50, 5, 5], SpawnLocation[0], SpawnLocation[1])
        return SelectedEnemy
    if EnemySelect == 3:
        SelectedEnemy = EnemyTHREE(enemy_three, 7.5, 45, 8, 20, ['NONE', 'Gold_1', 'Gold_2', 'Health_Potion'],
                                   [100, 25, 15, 10], SpawnLocation[0], SpawnLocation[1])
        return SelectedEnemy
    if EnemySelect == 4:
        SelectedEnemy = EnemyFOUR(enemy_four, 3.5, 65, 32, 30, ['NONE', 'Gold_2', 'Gold_3', 'Health_Potion'],
                                  [100, 50, 5, 10], SpawnLocation[0], SpawnLocation[1])
        return SelectedEnemy


# ARROW FUNCTIONS:
def SHOOT_CONTROL(selectedArrow):
    if selectedArrow is not None:
        if selectedArrow.arrowName == "Iron_Arrows":
            currentArrow = IronArrow("Iron_Arrows", Iron_Arrow, 24, 4, 0, Player1.playerAngle)  # Iron Arrows
            ARROW_LIST.append(currentArrow)

        elif selectedArrow.arrowName == "Steel_Arrows":
            currentArrow = SteelArrow("Steel_Arrows", Steel_Arrow, 24, 7, 25, Player1.playerAngle)  # Steel Arrows
            ARROW_LIST.append(currentArrow)

            Player1.INVENTORY["Steel_Arrows"] -= 1
            if Player1.INVENTORY.get("Steel_Arrows") == 0:
                selectedArrow = IronArrow("Iron_Arrows", Iron_Arrow, 24, 4, 0, Player1.playerAngle)  # reset

        elif selectedArrow.arrowName == "Hollowpoint_Arrows":
            currentArrow = HollowpointArrow("Hollowpoint_Arrows", Hollowpoint_Arrow, 24, 5, 30,
                                            Player1.playerAngle)  # Hollowpoint Arrows
            ARROW_LIST.append(currentArrow)

            Player1.INVENTORY["Hollowpoint_Arrows"] -= 1
            if Player1.INVENTORY.get("Hollowpoint_Arrows") == 0:
                selectedArrow = IronArrow("Iron_Arrows", Iron_Arrow, 24, 4, 0, Player1.playerAngle)  # reset

        elif selectedArrow.arrowName == "Tri_Arrows":
            currentArrow = TriArrow("Tri_Arrows", Tri_Arrow, 24, 4, 35, Player1.playerAngle)  # Tri Arrows
            ARROW_LIST.append(currentArrow)

            Player1.INVENTORY["Tri_Arrows"] -= 1
            if Player1.INVENTORY.get("Tri_Arrows") == 0:
                selectedArrow = IronArrow("Iron_Arrows", Iron_Arrow, 24, 4, 0, Player1.playerAngle)  # reset

        elif selectedArrow.arrowName == "Frost_Arrows":
            currentArrow = FrostArrow("Frost_Arrows", Frost_Arrow, 35, 4, 35, Player1.playerAngle)  # Frost Arrows
            ARROW_LIST.append(currentArrow)

            Player1.INVENTORY["Frost_Arrows"] -= 1
            if Player1.INVENTORY.get("Frost_Arrows") == 0:
                selectedArrow = IronArrow("Iron_Arrows", Iron_Arrow, 24, 4, 0, Player1.playerAngle)  # reset
    else:
        print("No arrow in this slot")

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


# ARMORY_FUNCTIONS:
def DRAW_ARMORY_HOTBAR(selectedHotBarArrows):
    pygame.draw.rect(screen, LIGHTGREY,
                     [ITEM_SLOT1_COOR[0], ITEM_SLOT1_COOR[1], ARMORY_ITEM_SLOT[0], ARMORY_ITEM_SLOT[1]])
    pygame.draw.rect(screen, LIGHTGREY,
                     [ITEM_SLOT2_COOR[0], ITEM_SLOT2_COOR[1], ARMORY_ITEM_SLOT[0], ARMORY_ITEM_SLOT[1]])
    pygame.draw.rect(screen, LIGHTGREY,
                     [ITEM_SLOT3_COOR[0], ITEM_SLOT3_COOR[1], ARMORY_ITEM_SLOT[0], ARMORY_ITEM_SLOT[1]])
    pygame.draw.rect(screen, LIGHTGREY,
                     [ITEM_SLOT4_COOR[0], ITEM_SLOT4_COOR[1], ARMORY_ITEM_SLOT[0], ARMORY_ITEM_SLOT[1]])


    pygame.draw.rect(screen, BLACK, [ITEM_SLOT1_COOR[0], ITEM_SLOT1_COOR[1], ARMORY_ITEM_SLOT[0], ARMORY_ITEM_SLOT[1]],
                     HOTBAR_ARMORY_BORDER)
    pygame.draw.rect(screen, BLACK, [ITEM_SLOT2_COOR[0], ITEM_SLOT2_COOR[1], ARMORY_ITEM_SLOT[0], ARMORY_ITEM_SLOT[1]],
                     HOTBAR_ARMORY_BORDER)
    pygame.draw.rect(screen, BLACK, [ITEM_SLOT3_COOR[0], ITEM_SLOT3_COOR[1], ARMORY_ITEM_SLOT[0], ARMORY_ITEM_SLOT[1]],
                     HOTBAR_ARMORY_BORDER)
    pygame.draw.rect(screen, BLACK, [ITEM_SLOT4_COOR[0], ITEM_SLOT4_COOR[1], ARMORY_ITEM_SLOT[0], ARMORY_ITEM_SLOT[1]],
                     HOTBAR_ARMORY_BORDER)

    index = 1
    for arrow in selectedHotBarArrows:
        if arrow is not None:
            if index == 1:
                screen.blit(arrowDict[arrow.getName()], (
                    ITEM_SLOT1_COOR[0] + ARMORY_ITEM_SLOT[0] / 2 - arrowDict[arrow.getName()].get_rect()[2] / 2,
                    ITEM_SLOT1_COOR[1] + ARMORY_ITEM_SLOT[1] / 2 - arrowDict[arrow.getName()].get_rect()[3] / 2))
            if index == 2:
                screen.blit(arrowDict[arrow.getName()], (
                    ITEM_SLOT2_COOR[0] + ARMORY_ITEM_SLOT[0] / 2 - arrowDict[arrow.getName()].get_rect()[2] / 2,
                    ITEM_SLOT2_COOR[1] + ARMORY_ITEM_SLOT[1] / 2 - arrowDict[arrow.getName()].get_rect()[3] / 2))
            if index == 3:
                screen.blit(arrowDict[arrow.getName()], (
                    ITEM_SLOT3_COOR[0] + ARMORY_ITEM_SLOT[0] / 2 - arrowDict[arrow.getName()].get_rect()[2] / 2,
                    ITEM_SLOT3_COOR[1] + ARMORY_ITEM_SLOT[1] / 2 - arrowDict[arrow.getName()].get_rect()[3] / 2))
            if index == 4:
                screen.blit(arrowDict[arrow.getName()], (
                    ITEM_SLOT4_COOR[0] + ARMORY_ITEM_SLOT[0] / 2 - arrowDict[arrow.getName()].get_rect()[2] / 2,
                    ITEM_SLOT4_COOR[1] + ARMORY_ITEM_SLOT[1] / 2 - arrowDict[arrow.getName()].get_rect()[3] / 2))
        index += 1


def DRAW_ARROW_BUTTONS():

    # Buy Buttons & Outlines:
    pygame.draw.rect( screen, LIGHTGREY, [ARROW_BUTTON_COOR[0], ARROW_BUTTON_COOR[1], ARROW_BUTTON[0], ARROW_BUTTON[1]] )
    pygame.draw.rect( screen, LIGHTGREY, [ARROW_BUTTON_COOR[0] + 400, ARROW_BUTTON_COOR[1], ARROW_BUTTON[0], ARROW_BUTTON[1]] )
    pygame.draw.rect( screen, LIGHTGREY, [ARROW_BUTTON_COOR[0] + 800, ARROW_BUTTON_COOR[1], ARROW_BUTTON[0], ARROW_BUTTON[1]] )
    pygame.draw.rect( screen, LIGHTGREY, [ARROW_BUTTON_COOR[0], ARROW_BUTTON_COOR[1] + 300, ARROW_BUTTON[0], ARROW_BUTTON[1]] )
    pygame.draw.rect( screen, LIGHTGREY, [ARROW_BUTTON_COOR[0] + 400, ARROW_BUTTON_COOR[1] + 300, ARROW_BUTTON[0], ARROW_BUTTON[1]] )
    pygame.draw.rect( screen, LIGHTGREY, [ARROW_BUTTON_COOR[0] + 800, ARROW_BUTTON_COOR[1] + 300, ARROW_BUTTON[0], ARROW_BUTTON[1]] )

    BORDER = 8
    pygame.draw.rect( screen, DARKGREY, [ARROW_BUTTON_COOR[0], ARROW_BUTTON_COOR[1], ARROW_BUTTON[0], ARROW_BUTTON[1]], BORDER )
    pygame.draw.rect( screen, DARKGREY, [ARROW_BUTTON_COOR[0] + 400, ARROW_BUTTON_COOR[1], ARROW_BUTTON[0], ARROW_BUTTON[1]], BORDER )
    pygame.draw.rect( screen, DARKGREY, [ARROW_BUTTON_COOR[0] + 800, ARROW_BUTTON_COOR[1], ARROW_BUTTON[0], ARROW_BUTTON[1]], BORDER )
    pygame.draw.rect( screen, DARKGREY, [ARROW_BUTTON_COOR[0], ARROW_BUTTON_COOR[1] + 300, ARROW_BUTTON[0], ARROW_BUTTON[1]], BORDER )
    pygame.draw.rect( screen, DARKGREY, [ARROW_BUTTON_COOR[0] + 400, ARROW_BUTTON_COOR[1] + 300, ARROW_BUTTON[0], ARROW_BUTTON[1]], BORDER )
    pygame.draw.rect( screen, DARKGREY, [ARROW_BUTTON_COOR[0] + 800, ARROW_BUTTON_COOR[1] + 300, ARROW_BUTTON[0], ARROW_BUTTON[1]], BORDER )

    # Arrow Images within Buy Buttons:
    screen.blit( Steel_Arrow_ARMORY, ( ARROW_BUTTON_COOR[0] + ARROW_BUTTON[0] / 2 - Steel_Arrow.get_rect().width / 2, ARROW_BUTTON_COOR[1] + ARROW_BUTTON[1] / 2 - Steel_Arrow.get_rect().height / 2) )  # TOP LEFT
    screen.blit( Hollowpoint_Arrow_ARMORY, ( ARROW_BUTTON_COOR[0] + ARROW_BUTTON[0] / 2 - Hollowpoint_Arrow.get_rect().width / 2 + 400, ARROW_BUTTON_COOR[1] + ARROW_BUTTON[1] / 2 - Hollowpoint_Arrow.get_rect().height / 2 ) )  # TOP MIDDLE
    screen.blit( Frost_Arrow_ARMORY, ( ARROW_BUTTON_COOR[0] + ARROW_BUTTON[0] / 2 - Frost_Arrow.get_rect().width / 2 + 800, ARROW_BUTTON_COOR[1] + ARROW_BUTTON[1] / 2 - Frost_Arrow.get_rect().height / 2 ) )  # TOP RIGHT
    screen.blit( Tri_Arrow_ARMORY, ( ARROW_BUTTON_COOR[0] + ARROW_BUTTON[0] / 2 - Tri_Arrow.get_rect().width / 2, ARROW_BUTTON_COOR[1] + ARROW_BUTTON[1] / 2 - Tri_Arrow.get_rect().height / 2 + 300 ) )  # MIDDLE LEFT

    # Arrow Names:
    screen.blit(SteelName_TEXT, (ARROW_BUTTON_COOR[0] + ARROW_BUTTON[0] / 2 - SteelName_TEXT.get_rect().width / 2, ARROW_BUTTON_COOR[1] - SteelName_TEXT.get_rect().height))
    screen.blit(HollowpointName_TEXT, (ARROW_BUTTON_COOR[0] + ARROW_BUTTON[0] / 2 - HollowpointName_TEXT.get_rect().width / 2 + 400, ARROW_BUTTON_COOR[1] - HollowpointName_TEXT.get_rect().height))
    screen.blit(FrostName_TEXT, (ARROW_BUTTON_COOR[0] + ARROW_BUTTON[0] / 2 - FrostName_TEXT.get_rect().width / 2 + 800, ARROW_BUTTON_COOR[1] - FrostName_TEXT.get_rect().height))
    screen.blit(TriName_TEXT, (ARROW_BUTTON_COOR[0] + ARROW_BUTTON[0] / 2 - TriName_TEXT.get_rect().width / 2, ARROW_BUTTON_COOR[1] - TriName_TEXT.get_rect().height + 300))

    # Arrow Quantities:
    screen.blit(BuyQuantity_TEXT, (ARROW_BUTTON_COOR[0] + ARROW_BUTTON[0] / 2 - BuyQuantity_TEXT.get_rect().width / 2, ARROW_BUTTON_COOR[1]))
    screen.blit(BuyQuantity_TEXT, (ARROW_BUTTON_COOR[0] + ARROW_BUTTON[0] / 2 - BuyQuantity_TEXT.get_rect().width / 2 + 400, ARROW_BUTTON_COOR[1]))
    screen.blit(BuyQuantity_TEXT, (ARROW_BUTTON_COOR[0] + ARROW_BUTTON[0] / 2 - BuyQuantity_TEXT.get_rect().width / 2 + 800, ARROW_BUTTON_COOR[1]))
    screen.blit(BuyQuantity_TEXT, (ARROW_BUTTON_COOR[0] + ARROW_BUTTON[0] / 2 - BuyQuantity_TEXT.get_rect().width / 2, ARROW_BUTTON_COOR[1] + 300))

    # Arrow Prices:
    screen.blit(SteelPrice_TEXT, (ARROW_BUTTON_COOR[0] + ARROW_BUTTON[0] / 2 - SteelPrice_TEXT.get_rect().width / 2, ARROW_BUTTON_COOR[1] + ARROW_BUTTON[1] - SteelPrice_TEXT.get_rect().height))
    screen.blit(HollowpointPrice_TEXT, (ARROW_BUTTON_COOR[0] + ARROW_BUTTON[0] / 2 - HollowpointPrice_TEXT.get_rect().width / 2 + 400, ARROW_BUTTON_COOR[1] + ARROW_BUTTON[1] - HollowpointPrice_TEXT.get_rect().height))
    screen.blit(FrostPrice_TEXT, (ARROW_BUTTON_COOR[0] + ARROW_BUTTON[0] / 2 - FrostPrice_TEXT.get_rect().width / 2 + 800, ARROW_BUTTON_COOR[1] + ARROW_BUTTON[1] - FrostPrice_TEXT.get_rect().height))
    screen.blit(TriPrice_TEXT, (ARROW_BUTTON_COOR[0] + ARROW_BUTTON[0] / 2 - TriPrice_TEXT.get_rect().width / 2, ARROW_BUTTON_COOR[1] + ARROW_BUTTON[1] - TriPrice_TEXT.get_rect().height + 300))
