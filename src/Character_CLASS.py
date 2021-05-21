
from Image_Imports import *

playerInitialpos = [displayWidth * 0.5, displayHeigth * 0.5]

class Character():
    def __init__(self, image, playerSpeed, playerHealth, WeaponType):
        self.image = image
        self.playerSpeed = playerSpeed
        self.playerHealth = playerHealth
        self.WeaponType = WeaponType
        self.healthBar = healthbar

    def PlayerSetup(self):
        radconvert = (360 / (2 * math.pi))
        mousePos = pygame.mouse.get_pos()
        global playerAngle
        playerAngle = math.atan2(mousePos[1] - playerInitialpos[1], mousePos[0] - playerInitialpos[0])
        global playerRotation
        playerRotation = pygame.transform.rotate(player, 360 - playerAngle * radconvert)
        global playerPos
        playerPos = (playerInitialpos[0] - playerRotation.get_rect().width / 2,
                     playerInitialpos[1] - playerRotation.get_rect().height / 2)
        screen.blit(playerRotation, playerPos)

    def Get_playerPos(self):
        return playerPos

    def Get_PlayerHealth(self):
        return self.playerHealth



Player1 = Character(player, 3, 200, "")

playerHealth = Player1.Get_PlayerHealth()