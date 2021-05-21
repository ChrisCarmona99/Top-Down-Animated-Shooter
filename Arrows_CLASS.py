
from Image_Imports import *
from Character_CLASS import *

arrows = []
enemyList = []
Dead = "You died!"

class Arrows():
    def __init__(self, arrowImage, arrowSpeed, arrowDamage):
        self.arrowImage = arrowImage
        self.arrowSpeed = arrowSpeed
        self.arrowDamage = arrowDamage

    def Get_arrowSpeed(self):
        return self.arrowSpeed

    def Get_arrowDamage(self):
        return self.arrowDamage

    def Set_ArrowAttributes(self, image, speed, damage):
        self.arrowImage = image
        self.arrowSpeed = speed
        self.damage = damage

    def Basic_Coordinates(self):
        radconvert = (360 / (2 * math.pi))
        mousePos = pygame.mouse.get_pos()
        playerAngle = math.atan2(mousePos[1] - playerInitialpos[1], mousePos[0] - playerInitialpos[0])
        playerRotation = pygame.transform.rotate(player, 360 - playerAngle * radconvert)
        playerPos = (playerInitialpos[0] - playerRotation.get_rect().width / 2,
                     playerInitialpos[1] - playerRotation.get_rect().height / 2)

        arrows.append([math.atan2(mousePos[1] - (playerInitialpos[1]), mousePos[0] - (playerInitialpos[0])),
                       math.atan2(mousePos[1] - (playerInitialpos[1]), mousePos[0] - (playerInitialpos[0])),
                       math.atan2(mousePos[1] - (playerInitialpos[1]), mousePos[0] - (playerInitialpos[0])),
                       playerPos[0] + (player.get_rect().width / 2), playerPos[1] + (player.get_rect().height / 2),
                       playerPos[0] + (player.get_rect().width / 2), playerPos[1] + (player.get_rect().height / 2),
                       playerPos[0] + (player.get_rect().width / 2), playerPos[1] + (player.get_rect().height / 2)])
    def Basic_Control(self, bullet):
        index = 0
        arrowVelx = math.cos(bullet[0]) * self.arrowSpeed
        arrowVely = math.sin(bullet[0]) * self.arrowSpeed
        bullet[3] += arrowVelx
        bullet[4] += arrowVely
        if bullet[3] < -64 or bullet[3] > displayWidth or bullet[4] < -64 or bullet[4] > displayHeigth:
            arrows.pop(index)
        for projectile in arrows:
            radconvert = (360 / (2 * math.pi))
            #global arrowGameImage
            arrowGameImage = pygame.transform.rotate(self.arrowImage, 360 - projectile[0] * radconvert)
            screen.blit(arrowGameImage, (projectile[3], projectile[4]))
    def Basic_Hit(self):
        enemyIndex = 0
        for enemy in enemyList:
            enemy.Enemy_Control()
            pos = enemy.Get_enemyPos()
            if pos != Player1.Get_playerPos():
                enemy.Enemy_Move()
            if enemy.Get_enemyPos()[0] >= Player1.Get_playerPos()[0] and enemy.Get_enemyPos()[0] <= \
                    Player1.Get_playerPos()[0] + player.get_rect().width and \
                    enemy.Get_enemyPos()[1] >= Player1.Get_playerPos()[1] and enemy.Get_enemyPos()[1] <= \
                    Player1.Get_playerPos()[1] + player.get_rect().height:
                global playerHealth
                playerHealth = playerHealth - enemy.Get_enemyDamage()
                if playerHealth <= 0:
                    print(Dead)
                    global Run_Game
                    Run_Game = False

            arrowIndex = 0
            for projectile in arrows:
                if projectile[3] >= enemy.Get_enemyPos()[0] and projectile[3] <= enemy.Get_enemyPos()[0] + \
                        enemy.Get_enemyDimensions()[0] and \
                        projectile[4] >= enemy.Get_enemyPos()[1] and projectile[4] <= enemy.Get_enemyPos()[1] + \
                        enemy.Get_enemyDimensions()[1]:
                    enemyHealth = enemy.Get_enemyHealth() - self.arrowDamage
                    arrows.pop(arrowIndex)
                    if enemyHealth <= 0:
                        enemyList.pop(enemyIndex)
                    elif enemyHealth > 0:
                        enemy.Set_enemyHealth(enemyHealth)
                arrowIndex += 1
            enemyIndex += 1

    def HollowPoint_Hit(self):
        enemyIndex = 0
        for enemy in enemyList:
            enemy.Enemy_Control()
            pos = enemy.Get_enemyPos()
            if pos != playerPos:
                enemy.Enemy_Move()
            if enemy.Get_enemyPos()[0] >= Player1.Get_playerPos()[0] and enemy.Get_enemyPos()[0] <= \
                    Player1.Get_playerPos()[0] + player.get_rect().width and \
                    enemy.Get_enemyPos()[1] >= Player1.Get_playerPos()[1] and enemy.Get_enemyPos()[1] <= \
                    Player1.Get_playerPos()[1] + player.get_rect().height:
                playerHealth = playerHealth - enemy.Get_enemyDamage()
                if playerHealth <= 0:
                    print(Dead)
                    global Run_Game
                    Run_Game = False
            arrowIndex = 0
            for projectile in arrows:
                if projectile[3] >= enemy.Get_enemyPos()[0] and projectile[3] <= enemy.Get_enemyPos()[0] + \
                        enemy.Get_enemyDimensions()[0] and \
                        projectile[4] >= enemy.Get_enemyPos()[1] and projectile[4] <= enemy.Get_enemyPos()[1] + \
                        enemy.Get_enemyDimensions()[1]:
                    enemyHealth = enemy.Get_enemyHealth() - self.arrowDamage
                    # arrows.pop(arrowIndex)
                    if enemyHealth <= 0:
                        enemyList.pop(enemyIndex)
                    elif enemyHealth > 0:
                        enemy.Set_enemyHealth(enemyHealth)
                arrowIndex += 1
            enemyIndex += 1

    def Tri_Control(self, bullet):
        index1 = 0
        index2 = 1
        index3 = 2
        arrow1Velx = math.cos(bullet[0]) * self.arrowSpeed
        arrow1Vely = math.sin(bullet[0]) * self.arrowSpeed
        arrow2Velx = math.cos(bullet[3]) * self.arrowSpeed
        arrow2Vely = math.sin(bullet[3]) * self.arrowSpeed
        arrow3Velx = math.cos(bullet[4]) * self.arrowSpeed
        arrow3Vely = math.sin(bullet[4]) * self.arrowSpeed
        bullet[3] += arrow1Velx
        bullet[4] += arrow1Vely
        bullet[5] += (arrow2Velx + (arrow2Velx / 10))
        bullet[6] += (arrow2Vely + (arrow2Velx / 10))
        bullet[7] += (arrow3Velx + (arrow3Velx / 10))
        bullet[8] += (arrow3Vely + (arrow3Velx / 10))
        if bullet[3] < -64 or bullet[3] > displayWidth or bullet[4] < -64 or bullet[4] > displayHeigth and \
                bullet[5] < -64 or bullet[5] > displayWidth or bullet[6] < -64 or bullet[6] > displayHeigth and \
                bullet[7] < -64 or bullet[7] > displayWidth or bullet[8] < -64 or bullet[8] > displayHeigth:
            arrows.pop(index1)
            arrows.pop(index2)
            arrows.pop(index3)
        for projectile in arrows:
            radconvert = (360 / (2 * math.pi))
            global arrowGameImage
            arrowGameImage1 = pygame.transform.rotate(self.arrowImage, 360 - projectile[0] * radconvert)
            arrowGameImage2 = pygame.transform.rotate(self.arrowImage, 360 - projectile[0] * radconvert)
            arrowGameImage3 = pygame.transform.rotate(self.arrowImage, 360 - projectile[0] * radconvert)
            screen.blit(arrowGameImage1, (projectile[3], projectile[4]))
            screen.blit(arrowGameImage2, (projectile[5], projectile[6]))
            screen.blit(arrowGameImage3, (projectile[7], projectile[8]))
    def Tri_Hit(self):
        enemyIndex = 0
        for enemy in enemyList:
            enemy.Enemy_Control()
            pos = enemy.Get_enemyPos()
            if pos != playerPos:
                enemy.Enemy_Move()
            if enemy.Get_enemyPos()[0] >= Player1.Get_playerPos()[0] and enemy.Get_enemyPos()[0] <= \
                    Player1.Get_playerPos()[0] + player.get_rect().width and \
                    enemy.Get_enemyPos()[1] >= Player1.Get_playerPos()[1] and enemy.Get_enemyPos()[1] <= \
                    Player1.Get_playerPos()[1] + player.get_rect().height:
                global playerHealth
                playerHealth = playerHealth - enemy.Get_enemyDamage()
                if playerHealth <= 0:
                    print(Dead)
                    global Run_Game
                    Run_Game = False
            arrowIndex = 0
            for projectile in arrows:
                if projectile[3] >= enemy.Get_enemyPos()[0] and projectile[3] <= enemy.Get_enemyPos()[0] + \
                        enemy.Get_enemyDimensions()[0] and \
                        projectile[4] >= enemy.Get_enemyPos()[1] and projectile[4] <= enemy.Get_enemyPos()[1] + \
                        enemy.Get_enemyDimensions()[1]:
                    enemyHealth = enemy.Get_enemyHealth() - self.arrowDamage
                    arrows.pop(arrowIndex)
                    if enemyHealth <= 0:
                        enemyList.pop(enemyIndex)
                    elif enemyHealth > 0:
                        enemy.Set_enemyHealth(enemyHealth)
                arrowIndex += 1
            enemyIndex += 1

    def Frost_Hit(self):
        enemyIndex = 0
        for enemy in enemyList:
            enemy.Enemy_Control()
            pos = enemy.Get_enemyPos()
            if pos != playerPos:
                enemy.Enemy_Move()
            if enemy.Get_enemyPos()[0] >= Player1.Get_playerPos()[0] and enemy.Get_enemyPos()[0] <= \
                    Player1.Get_playerPos()[0] + player.get_rect().width and \
                    enemy.Get_enemyPos()[1] >= Player1.Get_playerPos()[1] and enemy.Get_enemyPos()[1] <= \
                    Player1.Get_playerPos()[1] + player.get_rect().height:
                global playerHealth
                playerHealth = playerHealth - enemy.Get_enemyDamage()
                if playerHealth <= 0:
                    print(Dead)
                    global Run_Game
                    Run_Game = False
            arrowIndex = 0
            for projectile in arrows:
                if projectile[3] >= enemy.Get_enemyPos()[0] and projectile[3] <= enemy.Get_enemyPos()[0] + \
                        enemy.Get_enemyDimensions()[0] and \
                        projectile[4] >= enemy.Get_enemyPos()[1] and projectile[4] <= enemy.Get_enemyPos()[1] + \
                        enemy.Get_enemyDimensions()[1]:
                    enemyHealth = enemy.Get_enemyHealth() - self.arrowDamage
                    arrows.pop(arrowIndex)
                    if enemyHealth <= 0:
                        enemyList.pop(enemyIndex)
                    elif enemyHealth > 0:
                        enemy.Set_enemyHealth(enemyHealth)
                arrowIndex += 1
            enemyIndex += 1



Arrow_Type = Arrows(Basic_Arrow, 4.5, 4)
Selected_Arrow = "Basic_Arrow"

def arrowControl():
    for bullet in arrows:
        if Selected_Arrow == "Basic_Arrow" or "Steel_Arrow" or "HollowPoint_Arrow" or "Frost_Arrow":
            Arrow_Type.Basic_Control(bullet)
        elif Selected_Arrow == "Tri_Arrow":
            Arrow_Type.Tri_Control(bullet)

def arrowSelection():
    if Selected_Arrow == "Basic_Arrow" or "Steel_Arrow":
        Arrow_Type.Basic_Hit()
    elif Selected_Arrow == "HollowPoint_Arrow":
        Arrow_Type.HollowPoint_Hit()
    elif Selected_Arrow == "Tri_Arrow":
        Arrow_Type.Tri_Hit()
    elif Selected_Arrow == "Frost_Arrow":
        Arrow_Type.Frost_Hit()

def arrowAttributeSelecter(Selected_Arrow):
    if Selected_Arrow == "Basic_Arrow":
        Arrow_Type.Set_ArrowAttributes(Basic_Arrow, 4.5, 4)
    elif Selected_Arrow == "Steel_Arrow":
        Arrow_Type.Set_ArrowAttributes(Steel_Arrow, 4.5, 7)
    elif Selected_Arrow == "HollowPoint_Arrow":
        Arrow_Type.Set_ArrowAttributes(HollowPoint_Arrow, 4.5, 2)
    elif Selected_Arrow == "Tri_Arrow":
        Arrow_Type.Set_ArrowAttributes(Tri_Arrow, 4.5, 3)
    elif Selected_Arrow == "Frost_Arrow":
        Arrow_Type.Set_ArrowAttributes(Frost_Arrow, 4.5, 4)
