
# Import Files:
import math
import random


from Game_Files.General_Game_Functions import *
from Game_Files.Arrows_CLASS import *


# Initialize Button Dimensions:
PLAY = (700, 250)
HELP = (700, 250)
EXIT_GAME = (700, 250)

HELP_MENU_BACK = (500, 250)

CONTINUE = (500, 150)
BUY = (150, 100)

PAUSE_BACKGROUND = (700, 1000)
RESUME = (650, 250)
QUIT = (650, 250)

YOU_DIED_BACKGROUND = (900, 300)
GAMEOVER_BACKGROUND = (700, 1000)
PLAY_AGAIN = (650, 250)
EXIT = (650, 250)



def MAIN_MENU():

    FONT = pygame.font.SysFont( "Times New Roman, Arial", 100)
    Play_TEXT = FONT.render( "Play", True, RED )
    Help_TEXT = FONT.render( "Help", True, RED )
    Exit_TEXT = FONT.render( "Exit", True, RED)

    EnemyCount = 0
    Countdown = 1
    firstRound = 1

    runningMainMenu = True
    runningHelpMenu = False
    runningGame = False
    runningPauseMenu = False


    while runningMainMenu:

        screen.fill(GOLDENROD)

        pygame.draw.rect(screen, DARKGREY, [centerText(PLAY)[0], centerText(PLAY)[1], PLAY[0], PLAY[1]])
        pygame.draw.rect(screen, DARKGREY, [centerText(HELP)[0], centerText(HELP)[1] + 300, HELP[0], HELP[1]])
        pygame.draw.rect(screen, DARKGREY, [centerText(EXIT_GAME)[0], centerText(EXIT_GAME)[1] + 600, EXIT_GAME[0], EXIT_GAME[1]])

        screen.blit( Play_TEXT, ( displayWidth / 2 - Play_TEXT.get_rect().width / 2, displayHeight / 2 - Play_TEXT.get_rect().height/2 ) )
        screen.blit( Help_TEXT, ( displayWidth / 2 - Help_TEXT.get_rect().width / 2, displayHeight / 2 - Help_TEXT.get_rect().height / 2 + 300) )
        screen.blit( Exit_TEXT, ( displayWidth / 2 - Exit_TEXT.get_rect().width / 2, displayHeight / 2 - Exit_TEXT.get_rect().height / 2 + 600))

        if runningGame or runningPauseMenu:
            GAMEPLAY(EnemyCount, Countdown, firstRound)
            runningGame = False

        if runningHelpMenu:
            HELP_MENU()
            runningHelpMenu = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
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
    runningIntermissionMenu = False

    move = [False, False, False, False]
    Shooting = False
    ShootTimer = 0

    beginRound = True
    ROUND_COUNTER = currentRound
    roundBufferTimer = 75

    enemySpawnTimer = 10
    Countdown = CountDownSet
    MaximumEnemies = 30

    selectedArrow = "Iron_Arrows" # Initialize starting arrow to the basic arrow

    while runningGame:

        screen.fill(0)
        screen.blit(highResBackground, (0, 0))

        if beginRound:
            DISPLAY_WAVE(ROUND_COUNTER)
            Countdown = CountDownSet
            move = [False, False, False, False]
            beginRound = False

        if runningIntermissionMenu:
            x = INTERMISSION_MENU()
            runningGame = x[0]
            runningIntermissionMenu = x[1]
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
                runningIntermissionMenu = True


        # PLAYER, ENEMY & ARROW CONTROL:w
        Player1.drawPlayer() # Draws Player
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

        # HUD & ITEM BAR CONTROL
        pygame.draw.rect(screen, DARKGREY, [0, 0, displayWidth, 80]) # Draws grey rectangle at top of screen
        Player1.update()  # Updates player's health bar
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

                if event.key == K_1:
                    if Player1.INVENTORY.get("Iron_Arrows") > 0:
                        selectedArrow = "Iron_Arrows"
                    else:
                        print("You don't have any Iron Arrows!")
                if event.key == K_2:
                    if Player1.INVENTORY.get("Steel_Arrows") > 0:
                        selectedArrow = "Steel_Arrows"
                    else:
                        print("You don't have any Steel Arrows!")
                if event.key == K_3:
                    if Player1.INVENTORY.get("Hollowpoint_Arrows") > 0:
                        selectedArrow = "Hollowpoint_Arrows"
                    else:
                        print("You don't have any Hollowpoint Arrows!")
                if event.key == K_4:
                    if Player1.INVENTORY.get("Tri_Arrows") > 0:
                        selectedArrow = "Tri_Arrows"
                    else:
                        print("You don't have any Tri Arrows!")
                if event.key == K_5:
                    if Player1.INVENTORY.get("Frost_Arrows") > 0:
                        selectedArrow = "Frost_Arrows"
                    else:
                        print("You don't have any Frost Arrows!")

                if event.key == K_ESCAPE:
                    runningPauseMenu = True


                # TEST KEYS:
                if event.key == K_e:
                    Player1.getHealth(25)
                if event.key == K_q:
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


def INTERMISSION_MENU():

    FONT = pygame.font.SysFont( "Times New Roman, Ariel", 100 )
    Continue_TEXT = FONT.render( "Continue", True, RED )

    runningGame = True
    runningIntermissionMenu = True

    while runningIntermissionMenu:
        screen.fill(DARKORANGE)

        CONTINUE_COOR = ( displayWidth - CONTINUE[0] - 50, displayHeight - CONTINUE[1] - 50 )
        Continue_TEXT_COOR = ( displayWidth - CONTINUE[0] / 2 - Continue_TEXT.get_rect().width / 2 - 50, displayHeight - CONTINUE[1] / 2 - Continue_TEXT.get_rect().height / 2 - 50 )
        BUY_COOR = ( 250, 500 )

        pygame.draw.rect(screen, DARKGREY, [CONTINUE_COOR[0], CONTINUE_COOR[1], CONTINUE[0], CONTINUE[1]])
        screen.blit(Continue_TEXT, ( Continue_TEXT_COOR[0], Continue_TEXT_COOR[1] ))

        pygame.draw.rect( screen, LIGHTGREY, [ BUY_COOR[0], BUY_COOR[1], BUY[0], BUY[1] ] )
        pygame.draw.rect( screen, LIGHTGREY, [ BUY_COOR[0] + 250, BUY_COOR[1], BUY[0], BUY[1] ] )
        pygame.draw.rect( screen, LIGHTGREY, [ BUY_COOR[0] + 500, BUY_COOR[1], BUY[0], BUY[1] ] )
        pygame.draw.rect(screen, LIGHTGREY, [BUY_COOR[0], BUY_COOR[1] + 200, BUY[0], BUY[1] ] )
        pygame.draw.rect(screen, LIGHTGREY, [BUY_COOR[0] + 250, BUY_COOR[1] + 200, BUY[0], BUY[1] ] )
        pygame.draw.rect(screen, LIGHTGREY, [BUY_COOR[0] + 500, BUY_COOR[1] + 200, BUY[0], BUY[1] ] )

        screen.blit( Steel_Arrow, (BUY_COOR[0] + BUY[0]/2 - Steel_Arrow.get_rect().width/2, BUY_COOR[1] + BUY[1]/2 - Steel_Arrow.get_rect().height/2) )
        screen.blit( Hollowpoint_Arrow, (BUY_COOR[0] + BUY[0]/2 - Hollowpoint_Arrow.get_rect().width/2 + 250, BUY_COOR[1] + BUY[1]/2 - Hollowpoint_Arrow.get_rect().height/2) )
        screen.blit( Frost_Arrow, (BUY_COOR[0] + BUY[0]/2 - Frost_Arrow.get_rect().width/2 + 500, BUY_COOR[1] + BUY[1]/2 - Frost_Arrow.get_rect().height/2) )
        # screen.blit(Tri_Arrow, (BUY_COOR[0] + BUY[0] / 2 - Tri_Arrow.get_rect().width / 2, BUY_COOR[1] + BUY[1] / 2 - Tri_Arrow.get_rect().height / 2 + 200))
        # screen.blit(Hollowpoint_Arrow, (BUY_COOR[0] + BUY[0] / 2 - Hollowpoint_Arrow.get_rect().width / 2 + 250, BUY_COOR[1] + BUY[1] / 2 - Hollowpoint_Arrow.get_rect().height / 2 + 200))
        screen.blit(Tri_Arrow, (BUY_COOR[0] + BUY[0] / 2 - Tri_Arrow.get_rect().width / 2, BUY_COOR[1] + BUY[1] / 2 - Tri_Arrow.get_rect().height / 2 + 200))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                if displayWidth - CONTINUE[0] - 50 <= mousePos[0] <= displayWidth - 50 and \
                   displayHeight - CONTINUE[1] - 50 <= mousePos[1] <= displayHeight - 50:
                    runningGame = True
                    runningIntermissionMenu = False

                if BUY_COOR[0] <= mousePos[0] <= BUY_COOR[0] + BUY[0] and BUY_COOR[1] <= mousePos[1] <= BUY_COOR[1] + BUY[1]: # Steel Arrows
                    Player1.INVENTORY['Steel_Arrows'] += 10
                    print("Steel Arrow Count: " + str(Player1.INVENTORY.get('Steel_Arrows')))


        pygame.display.update()
        clock.tick(120)

    return runningGame, runningIntermissionMenu


def HELP_MENU():

    FONT = pygame.font.SysFont("Times New Roman, Arial", 100)
    Back_TEXT = FONT.render("Back", True, RED)

    runningHelpMenu = True

    while runningHelpMenu:
        screen.fill(GOLDENROD)
        screen.blit(Help_PIC, (displayWidth * 0.5 - (Help_PIC.get_rect().width / 2), 0))

        x = (((displayWidth * 0.5 - (Help_PIC.get_rect().width / 2)) / 2) - (HELP_MENU_BACK[0] / 2))
        y = (((displayWidth * 0.5 - (Help_PIC.get_rect().width / 2)) / 2) - (HELP_MENU_BACK[0] / 2))

        pygame.draw.rect(screen, DARKGREY, [x, y, HELP_MENU_BACK[0], HELP_MENU_BACK[1]])
        screen.blit(Back_TEXT, (x + HELP_MENU_BACK[0] / 2 - Back_TEXT.get_rect().width / 2, y + HELP_MENU_BACK[1] / 2 - Back_TEXT.get_rect().height / 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                if x <= mousePos[0] <= x + HELP_MENU_BACK[0] and y <= mousePos[1] <= y + HELP_MENU_BACK[1]:
                    runningHelpMenu = False

        pygame.display.update()
        clock.tick(120)


def PAUSE_MENU():

    FONT = pygame.font.SysFont("Times New Roman, Arial", 100)
    Resume_TEXT = FONT.render("Resume", True, RED)
    Quit_TEXT = FONT.render("Main Menu", True, RED)

    runningGame = True
    runningPauseMenu = True

    while runningPauseMenu:
        pygame.draw.rect(screen, LIGHTGREY, [centerText(PAUSE_BACKGROUND)[0], centerText(PAUSE_BACKGROUND)[1], PAUSE_BACKGROUND[0], PAUSE_BACKGROUND[1]])
        pygame.draw.rect(screen, DARKGREY, [centerText(RESUME)[0], centerText(RESUME)[1], RESUME[0], RESUME[1]])
        pygame.draw.rect(screen, DARKGREY, [centerText(QUIT)[0], centerText(QUIT)[1] + 300, QUIT[0], QUIT[1]])
        screen.blit(Resume_TEXT, ( displayWidth / 2 - Resume_TEXT.get_rect().width / 2, displayHeight / 2 - Resume_TEXT.get_rect().height / 2))
        screen.blit(Quit_TEXT, ( displayWidth / 2 - Quit_TEXT.get_rect().width / 2, displayHeight / 2 - Quit_TEXT.get_rect().height / 2 + 300))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
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
    runningGame = True # Just initialized... assignment not relevant
    restartGame = True # Just initialized... assignment not relevant

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

# import random
# myList = ['a', 'b', 'c']
# print(random.choices(myList, weights = [10, 0, 0], k = 2))

