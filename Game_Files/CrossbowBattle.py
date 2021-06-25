
# Import Files:
import math
import random

from Game_Files.General_Game_Functions import *
from Game_Files.Arrows_CLASS import *
from Game_Files.HotBar_CLASS import *


HotBar = DoublyLinkedList()
InitialSelect = IronArrow( "Iron_Arrows", Iron_Arrow, 24, 4, 0, Player1.playerAngle )
# Initialize Item Slots with the first slot containing Iron Arrows:
HotBar.append( InitialSelect, 1 )
HotBar.append( None, 2 )
HotBar.append( None, 3 )
HotBar.append( None, 4 )

selectedArrows = [InitialSelect, None, None, None]



def MAIN_MENU():

    FONT = pygame.font.SysFont( "Times New Roman, Arial", 100)
    Play_TEXT = FONT.render( "Play", True, RED )
    Help_TEXT = FONT.render( "Help", True, RED )
    Exit_TEXT = FONT.render( "Exit", True, RED)

    EnemyCount, Countdown, firstRound = 0, 1, 1

    playBorder, helpBorder, exitBorder = False, False, False
    playClickBorder, helpClickBorder, exitClickBorder = False, False, False

    runningMainMenu, runningHelpMenu, runningGame, runningPauseMenu = True, False, False, False


    while runningMainMenu:

        screen.fill(GOLDENROD)

        pygame.draw.rect(screen, DARKGREY, [centerText(PLAY)[0], centerText(PLAY)[1], PLAY[0], PLAY[1]])
        pygame.draw.rect(screen, DARKGREY, [centerText(HELP)[0], centerText(HELP)[1] + 300, HELP[0], HELP[1]])
        pygame.draw.rect(screen, DARKGREY, [centerText(EXIT_GAME)[0], centerText(EXIT_GAME)[1] + 600, EXIT_GAME[0], EXIT_GAME[1]])

        screen.blit( Play_TEXT, ( displayWidth / 2 - Play_TEXT.get_rect().width / 2, displayHeight / 2 - Play_TEXT.get_rect().height/2 ) )
        screen.blit( Help_TEXT, ( displayWidth / 2 - Help_TEXT.get_rect().width / 2, displayHeight / 2 - Help_TEXT.get_rect().height / 2 + 300) )
        screen.blit( Exit_TEXT, ( displayWidth / 2 - Exit_TEXT.get_rect().width / 2, displayHeight / 2 - Exit_TEXT.get_rect().height / 2 + 600))

        if playBorder:
            pygame.draw.rect(screen, WHITE, [centerText(PLAY)[0], centerText(PLAY)[1], PLAY[0], PLAY[1]], 4)
        if helpBorder:
            pygame.draw.rect(screen, WHITE, [centerText(HELP)[0], centerText(HELP)[1] + 300, HELP[0], HELP[1]], 4)
        if exitBorder:
            pygame.draw.rect(screen, WHITE, [centerText(EXIT_GAME)[0], centerText(EXIT_GAME)[1] + 600, EXIT_GAME[0], EXIT_GAME[1]], 4)

        if playClickBorder:
            pygame.draw.rect(screen, RED, [centerText(PLAY)[0], centerText(PLAY)[1], PLAY[0], PLAY[1]], 8)
        if helpClickBorder:
            pygame.draw.rect(screen, RED, [centerText(HELP)[0], centerText(HELP)[1] + 300, HELP[0], HELP[1]], 8)
        if exitClickBorder:
            pygame.draw.rect(screen, RED, [centerText(EXIT_GAME)[0], centerText(EXIT_GAME)[1] + 600, EXIT_GAME[0], EXIT_GAME[1]], 8)


        if runningGame or runningPauseMenu:
            GAMEPLAY(EnemyCount, Countdown, firstRound)
            runningGame = False

        if runningHelpMenu:
            HELP_MENU()
            runningHelpMenu = False


        for event in pygame.event.get():
            mousePos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if (centerText(PLAY)[0] <= mousePos[0] <= centerText(PLAY)[0] + PLAY[0] and centerText(PLAY)[1] <=
                    mousePos[1] <= centerText(PLAY)[1] + PLAY[1]):
                playBorder = True
            else:
                playBorder = False

            if (centerText(HELP)[0] <= mousePos[0] <= centerText(HELP)[0] + HELP[0] and centerText(HELP)[1] + 300 <=
                    mousePos[1] <= centerText(HELP)[1] + HELP[1] + 300):
                helpBorder = True
            else:
                helpBorder = False

            if (centerText(EXIT_GAME)[0] <= mousePos[0] <= centerText(EXIT_GAME)[0] + EXIT_GAME[0] and
                    centerText(EXIT_GAME)[1] + 600 <=
                    mousePos[1] <= centerText(EXIT_GAME)[1] + EXIT_GAME[1] + 600):
                exitBorder = True
            else:
                exitBorder = False


            if event.type == MOUSEBUTTONDOWN:

                if (centerText(PLAY)[0] <= mousePos[0] <= centerText(PLAY)[0] + PLAY[0] and centerText(PLAY)[1] <=
                        mousePos[1] <= centerText(PLAY)[1] + PLAY[1]):
                    playClickBorder = True

                if (centerText(HELP)[0] <= mousePos[0] <= centerText(HELP)[0] + HELP[0] and centerText(HELP)[1] + 300 <=
                        mousePos[1] <= centerText(HELP)[1] + HELP[1] + 300):
                    helpClickBorder = True

                if (centerText(EXIT_GAME)[0] <= mousePos[0] <= centerText(EXIT_GAME)[0] + EXIT_GAME[0] and centerText(EXIT_GAME)[1] + 600 <=
                        mousePos[1] <= centerText(EXIT_GAME)[1] + EXIT_GAME[1] + 600):
                    exitClickBorder = True

            if event.type == MOUSEBUTTONUP:
                playClickBorder = False
                helpClickBorder = False
                exitClickBorder = False
                mousePos = pygame.mouse.get_pos()

                if (centerText(PLAY)[0] <= mousePos[0] <= centerText(PLAY)[0] + PLAY[0] and centerText(PLAY)[1] <=
                        mousePos[1] <= centerText(PLAY)[1] + PLAY[1]):
                    runningGame = True
                    RESET()

                if (centerText(HELP)[0] <= mousePos[0] <= centerText(HELP)[0] + HELP[0] and centerText(HELP)[1] + 300 <=
                        mousePos[1] <= centerText(HELP)[1] + HELP[1] + 300):
                    runningHelpMenu = True

                if (centerText(EXIT_GAME)[0] <= mousePos[0] <= centerText(EXIT_GAME)[0] + EXIT_GAME[0] and centerText(EXIT_GAME)[1] + 600 <=
                        mousePos[1] <= centerText(EXIT_GAME)[1] + EXIT_GAME[1] + 600):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(120)


def GAMEPLAY(EnemyCount, CountDownSet, currentRound):

    runningGame = True
    runningPauseMenu = False
    restartGame = False
    runningArmoryMenu = False

    move = [False, False, False, False]
    Shooting = False
    ShootTimer = 0

    beginRound = True
    ROUND_COUNTER = currentRound
    roundBufferTimer = 75

    enemySpawnTimer = 10
    Countdown = CountDownSet
    MaximumEnemies = 1


    currentlySelectedItemSlot = HotBar.head # Initialized at ItemSlot 1
    selectedHotBarArrows = selectedArrows

    while runningGame:

        screen.fill(0)
        screen.blit(highResBackground, (0, 0))

        selectedArrow = currentlySelectedItemSlot.CURRENT_ARROW

        if beginRound:
            DISPLAY_WAVE(ROUND_COUNTER)
            Countdown = CountDownSet
            move = [False, False, False, False]
            beginRound = False

        if runningArmoryMenu:
            x = ARMORY_MENU(selectedHotBarArrows)
            runningGame = x[0]
            runningArmoryMenu = x[1]
            selectedHotBarArrows = x[2]

            beginRound = True

        if runningPauseMenu:
            y = PAUSE_MENU()
            runningGame = y[0]
            runningPauseMenu = y[1]

        if EnemyCount == MaximumEnemies:  # Nulls enemy spawn countdown as soon as all enemies have been spawned
            Countdown = 0
        if len(ENEMY_LIST) == 0 and EnemyCount == MaximumEnemies:  # Executes next round logic once all enemies are killed
            roundBufferTimer -= 1
            if roundBufferTimer == 0:
                roundBufferTimer = 75
                EnemyCount = 0
                ROUND_COUNTER += 1
                runningArmoryMenu = True


        # PLAYER, HOTBAR, ENEMY & ARROW CONTROL:w
        Player1.drawPlayer() # Draws Player
        DRAW_GAMEPLAY_HOTBAR(selectedHotBarArrows, currentlySelectedItemSlot)
        for currentArrow in ARROW_LIST:
            currentArrow.Basic_DrawArrow()
            currentArrow.Basic_MoveArrow()

        if enemySpawnTimer <= 0:
            SpawnLocation = generateEnemySpawnCoordinates()
            if len(ENEMY_LIST) < 10:
                ENEMY_LIST.append(generateEnemy(SpawnLocation)) # Adds an enemy to the list
            EnemyCount += 1
            enemySpawnTimer = 100
        elif enemySpawnTimer != 0:
            enemySpawnTimer -= Countdown

        playerDied = COLLISION_CONTROL()
        ITEM_COLLISION_CONTROL()

        # HUD CONTROL:
        pygame.draw.rect(screen, DARKGREY, [0, 0, displayWidth, 80]) # Draws grey rectangle at top of screen
        Player1.updateHealthBar()  # Updates player's health bar
        FONT = pygame.font.SysFont("Times New Roman, Ariel", 50)
        PlayerScore_TEXT = FONT.render("Score: " + str(Player1.playerScore), True, WHITE)
        PlayerGold_TEXT = FONT.render("Gold: " + str(Player1.INVENTORY.get('Gold')), True, WHITE)
        screen.blit( PlayerScore_TEXT, ( displayWidth - 250, 15 ) )
        screen.blit( PlayerGold_TEXT, ( displayWidth - 750, 15 ) )


        # Player Death Logic:
        if playerDied:
            DRAW_GAMEOVER() # Draws 'You Died'
            z = GAMEOVER_MENU() # Runs the Game Over Menu
            runningGame = z[0]
            restartGame = z[1]
        if restartGame:
            RESET()
            move = [False, False, False, False]
            roundBufferTimer = 75
            Countdown = 1
            EnemyCount = 0
            ROUND_COUNTER = 1
            beginRound = True
            restartGame = False


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

                if event.key == K_e:
                    if currentlySelectedItemSlot.RIGHT is not None:
                        currentlySelectedItemSlot = currentlySelectedItemSlot.RIGHT
                if event.key == K_q:
                    if currentlySelectedItemSlot.LEFT is not None:
                        currentlySelectedItemSlot = currentlySelectedItemSlot.LEFT
                if event.key == K_l:
                    print(str( currentlySelectedItemSlot.slotNum ))


                if event.key == K_ESCAPE:
                    runningPauseMenu = True


                # TEST KEYS:
                if event.key == K_c:
                    Player1.getHealth(25)
                if event.key == K_v:
                    Player1.getDamage(30)
                if event.key == K_r:
                    ARROW_LIST.clear()
                if event.key == K_f:
                    ENEMY_LIST.clear()
                if event.key == K_x:
                    SpawnLocation = generateEnemySpawnCoordinates()
                    ENEMY_LIST.append(generateEnemy(SpawnLocation))


            if event.type == pygame.KEYUP:
                if event.key == K_w:
                    move[0] = False
                elif event.key == K_a:
                    move[2] = False
                elif event.key == K_s:
                    move[1] = False
                elif event.key == K_d:
                    move[3] = False

            if event.type == MOUSEBUTTONDOWN:
                Shooting = True
            if event.type == MOUSEBUTTONUP:
                Shooting = False

        if move[0]:
            Player1.spawnPos[1] += -Player1.playerSpeed
        elif move[1]:
            Player1.spawnPos[1] += Player1.playerSpeed
        if move[2]:
            Player1.spawnPos[0] += -Player1.playerSpeed
        elif move[3]:
            Player1.spawnPos[0] += Player1.playerSpeed

        if Player1.spawnPos[0] <= 0:
            move[2] = False
        if Player1.spawnPos[1] <= 80:
            move[0] = False
        if Player1.spawnPos[0] >= displayWidth:
            move[3] = False
        if Player1.spawnPos[1] >= displayHeight:
            move[1] = False

        if Shooting:
            if ShootTimer == 0:
                selectedArrow = SHOOT_CONTROL(selectedArrow)
                ShootTimer = 15
        if ShootTimer != 0:
            ShootTimer -= 1

        pygame.display.update()
        clock.tick(60)


def ARMORY_MENU(selectedHotBar):

    runningGame, runningArmoryMenu = True, True
    selectedHotBarArrows = selectedHotBar


    # Button Border Control Booleans:
    buyBorder, buyAvailableBorder, buyClickedBorder = False, False, False
    sellBorder, sellAvailableBorder, sellClickedBorder = False, False, False
    equipBorder, equipAvailableBorder, equipClickedBorder = False, False, False

    hotbarAvailableBorder = False
    hotbarBorder2, hotbarBorder3, hotbarBorder4 = False, False, False
    hotbarClickedBorder2, hotbarClickedBorder3, hotbarClickedBorder4 = False, False, False

    continueBorder, continueClickedBorder = False, False

    HIGHLIGHT = 8
    arrowOneBorder, arrowTwoBorder, arrowThreeBorder, arrowFourBorder = False, False, False, False
    arrowOneClickedBorder, arrowTwoClickedBorder, arrowThreeClickedBorder, arrowFourClickedBorder = False, False, False, False



    SELECTED = None

    while runningArmoryMenu:
        screen.fill(DARKORANGE)

        # HotBar:
        DRAW_ARMORY_HOTBAR(selectedHotBarArrows) # Draw Arrows in HotBar

        # Arrow Buttons:
        DRAW_ARROW_BUTTONS()

        # 'Buy' Button:
        pygame.draw.rect( screen, BROWN, [BUY_BUTTON_COOR[0], BUY_BUTTON_COOR[1], BUY_BUTTON[0], BUY_BUTTON[1]] )
        pygame.draw.rect( screen, DARKGREY, [BUY_BUTTON_COOR[0], BUY_BUTTON_COOR[1], BUY_BUTTON[0], BUY_BUTTON[1]], 4 )
        screen.blit( Buy_TEXT, ( BUY_BUTTON_COOR[0] + BUY_BUTTON[0]/2 - Buy_TEXT.get_rect().width/2, BUY_BUTTON_COOR[1] + BUY_BUTTON[1]/2 - Buy_TEXT.get_rect().height/2 ) )

        # 'Sell' Button:
        pygame.draw.rect(screen, BROWN, [SELL_BUTTON_COOR[0], SELL_BUTTON_COOR[1], EQUIP_BUTTON[0], EQUIP_BUTTON[1]])
        pygame.draw.rect(screen, DARKGREY, [SELL_BUTTON_COOR[0], SELL_BUTTON_COOR[1], EQUIP_BUTTON[0], EQUIP_BUTTON[1]], 4)
        screen.blit(Sell_TEXT, (SELL_BUTTON_COOR[0] + EQUIP_BUTTON[0] / 2 - Sell_TEXT.get_rect().width / 2,
                                SELL_BUTTON_COOR[1] + EQUIP_BUTTON[1] / 2 - Sell_TEXT.get_rect().height / 2))

        # 'Equip' Button:
        pygame.draw.rect(screen, BROWN, [EQUIP_BUTTON_COOR[0], EQUIP_BUTTON_COOR[1], EQUIP_BUTTON[0], EQUIP_BUTTON[1]])
        pygame.draw.rect(screen, DARKGREY, [EQUIP_BUTTON_COOR[0], EQUIP_BUTTON_COOR[1], EQUIP_BUTTON[0], EQUIP_BUTTON[1]], 4)
        screen.blit(Equip_TEXT, (EQUIP_BUTTON_COOR[0] + EQUIP_BUTTON[0] / 2 - Equip_TEXT.get_rect().width / 2,
                                 EQUIP_BUTTON_COOR[1] + EQUIP_BUTTON[1] / 2 - Equip_TEXT.get_rect().height / 2))

        # 'Continue' Button:
        pygame.draw.rect(screen, DARKGREY, [CONTINUE_COOR[0], CONTINUE_COOR[1], CONTINUE[0], CONTINUE[1]])
        pygame.draw.rect(screen, BLACK, [CONTINUE_COOR[0], CONTINUE_COOR[1], CONTINUE[0], CONTINUE[1]], 4)
        screen.blit(Continue_TEXT, (Continue_TEXT_COOR[0], Continue_TEXT_COOR[1]))





        # Buy Button Borders:
        if buyAvailableBorder:
            pygame.draw.rect(screen, LIGHTBLUE, [BUY_BUTTON_COOR[0], BUY_BUTTON_COOR[1], BUY_BUTTON[0], BUY_BUTTON[1]], 4)
        if buyBorder:
            pygame.draw.rect(screen, WHITE, [BUY_BUTTON_COOR[0], BUY_BUTTON_COOR[1], BUY_BUTTON[0], BUY_BUTTON[1]], 4)
        if buyClickedBorder:
            pygame.draw.rect(screen, YELLOW, [BUY_BUTTON_COOR[0], BUY_BUTTON_COOR[1], BUY_BUTTON[0], BUY_BUTTON[1]], 8)

        # Sell Button Borders:
        if sellAvailableBorder:
            pygame.draw.rect(screen, LIGHTBLUE, [SELL_BUTTON_COOR[0], SELL_BUTTON_COOR[1], EQUIP_BUTTON[0], EQUIP_BUTTON[1]], 4)
        if sellBorder:
            pygame.draw.rect(screen, WHITE, [SELL_BUTTON_COOR[0], SELL_BUTTON_COOR[1], EQUIP_BUTTON[0], EQUIP_BUTTON[1]], 4)
        if sellClickedBorder:
            pygame.draw.rect(screen, YELLOW, [SELL_BUTTON_COOR[0], SELL_BUTTON_COOR[1], EQUIP_BUTTON[0], EQUIP_BUTTON[1]], 8)

        # Equip Button Borders:

        if equipAvailableBorder:
            pygame.draw.rect(screen, LIGHTBLUE, [EQUIP_BUTTON_COOR[0], EQUIP_BUTTON_COOR[1], EQUIP_BUTTON[0], EQUIP_BUTTON[1]], 4)
        if equipBorder:
            pygame.draw.rect(screen, WHITE, [EQUIP_BUTTON_COOR[0], EQUIP_BUTTON_COOR[1], EQUIP_BUTTON[0], EQUIP_BUTTON[1]], 4)
        if equipClickedBorder:
            pygame.draw.rect(screen, YELLOW, [EQUIP_BUTTON_COOR[0], EQUIP_BUTTON_COOR[1], EQUIP_BUTTON[0], EQUIP_BUTTON[1]], 8)

        # Continue Button Borders:
        if continueBorder:
            pygame.draw.rect(screen, WHITE, [CONTINUE_COOR[0], CONTINUE_COOR[1], CONTINUE[0], CONTINUE[1]], 4)
        if continueClickedBorder:
            pygame.draw.rect(screen, RED, [CONTINUE_COOR[0], CONTINUE_COOR[1], CONTINUE[0], CONTINUE[1]], 8)

        # Arrow Button Borders:
        if arrowOneBorder:
            pygame.draw.rect(screen, WHITE, [ARROW_BUTTON_COOR[0], ARROW_BUTTON_COOR[1], ARROW_BUTTON[0], ARROW_BUTTON[1]], HIGHLIGHT)
        if arrowTwoBorder:
            pygame.draw.rect(screen, WHITE, [ARROW_BUTTON_COOR[0] + 400, ARROW_BUTTON_COOR[1], ARROW_BUTTON[0], ARROW_BUTTON[1]], HIGHLIGHT)
        if arrowThreeBorder:
            pygame.draw.rect( screen, WHITE, [ARROW_BUTTON_COOR[0] + 800, ARROW_BUTTON_COOR[1], ARROW_BUTTON[0], ARROW_BUTTON[1]], HIGHLIGHT )
        if arrowFourBorder:
            pygame.draw.rect( screen, WHITE, [ARROW_BUTTON_COOR[0], ARROW_BUTTON_COOR[1] + 300, ARROW_BUTTON[0], ARROW_BUTTON[1]], HIGHLIGHT )

        if arrowOneClickedBorder:
            pygame.draw.rect(screen, YELLOW, [ARROW_BUTTON_COOR[0], ARROW_BUTTON_COOR[1], ARROW_BUTTON[0], ARROW_BUTTON[1]], HIGHLIGHT)
        if arrowTwoClickedBorder:
            pygame.draw.rect(screen, YELLOW, [ARROW_BUTTON_COOR[0] + 400, ARROW_BUTTON_COOR[1], ARROW_BUTTON[0], ARROW_BUTTON[1]], HIGHLIGHT)
        if arrowThreeClickedBorder:
            pygame.draw.rect(screen, YELLOW, [ARROW_BUTTON_COOR[0] + 800, ARROW_BUTTON_COOR[1], ARROW_BUTTON[0], ARROW_BUTTON[1]], HIGHLIGHT)
        if arrowFourClickedBorder:
            pygame.draw.rect(screen, YELLOW, [ARROW_BUTTON_COOR[0], ARROW_BUTTON_COOR[1] + 300, ARROW_BUTTON[0], ARROW_BUTTON[1]], HIGHLIGHT)




        for event in pygame.event.get():
            mousePos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Arrow Button Hover Highlight:
            if ARROW_BUTTON_COOR[0] <= mousePos[0] <= ARROW_BUTTON_COOR[0] + ARROW_BUTTON[0] and ARROW_BUTTON_COOR[1] <= mousePos[1] <= ARROW_BUTTON_COOR[1] + ARROW_BUTTON[1]:  # Steel Arrows
                arrowOneBorder = True
            else:
                arrowOneBorder = False
            if ARROW_BUTTON_COOR[0] + 400 <= mousePos[0] <= ARROW_BUTTON_COOR[0] + ARROW_BUTTON[0] + 400 and ARROW_BUTTON_COOR[1] <= mousePos[1] <= ARROW_BUTTON_COOR[1] + ARROW_BUTTON[1]:  # Steel Arrows
                arrowTwoBorder = True
            else:
                arrowTwoBorder = False
            if ARROW_BUTTON_COOR[0] + 800 <= mousePos[0] <= ARROW_BUTTON_COOR[0] + ARROW_BUTTON[0] + 800 and ARROW_BUTTON_COOR[1] <= mousePos[1] <= ARROW_BUTTON_COOR[1] + ARROW_BUTTON[1]:  # Steel Arrows
                arrowThreeBorder = True
            else:
                arrowThreeBorder = False
            if ARROW_BUTTON_COOR[0] <= mousePos[0] <= ARROW_BUTTON_COOR[0] + ARROW_BUTTON[0] and ARROW_BUTTON_COOR[1] + 300 <= mousePos[1] <= ARROW_BUTTON_COOR[1] + ARROW_BUTTON[1] + 300:  # Steel Arrows
                arrowFourBorder = True
            else:
                arrowFourBorder = False


            # Buy Button Hover Highlight
            if SELECTED is not None and BUY_BUTTON_COOR[0] <= mousePos[0] <= BUY_BUTTON_COOR[0] + BUY_BUTTON[0] and \
                    BUY_BUTTON_COOR[1] <= mousePos[1] <= BUY_BUTTON_COOR[1] + BUY_BUTTON[1]:
                buyBorder = True
            else:
                buyBorder = False

            # Sell Button Hover Highlight
            if SELECTED is not None and SELL_BUTTON_COOR[0] <= mousePos[0] <= SELL_BUTTON_COOR[0] + SELL_BUTTON[0] and \
                    SELL_BUTTON_COOR[1] <= mousePos[1] <= SELL_BUTTON_COOR[1] + SELL_BUTTON[1]:
                sellBorder = True
            else:
                sellBorder = False

            # Equip Button Hover Highlight
            if SELECTED is not None and EQUIP_BUTTON_COOR[0] <= mousePos[0] <= EQUIP_BUTTON_COOR[0] + EQUIP_BUTTON[0] and \
                    EQUIP_BUTTON_COOR[1] <= mousePos[1] <= EQUIP_BUTTON_COOR[1] + EQUIP_BUTTON[1]:
                equipBorder = True
            else:
                equipBorder = False


            # Continue Button Hover Highlight
            if displayWidth - CONTINUE[0] - 50 <= mousePos[0] <= displayWidth - 50 and \
                    displayHeight - CONTINUE[1] - 50 <= mousePos[1] <= displayHeight - 50:
                continueBorder = True
            else:
                continueBorder = False



            if event.type == MOUSEBUTTONDOWN:

                # Continue Button Functionality:
                if displayWidth - CONTINUE[0] - 50 <= mousePos[0] <= displayWidth - 50 and \
                   displayHeight - CONTINUE[1] - 50 <= mousePos[1] <= displayHeight - 50:
                    continueClickedBorder = True

                # Arrow Select Button Functionality:
                if ARROW_BUTTON_COOR[0] <= mousePos[0] <= ARROW_BUTTON_COOR[0] + ARROW_BUTTON[0] and \
                        ARROW_BUTTON_COOR[1] <= mousePos[1] <= ARROW_BUTTON_COOR[1] + ARROW_BUTTON[1]: # Steel Arrows
                    SELECTED = SteelArrow("Steel_Arrows", Steel_Arrow, 24, 7, 25, Player1.playerAngle)
                    if not arrowOneClickedBorder:
                        arrowOneClickedBorder = True
                    else:
                        arrowOneClickedBorder = False
                    arrowTwoClickedBorder = False
                    arrowThreeClickedBorder = False
                    arrowFourClickedBorder = False

                    buyAvailableBorder = True
                    sellAvailableBorder = True
                    equipAvailableBorder = True
                if ARROW_BUTTON_COOR[0] + 400 <= mousePos[0] <= ARROW_BUTTON_COOR[0] + ARROW_BUTTON[0] + 400 and \
                        ARROW_BUTTON_COOR[1] <= mousePos[1] <= ARROW_BUTTON_COOR[1] + ARROW_BUTTON[1]: # Steel Arrows
                    SELECTED = HollowpointArrow("Hollowpoint_Arrows", Hollowpoint_Arrow, 24, 5, 30, Player1.playerAngle)

                    if not arrowTwoClickedBorder:
                        arrowTwoClickedBorder = True
                    else:
                        arrowTwoClickedBorder = False
                    arrowOneClickedBorder = False
                    arrowThreeClickedBorder = False
                    arrowFourClickedBorder = False

                    buyAvailableBorder = True
                    sellAvailableBorder = True
                    equipAvailableBorder = True
                if ARROW_BUTTON_COOR[0] + 800 <= mousePos[0] <= ARROW_BUTTON_COOR[0] + ARROW_BUTTON[0] + 800 and \
                        ARROW_BUTTON_COOR[1] <= mousePos[1] <= ARROW_BUTTON_COOR[1] + ARROW_BUTTON[1]: # Steel Arrows
                    SELECTED = FrostArrow("Frost_Arrows", Frost_Arrow, 35, 4, 35, Player1.playerAngle)
                    if not arrowThreeClickedBorder:
                        arrowThreeClickedBorder = True
                    else:
                        arrowThreeClickedBorder = False
                    arrowOneClickedBorder = False
                    arrowTwoClickedBorder = False
                    arrowFourClickedBorder = False

                    buyAvailableBorder = True
                    sellAvailableBorder = True
                    equipAvailableBorder = True
                if ARROW_BUTTON_COOR[0] <= mousePos[0] <= ARROW_BUTTON_COOR[0] + ARROW_BUTTON[0] and \
                        ARROW_BUTTON_COOR[1] + 300 <= mousePos[1] <= ARROW_BUTTON_COOR[1] + ARROW_BUTTON[1] + 300: # Steel Arrows
                    SELECTED = TriArrow("Tri_Arrows", Tri_Arrow, 24, 4, 35, Player1.playerAngle)
                    if not arrowFourClickedBorder:
                        arrowFourClickedBorder = True
                    else:
                        arrowFourClickedBorder = False
                    arrowOneClickedBorder = False
                    arrowTwoClickedBorder = False
                    arrowThreeClickedBorder = False

                    buyAvailableBorder = True
                    sellAvailableBorder = True
                    equipAvailableBorder = True

                # Buy Button Functionality:
                if SELECTED is not None and BUY_BUTTON_COOR[0] <= mousePos[0] <= BUY_BUTTON_COOR[0] + BUY_BUTTON[0] and \
                        BUY_BUTTON_COOR[1] <= mousePos[1] <= BUY_BUTTON_COOR[1] + BUY_BUTTON[1]:
                    buyClickedBorder = True
                    Player1.INVENTORY[SELECTED.getName()] += 50


                # Sell Button Functionality:
                if SELECTED is not None and SELL_BUTTON_COOR[0] <= mousePos[0] <= SELL_BUTTON_COOR[0] + SELL_BUTTON[0] and \
                        SELL_BUTTON_COOR[1] <= mousePos[1] <= SELL_BUTTON_COOR[1] + SELL_BUTTON[1]:
                    sellClickedBorder = True
                    if Player1.INVENTORY[SELECTED.getName()] >= 50:
                        Player1.INVENTORY[SELECTED.getName()] -= 50
                        print("New " + str(SELECTED.getName()) + " amount: " + str(Player1.INVENTORY[SELECTED.getName()]))
                    else:
                        print("Not enough arrows to sell!")


                # Equip Button Functionality:
                if SELECTED is not None and EQUIP_BUTTON_COOR[0] <= mousePos[0] <= EQUIP_BUTTON_COOR[0] + EQUIP_BUTTON[0] and \
                        EQUIP_BUTTON_COOR[1] <= mousePos[1] <= EQUIP_BUTTON_COOR[1] + EQUIP_BUTTON[1]:
                    equipClickedBorder = True




            if event.type == MOUSEBUTTONUP:

                continueClickedBorder = False

                buyClickedBorder = False
                sellClickedBorder = False

                # Equip Button Functionality:
                if SELECTED is not None and EQUIP_BUTTON_COOR[0] <= mousePos[0] <= EQUIP_BUTTON_COOR[0] + EQUIP_BUTTON[0] and \
                        EQUIP_BUTTON_COOR[1] <= mousePos[1] <= EQUIP_BUTTON_COOR[1] + EQUIP_BUTTON[1]:

                    hotbarAvailableBorder = True

                    EQUIPING = True
                    while EQUIPING:

                        # HotBar Borders:
                        if hotbarAvailableBorder:
                            pygame.draw.rect(screen, LIGHTBLUE,
                                             [ITEM_SLOT2_COOR[0], ITEM_SLOT2_COOR[1], ARMORY_ITEM_SLOT[0],
                                              ARMORY_ITEM_SLOT[1]],
                                             HOTBAR_ARMORY_BORDER)
                            pygame.draw.rect(screen, LIGHTBLUE,
                                             [ITEM_SLOT3_COOR[0], ITEM_SLOT3_COOR[1], ARMORY_ITEM_SLOT[0],
                                              ARMORY_ITEM_SLOT[1]],
                                             HOTBAR_ARMORY_BORDER)
                            pygame.draw.rect(screen, LIGHTBLUE,
                                             [ITEM_SLOT4_COOR[0], ITEM_SLOT4_COOR[1], ARMORY_ITEM_SLOT[0],
                                              ARMORY_ITEM_SLOT[1]],
                                             HOTBAR_ARMORY_BORDER)

                        if hotbarBorder2:
                            pygame.draw.rect(screen, WHITE,
                                             [ITEM_SLOT2_COOR[0], ITEM_SLOT2_COOR[1], ARMORY_ITEM_SLOT[0],
                                              ARMORY_ITEM_SLOT[1]],
                                             HOTBAR_ARMORY_BORDER)
                        if hotbarBorder3:
                            pygame.draw.rect(screen, WHITE,
                                             [ITEM_SLOT3_COOR[0], ITEM_SLOT3_COOR[1], ARMORY_ITEM_SLOT[0],
                                              ARMORY_ITEM_SLOT[1]],
                                             HOTBAR_ARMORY_BORDER)
                        if hotbarBorder4:
                            pygame.draw.rect(screen, WHITE,
                                             [ITEM_SLOT4_COOR[0], ITEM_SLOT4_COOR[1], ARMORY_ITEM_SLOT[0],
                                              ARMORY_ITEM_SLOT[1]],
                                             HOTBAR_ARMORY_BORDER)

                        if hotbarClickedBorder2:
                            pygame.draw.rect(screen, YELLOW,
                                             [ITEM_SLOT2_COOR[0], ITEM_SLOT2_COOR[1], ARMORY_ITEM_SLOT[0],
                                              ARMORY_ITEM_SLOT[1]],
                                             HOTBAR_ARMORY_BORDER)
                        if hotbarClickedBorder3:
                            pygame.draw.rect(screen, YELLOW,
                                             [ITEM_SLOT3_COOR[0], ITEM_SLOT3_COOR[1], ARMORY_ITEM_SLOT[0],
                                              ARMORY_ITEM_SLOT[1]],
                                             HOTBAR_ARMORY_BORDER)
                        if hotbarClickedBorder4:
                            pygame.draw.rect(screen, YELLOW,
                                             [ITEM_SLOT4_COOR[0], ITEM_SLOT4_COOR[1], ARMORY_ITEM_SLOT[0],
                                              ARMORY_ITEM_SLOT[1]],
                                             HOTBAR_ARMORY_BORDER)


                        for newEvent in pygame.event.get():
                            mousePos = pygame.mouse.get_pos()

                            if ITEM_SLOT2_COOR[0] <= mousePos[0] <= ITEM_SLOT2_COOR[0] + ARMORY_ITEM_SLOT[0] and \
                                    ITEM_SLOT2_COOR[1] <= mousePos[1] <= ITEM_SLOT2_COOR[1] + ARMORY_ITEM_SLOT[1]:
                                hotbarBorder2 = True
                            else:
                                hotbarBorder2 = False

                            if ITEM_SLOT3_COOR[0] <= mousePos[0] <= ITEM_SLOT3_COOR[0] + ARMORY_ITEM_SLOT[0] and \
                                    ITEM_SLOT3_COOR[1] <= mousePos[1] <= ITEM_SLOT3_COOR[1] + ARMORY_ITEM_SLOT[1]:
                                hotbarBorder3 = True
                            else:
                                hotbarBorder3 = False

                            if ITEM_SLOT4_COOR[0] <= mousePos[0] <= ITEM_SLOT4_COOR[0] + ARMORY_ITEM_SLOT[0] and \
                                    ITEM_SLOT4_COOR[1] <= mousePos[1] <= ITEM_SLOT4_COOR[1] + ARMORY_ITEM_SLOT[1]:
                                hotbarBorder4 = True
                            else:
                                hotbarBorder4 = False



                            if newEvent.type == MOUSEBUTTONDOWN:

                                if ITEM_SLOT2_COOR[0] <= mousePos[0] <= ITEM_SLOT2_COOR[0] + ARMORY_ITEM_SLOT[0] and \
                                        ITEM_SLOT2_COOR[1] <= mousePos[1] <= ITEM_SLOT2_COOR[1] + ARMORY_ITEM_SLOT[1]:
                                    hotbarClickedBorder2 = True

                                elif ITEM_SLOT3_COOR[0] <= mousePos[0] <= ITEM_SLOT3_COOR[0] + ARMORY_ITEM_SLOT[0] and \
                                        ITEM_SLOT3_COOR[1] <= mousePos[1] <= ITEM_SLOT3_COOR[1] + ARMORY_ITEM_SLOT[1]:
                                    hotbarClickedBorder3 = True

                                elif ITEM_SLOT4_COOR[0] <= mousePos[0] <= ITEM_SLOT4_COOR[0] + ARMORY_ITEM_SLOT[0] and \
                                        ITEM_SLOT4_COOR[1] <= mousePos[1] <= ITEM_SLOT4_COOR[1] + ARMORY_ITEM_SLOT[1]:
                                    hotbarClickedBorder4 = True



                            if newEvent.type == MOUSEBUTTONUP:
                                if ITEM_SLOT2_COOR[0] <= mousePos[0] <= ITEM_SLOT2_COOR[0] + ARMORY_ITEM_SLOT[0] and \
                                        ITEM_SLOT2_COOR[1] <= mousePos[1] <= ITEM_SLOT2_COOR[1] + ARMORY_ITEM_SLOT[1]:
                                    hotbarClickedBorder2 = False
                                    HotBar.updateArrow(2, SELECTED)
                                    selectedArrows[1] = SELECTED
                                    print("Equipped at Slot 2")
                                    EQUIPING, SELECTED = False, None

                                    equipClickedBorder = False
                                    equipAvailableBorder = False
                                    equipBorder = False

                                elif ITEM_SLOT3_COOR[0] <= mousePos[0] <= ITEM_SLOT3_COOR[0] + ARMORY_ITEM_SLOT[0] and \
                                        ITEM_SLOT3_COOR[1] <= mousePos[1] <= ITEM_SLOT3_COOR[1] + ARMORY_ITEM_SLOT[1]:
                                    hotbarClickedBorder3 = False
                                    HotBar.updateArrow(3, SELECTED)
                                    selectedArrows[2] = SELECTED
                                    print("Equipped at Slot 3")
                                    EQUIPING, SELECTED = False, None

                                    equipClickedBorder = False
                                    equipAvailableBorder = False
                                    equipBorder = False

                                elif ITEM_SLOT4_COOR[0] <= mousePos[0] <= ITEM_SLOT4_COOR[0] + ARMORY_ITEM_SLOT[0] and \
                                        ITEM_SLOT4_COOR[1] <= mousePos[1] <= ITEM_SLOT4_COOR[1] + ARMORY_ITEM_SLOT[1]:
                                    hotbarClickedBorder4 = False
                                    HotBar.updateArrow(4, SELECTED)
                                    selectedArrows[3] = SELECTED
                                    print("Equipped at Slot 4")
                                    EQUIPING, SELECTED = False, None

                                    equipClickedBorder = False
                                    equipAvailableBorder = False
                                    equipBorder = False


                # Continue Button Functionality:
                if displayWidth - CONTINUE[0] - 50 <= mousePos[0] <= displayWidth - 50 and \
                   displayHeight - CONTINUE[1] - 50 <= mousePos[1] <= displayHeight - 50:
                    runningGame, runningArmoryMenu = True, False



        pygame.display.update()
        clock.tick(120)

    return runningGame, runningArmoryMenu, selectedHotBarArrows


def HELP_MENU():

    FONT = pygame.font.SysFont("Times New Roman, Arial", 100)
    Back_TEXT = FONT.render("Back", True, RED)

    backBorder, backClickBorder = False, False

    runningHelpMenu = True

    while runningHelpMenu:
        screen.fill(GOLDENROD)
        screen.blit(Help_PIC, (displayWidth * 0.5 - (Help_PIC.get_rect().width / 2), 0))

        x = (((displayWidth * 0.5 - (Help_PIC.get_rect().width / 2)) / 2) - (HELP_MENU_BACK[0] / 2))
        y = (((displayWidth * 0.5 - (Help_PIC.get_rect().width / 2)) / 2) - (HELP_MENU_BACK[0] / 2))

        pygame.draw.rect(screen, DARKGREY, [x, y, HELP_MENU_BACK[0], HELP_MENU_BACK[1]])
        pygame.draw.rect(screen, BLACK, [x, y, HELP_MENU_BACK[0], HELP_MENU_BACK[1]], 4)
        screen.blit(Back_TEXT, (x + HELP_MENU_BACK[0] / 2 - Back_TEXT.get_rect().width / 2, y + HELP_MENU_BACK[1] / 2 - Back_TEXT.get_rect().height / 2))

        if backBorder:
            pygame.draw.rect(screen, WHITE, [x, y, HELP_MENU_BACK[0], HELP_MENU_BACK[1]], 4)
        if backClickBorder:
            pygame.draw.rect(screen, RED, [x, y, HELP_MENU_BACK[0], HELP_MENU_BACK[1]], 8)

        for event in pygame.event.get():
            mousePos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if x <= mousePos[0] <= x + HELP_MENU_BACK[0] and y <= mousePos[1] <= y + HELP_MENU_BACK[1]:
                backBorder = True
            else:
                backBorder = False

            if event.type == MOUSEBUTTONDOWN:
                if x <= mousePos[0] <= x + HELP_MENU_BACK[0] and y <= mousePos[1] <= y + HELP_MENU_BACK[1]:
                    backClickBorder = True

            if event.type == MOUSEBUTTONUP:
                backClickBorder = False
                if x <= mousePos[0] <= x + HELP_MENU_BACK[0] and y <= mousePos[1] <= y + HELP_MENU_BACK[1]:
                    runningHelpMenu = False

        pygame.display.update()
        clock.tick(120)


def PAUSE_MENU():

    FONT = pygame.font.SysFont("Times New Roman, Arial", 100)
    Resume_TEXT = FONT.render("Resume", True, RED)
    MainMenu_TEXT = FONT.render("Main Menu", True, RED)

    resumeBorder, mainmenuBorder = False, False
    resumeClickBorder, mainmenuClickBorder = False, False

    runningGame, runningPauseMenu = True, True

    while runningPauseMenu:
        pygame.draw.rect(screen, LIGHTGREY, [centerText(PAUSE_BACKGROUND)[0], centerText(PAUSE_BACKGROUND)[1], PAUSE_BACKGROUND[0], PAUSE_BACKGROUND[1]])
        pygame.draw.rect(screen, DARKGREY, [centerText(RESUME)[0], centerText(RESUME)[1], RESUME[0], RESUME[1]])
        pygame.draw.rect(screen, DARKGREY, [centerText(QUIT)[0], centerText(QUIT)[1] + 300, QUIT[0], QUIT[1]])
        screen.blit(Resume_TEXT, ( displayWidth / 2 - Resume_TEXT.get_rect().width / 2, displayHeight / 2 - Resume_TEXT.get_rect().height / 2))
        screen.blit(MainMenu_TEXT, ( displayWidth / 2 - MainMenu_TEXT.get_rect().width / 2, displayHeight / 2 - MainMenu_TEXT.get_rect().height / 2 + 300))

        if resumeBorder:
            pygame.draw.rect(screen, WHITE, [centerText(RESUME)[0], centerText(RESUME)[1], RESUME[0], RESUME[1]], 4)
        if mainmenuBorder:
            pygame.draw.rect(screen, WHITE, [centerText(QUIT)[0], centerText(QUIT)[1] + 300, QUIT[0], QUIT[1]], 4)
        if resumeClickBorder:
            pygame.draw.rect(screen, RED, [centerText(RESUME)[0], centerText(RESUME)[1], RESUME[0], RESUME[1]], 8)
        if mainmenuClickBorder:
            pygame.draw.rect(screen, RED, [centerText(QUIT)[0], centerText(QUIT)[1] + 300, QUIT[0], QUIT[1]], 8)

        for event in pygame.event.get():
            mousePos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            if centerText(RESUME)[0] <= mousePos[0] <= centerText(RESUME)[0] + RESUME[0] and centerText(RESUME)[1] <= mousePos[1] <= centerText(RESUME)[1] + RESUME[1]:
                resumeBorder = True
            else:
                resumeBorder = False

            if centerText(QUIT)[0] <= mousePos[0] <= centerText(QUIT)[0] + QUIT[0] and centerText(QUIT)[1] + 300 <= mousePos[1] <= centerText(QUIT)[1] + QUIT[1] + 300:
                mainmenuBorder = True
            else:
                mainmenuBorder = False


            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pass

            if event.type == MOUSEBUTTONDOWN:
                if (centerText(RESUME)[0] <= mousePos[0] <= centerText(RESUME)[0] + RESUME[0] and centerText(RESUME)[1] <=
                        mousePos[1] <= centerText(RESUME)[1] + RESUME[1]):
                    resumeClickBorder = True

                if (centerText(QUIT)[0] <= mousePos[0] <= centerText(QUIT)[0] + QUIT[0] and centerText(QUIT)[1] + 300 <=
                        mousePos[1] <= centerText(QUIT)[1] + QUIT[1] + 300):
                    mainmenuClickBorder = True

            if event.type == MOUSEBUTTONUP:
                resumeClickBorder = False
                mainmenuClickBorder = False

                if (centerText(RESUME)[0] <= mousePos[0] <= centerText(RESUME)[0] + RESUME[0] and centerText(RESUME)[1] <=
                        mousePos[1] <= centerText(RESUME)[1] + RESUME[1]):
                    runningPauseMenu = False
                    runningGame = True

                if (centerText(QUIT)[0] <= mousePos[0] <= centerText(QUIT)[0] + QUIT[0] and centerText(QUIT)[1] + 300 <=
                        mousePos[1] <= centerText(QUIT)[1] + QUIT[1] + 300):
                    runningPauseMenu = False
                    runningGame = False

        pygame.display.update()
        clock.tick(120)

    return runningGame, runningPauseMenu


def DRAW_GAMEOVER():
    FONT = pygame.font.SysFont("Times New Roman, Arial", 100)
    You_Died_TEXT = FONT.render("You Died!", True, RED)

    Player1.playerSpeed = 0
    for checkEnemy in ENEMY_LIST:
        checkEnemy.currentEnemySpeed = 0

    drawGameOver = True
    gameOverTimer = 100

    while drawGameOver:
        pygame.draw.rect( screen, DARKGREY, [ centerText(YOU_DIED_BACKGROUND)[0], centerText(YOU_DIED_BACKGROUND)[1], YOU_DIED_BACKGROUND[0], YOU_DIED_BACKGROUND[1] ] )
        screen.blit( You_Died_TEXT, ( displayWidth / 2 - You_Died_TEXT.get_rect().width / 2, displayHeight / 2 - You_Died_TEXT.get_rect().height / 2 ) )
        gameOverTimer -= 1
        if gameOverTimer == 0:
            drawGameOver = False

        pygame.display.update()
        clock.tick(120)


def GAMEOVER_MENU():

    FONT = pygame.font.SysFont("Times New Roman, Arial", 100)
    Play_Again_TEXT = FONT.render( "Play Again?", True, RED )
    Exit_TEXT = FONT.render( "Main Menu", True, RED )

    runningGameOverMenu = True
    runningGame, restartGame = True, True # Just initialized... assignment not relevant

    while runningGameOverMenu:
        screen.fill(0)
        screen.blit(highResBackground, (0, 0))

        pygame.draw.rect( screen, LIGHTGREY, [ centerText(GAMEOVER_BACKGROUND)[0], centerText(GAMEOVER_BACKGROUND)[1], GAMEOVER_BACKGROUND[0], GAMEOVER_BACKGROUND[1] ] )
        pygame.draw.rect( screen, DARKGREY, [ centerText(PLAY_AGAIN)[0], centerText(PLAY_AGAIN)[1], PLAY_AGAIN[0], PLAY_AGAIN[1] ] )
        pygame.draw.rect( screen, DARKGREY, [centerText(EXIT)[0], centerText(EXIT)[1] + 300, EXIT[0], EXIT[1] ] )
        screen.blit( Play_Again_TEXT, ( displayWidth / 2 - Play_Again_TEXT.get_rect().width / 2, displayHeight / 2 - Play_Again_TEXT.get_rect().height / 2 ) )
        screen.blit(Exit_TEXT, ( displayWidth / 2 - Exit_TEXT.get_rect().width / 2, displayHeight / 2 - Exit_TEXT.get_rect().height / 2 + 300 ) )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                if (centerText(PLAY_AGAIN)[0] <= mousePos[0] <= centerText(PLAY_AGAIN)[0] + PLAY_AGAIN[0] and
                        centerText(PLAY_AGAIN)[1] <= mousePos[1] <= centerText(PLAY_AGAIN)[1] + PLAY_AGAIN[1]):
                    runningGameOverMenu = False
                    runningGame = True
                    restartGame = True
                if (centerText(EXIT)[0] <= mousePos[0] <= centerText(EXIT)[0] + EXIT[0] and centerText(EXIT)[1] + 300 <=
                        mousePos[1] <= centerText(EXIT)[1] + EXIT[1] + 300):
                    runningGameOverMenu = False
                    runningGame = False
                    restartGame = False
                    RESET()

        pygame.display.update()
        clock.tick(120)

    return runningGame, restartGame



# Runs The game:
MAIN_MENU()