
from Game_Files.Character_CLASS import *
from Game_Files.General_Game_Functions import *

ARROW_LIST = []
ENEMY_LIST = []
Dead = "You died!"



class Arrow:
    def __init__(self, arrowImage, arrowSpeed, arrowDamage):

        self.arrowImage = arrowImage
        self.arrowSpeed = arrowSpeed
        self.arrowDamage = arrowDamage

        self.hitBox = 10
        self.hitEpicenter = [0, 0]


    def setArrowParameters(self, image, speed, damage):

        self.arrowImage = image
        self.arrowSpeed = speed
        self.arrowDamage = damage


    def collisionDetection(self, pos1, pos2, hitBox1, hitBox2):

        dist = math.sqrt(((pos2[0] - pos1[0]) ** 2) + ((pos2[1] - pos1[1]) ** 2))
        if dist <= (hitBox1 + hitBox2):
            return True
        else:
            return False



    def Basic_Coordinates(self):

        radConvert = (360 / (2 * math.pi))
        mousePos = pygame.mouse.get_pos()
        arrowAngle = math.atan2(mousePos[1] - Player1.spawnPos[1], mousePos[0] - Player1.spawnPos[0])
        arrowRotation = pygame.transform.rotate(self.arrowImage, 360 - arrowAngle * radConvert)
        self.hitEpicenter = [ Player1.spawnPos[0], Player1.spawnPos[1] ]
        currentArrowPos = (Player1.spawnPos[0] - arrowRotation.get_rect().width / 2,
                           Player1.spawnPos[1] - arrowRotation.get_rect().height / 2)

        ARROW_LIST.append([arrowAngle, currentArrowPos[0], currentArrowPos[1], self.hitEpicenter, self.hitBox])


    def Basic_Control(self, ARROW):

        index = 0
        arrowVelX = math.cos(ARROW[0]) * self.arrowSpeed
        arrowVelY = math.sin(ARROW[0]) * self.arrowSpeed
        ARROW[1] += arrowVelX
        ARROW[2] += arrowVelY
        ARROW[3][0] += arrowVelX
        ARROW[3][1] += arrowVelY

        if ARROW[1] < -64 or ARROW[1] > displayWidth or ARROW[2] < -64 or ARROW[2] > displayHeight:
            ARROW_LIST.pop(index)

        for currArrow in ARROW_LIST:
            radConvert = (360 / (2 * math.pi))
            arrowGameImage = pygame.transform.rotate(self.arrowImage, 360 - currArrow[0] * radConvert)

            screen.blit(arrowGameImage, (currArrow[1], currArrow[2]))

            # pygame.draw.circle( screen, PURPLE, [round(currArrow[3][0]), round(currArrow[3][1]) ], self.hitBox)


    def Basic_Hit(self):

        playerDied = False

        enemyIndex = 0
        for enemy in ENEMY_LIST:

            if enemy.currentEnemySpeed == 0:
                enemy.idleTimer -= 1
                if enemy.idleTimer == 0:
                    enemy.idleTimer = 50
                    enemy.currentEnemyDamage = enemy.activeDamage
                    enemy.currentEnemySpeed = enemy.activeSpeed

            enemy.enemyControl()
            if enemy.currentEnemyPos != Player1.spawnPos:
                enemy.enemyMove()

            # HANDLES ENEMY<->PLAYER COLLISION:
            EnemyPlayerCollide = self.collisionDetection(Player1.hitEpicenter, enemy.hitEpicenter, Player1.hitBox, enemy.hitBox)
            if EnemyPlayerCollide:
                Player1.getDamage(enemy.currentEnemyDamage)
                enemy.currentEnemySpeed = enemy.idleSpeed
                enemy.currentEnemyDamage = enemy.idleDamage

                if Player1.targetHealth <= 0:
                    playerDied = True
                    return playerDied

            # HANDLES ARROW<->ENEMY COLLISION:
            arrowIndex = 0
            for currArrow in ARROW_LIST:
                ArrowEnemyCollide = self.collisionDetection(enemy.hitEpicenter, (currArrow[3][0], currArrow[3][1]), enemy.hitBox, currArrow[4])
                if ArrowEnemyCollide:
                    enemyHealth = enemy.enemyHealth - self.arrowDamage
                    ARROW_LIST.pop(arrowIndex)
                    if enemyHealth <= 0:
                        Player1.playerScore += enemy.enemyScore
                        #print(Player1.playerScore)
                        ENEMY_LIST.pop(enemyIndex)

                    elif enemyHealth > 0:
                        enemy.setEnemyHealth(enemyHealth)
                arrowIndex += 1
            enemyIndex += 1

        return playerDied



    # def HollowPoint_Hit(self):
    #     enemyIndex = 0
    #     for enemy in ENEMY_LIST:
    #         enemy.enemyControl()
    #         pos = enemy.Get_enemyPos()
    #         if pos != Player1.Get_playerPos():
    #             enemy.enemyMove()
    #         if enemy.Get_enemyPos()[0] >= Player1.Get_playerPos()[0] and enemy.Get_enemyPos()[0] <= \
    #                 Player1.Get_playerPos()[0] + player.get_rect().width and \
    #                 enemy.Get_enemyPos()[1] >= Player1.Get_playerPos()[1] and enemy.Get_enemyPos()[1] <= \
    #                 Player1.Get_playerPos()[1] + player.get_rect().height:
    #             playerHealth = playerHealth - enemy.enemyDamage
    #             if playerHealth <= 0:
    #                 print(Dead)
    #                 global Run_Game
    #                 Run_Game = False
    #         arrowIndex = 0
    #         for projectile in ARROW_LIST:
    #             if projectile[3] >= enemy.Get_enemyPos()[0] and projectile[3] <= enemy.Get_enemyPos()[0] + \
    #                     enemy.getEnemyDimensions()[0] and \
    #                     projectile[4] >= enemy.Get_enemyPos()[1] and projectile[4] <= enemy.Get_enemyPos()[1] + \
    #                     enemy.getEnemyDimensions()[1]:
    #                 enemyHealth = enemy.getEnemyHealth() - self.arrowDamage
    #                 # arrows.pop(arrowIndex)
    #                 if enemyHealth <= 0:
    #                     ENEMY_LIST.pop(enemyIndex)
    #                 elif enemyHealth > 0:
    #                     enemy.setEnemyHealth(enemyHealth)
    #             arrowIndex += 1
    #         enemyIndex += 1
    #
    # def Tri_Hit(self):
    #     enemyIndex = 0
    #     for enemy in ENEMY_LIST:
    #         enemy.enemyControl()
    #         pos = enemy.Get_enemyPos()
    #         if pos != Player1.Get_playerPos():
    #             enemy.enemyMove()
    #         if enemy.Get_enemyPos()[0] >= Player1.Get_playerPos()[0] and enemy.Get_enemyPos()[0] <= \
    #                 Player1.Get_playerPos()[0] + player.get_rect().width and \
    #                 enemy.Get_enemyPos()[1] >= Player1.Get_playerPos()[1] and enemy.Get_enemyPos()[1] <= \
    #                 Player1.Get_playerPos()[1] + player.get_rect().height:
    #             global playerHealth
    #             playerHealth = playerHealth - enemy.enemyDamage
    #             if playerHealth <= 0:
    #                 print(Dead)
    #                 global Run_Game
    #                 Run_Game = False
    #         arrowIndex = 0
    #         for projectile in ARROW_LIST:
    #             if projectile[3] >= enemy.Get_enemyPos()[0] and projectile[3] <= enemy.Get_enemyPos()[0] + \
    #                     enemy.getEnemyDimensions()[0] and \
    #                     projectile[4] >= enemy.Get_enemyPos()[1] and projectile[4] <= enemy.Get_enemyPos()[1] + \
    #                     enemy.getEnemyDimensions()[1]:
    #                 enemyHealth = enemy.getEnemyHealth() - self.arrowDamage
    #                 ARROW_LIST.pop(arrowIndex)
    #                 if enemyHealth <= 0:
    #                     ENEMY_LIST.pop(enemyIndex)
    #                 elif enemyHealth > 0:
    #                     enemy.setEnemyHealth(enemyHealth)
    #             arrowIndex += 1
    #         enemyIndex += 1
    #
    # def Frost_Hit(self):
    #     enemyIndex = 0
    #     for enemy in ENEMY_LIST:
    #         enemy.enemyControl()
    #         pos = enemy.Get_enemyPos()
    #         if pos != Player1.Get_playerPos():
    #             enemy.enemyMove()
    #         if enemy.Get_enemyPos()[0] >= Player1.Get_playerPos()[0] and enemy.Get_enemyPos()[0] <= \
    #                 Player1.Get_playerPos()[0] + player.get_rect().width and \
    #                 enemy.Get_enemyPos()[1] >= Player1.Get_playerPos()[1] and enemy.Get_enemyPos()[1] <= \
    #                 Player1.Get_playerPos()[1] + player.get_rect().height:
    #             global playerHealth
    #             playerHealth = playerHealth - enemy.enemyDamage
    #             if playerHealth <= 0:
    #                 print(Dead)
    #                 global Run_Game
    #                 Run_Game = False
    #         arrowIndex = 0
    #         for projectile in ARROW_LIST:
    #             if projectile[3] >= enemy.Get_enemyPos()[0] and projectile[3] <= enemy.Get_enemyPos()[0] + \
    #                     enemy.getEnemyDimensions()[0] and \
    #                     projectile[4] >= enemy.Get_enemyPos()[1] and projectile[4] <= enemy.Get_enemyPos()[1] + \
    #                     enemy.getEnemyDimensions()[1]:
    #                 enemyHealth = enemy.getEnemyHealth() - self.arrowDamage
    #                 ARROW_LIST.pop(arrowIndex)
    #                 if enemyHealth <= 0:
    #                     ENEMY_LIST.pop(enemyIndex)
    #                 elif enemyHealth > 0:
    #                     enemy.setEnemyHealth(enemyHealth)
    #             arrowIndex += 1
    #         enemyIndex += 1
