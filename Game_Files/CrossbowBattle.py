
# Import Files:
from Game_Files.General_Game_Functions import *
from Game_Files.Arrows_CLASS import *


# Initialize Button Dimensions:
PLAY = (700, 250)
HELP = (700, 250)

PAUSE_BACKGROUND = (700, 1000)
QUIT = (650, 250)
RESUME = (650, 250)

YOU_DIED_BACKGROUND = (900, 300)
GAMEOVER_BACKGROUND = (700, 1000)
PLAY_AGAIN = (650, 250)
EXIT = (650, 250)

# Initialize


def MAIN_MENU():

    FONT = pygame.font.SysFont( "Times New Roman, Arial", 100)
    Play_TEXT = FONT.render( "Play", True, RED )
    Help_TEXT = FONT.render( "Help", True, RED )

    EnemyCount = 0
    Countdown = 1
    firstRound = 1

    runningMainMenu = True
    runningGame = False
    runningPauseMenu = False

    while runningMainMenu:
        screen.fill(GOLDENROD)

        pygame.draw.rect(screen, DARKGREY, [centerText(PLAY)[0], centerText(PLAY)[1], PLAY[0], PLAY[1]])
        pygame.draw.rect(screen, DARKGREY, [centerText(HELP)[0], centerText(HELP)[1] + 300, HELP[0], HELP[1]])
        screen.blit( Play_TEXT, ( displayWidth / 2 - Play_TEXT.get_rect().width / 2, displayHeight / 2 - Play_TEXT.get_rect().height/2 ) )
        screen.blit( Help_TEXT, ( displayWidth / 2 - Help_TEXT.get_rect().width / 2, displayHeight / 2 - Help_TEXT.get_rect().height / 2 + 300) )

        if runningGame or runningPauseMenu:
            GAMEPLAY(selectedArrow, EnemyCount, Countdown, firstRound)
            runningGame = False

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
                    print("Help Menu")

        pygame.display.update()
        clock.tick(120)



def GAMEPLAY(Selected_Arrow, EnemyCount, CountDownSet, currentRound):
    runningGame = True
    runningPauseMenu = False
    restartGame = False



    move = [False, False, False, False]
    Shooting = False
    ShootTimer = 0

    beginRound = True
    ROUND_COUNTER = currentRound
    roundBufferTimer = 75

    enemySpawnTimer = 100
    Countdown = CountDownSet
    MaximumEnemies = 30

    while runningGame:

        screen.fill(0)
        screen.blit(highResBackground, (0, 0))

        if beginRound:
            DISPLAY_WAVE(ROUND_COUNTER)
            Countdown = CountDownSet
            move = [False, False, False, False]
            beginRound = False

        if runningPauseMenu:
            x = PAUSE_MENU()
            runningGame = x[0]
            runningPauseMenu = x[1]


        Player1.playerSetup()


        # Enemy Spawn Logic:
        if enemySpawnTimer <= 0:
            SpawnLocation = generateEnemySpawnCoordinates()
            if len(ENEMY_LIST) < 10: # Sets maximum amount of enemies that can be spawned at a time
                ENEMY_LIST.append(generateEnemy(SpawnLocation))  # Appends a new enemy object to our "enemyList", essentially generating a new enemy.
            EnemyCount += 1
            enemySpawnTimer = 50
        elif enemySpawnTimer != 0:
            enemySpawnTimer -= Countdown

        # End of Round Logic:
        if EnemyCount == MaximumEnemies: # Nulls enemy spawn countdown as soon as all enemies have been spawned
            Countdown = 0
        if len(ENEMY_LIST) == 0 and EnemyCount == MaximumEnemies: # Executes next round logic once all enemies are killed
            roundBufferTimer -= 1
            if roundBufferTimer == 0:
                roundBufferTimer = 75
                EnemyCount = 0
                ROUND_COUNTER += 1
                beginRound = True


        arrowControl()  # Runs Arrow CONTROL
        playerDied = arrowSelection()  # Runs Arrow HITS, returns true or false if player health == 0


        pygame.draw.rect(screen, DARKGREY, [0, 0, displayWidth, 80]) # Draws grey box at top of screen

        playerScoreText = "Score: " + str(Player1.playerScore)
        FONT = pygame.font.SysFont("Times New Roman, Ariel", 50)
        PlayerScore_TEXT = FONT.render(playerScoreText, True, WHITE)
        screen.blit( PlayerScore_TEXT, ( displayWidth - 250, 15 ) )

        Player1.update() # Updates player's health bar

        # Player Death Logic:
        if playerDied:
            DRAW_GAMEOVER() # Draws 'You Died'
            y = GAMEOVER_MENU() # Runs the Game Over Menu
            runningGame = y[0]
            restartGame = y[1]
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
                SHOOT(Selected_Arrow)
                ShootTimer = 15 # Sets the time between arrow shots... basically defines fire rate
        if ShootTimer != 0: # This if statement ensures the player can never fire off arrows faster than the defined 'ShootTimer"
            ShootTimer -= 1


        pygame.display.update()
        clock.tick(120)



def PAUSE_MENU():

    FONT = pygame.font.SysFont("Times New Roman, Arial", 100)
    Resume_TEXT = FONT.render("Resume", True, RED)
    Quit_TEXT = FONT.render("Quit", True, RED)

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
                    # RESET_GAME()

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
    Exit_TEXT = FONT.render( "Exit", True, RED )

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
