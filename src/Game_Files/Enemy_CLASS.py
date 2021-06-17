
from Game_Files.Character_CLASS import *

class Enemy:
    def __init__(self, image, enemySpeed, enemyDamage, enemyHealth, xSpawnPos, ySpawnPos):
        self.image = image

        self.enemyHealth = enemyHealth
        self.currentEnemyDamage = enemyDamage
        self.currentEnemySpeed = enemySpeed

        # Used to manipulate Enemy damage + pause after a successful hit against the player:
        self.activeDamage = enemyDamage
        self.activeSpeed = enemySpeed
        self.idleDamage = 0
        self.idleSpeed = 0
        self.idleTimer = 100

        # Defines/Initializes the hitBox and origin of the radius for the hitbox
        self.hitBox = 45 # Radius of the hitbox
        self.hitEpicenter = 0

        self.xSpawnPos = xSpawnPos
        self.ySpawnPos = ySpawnPos
        self.currentEnemyPos = [0, 0]

    def enemyControl(self):
        radConvert = (360 / (2 * math.pi))
        enemyAngle = math.atan2(Player1.spawnPos[1] - self.ySpawnPos, Player1.spawnPos[0] - self.xSpawnPos)
        enemyRotation = pygame.transform.rotate(self.image, 360 - enemyAngle * radConvert)
        self.hitEpicenter = [ round(self.xSpawnPos), round(self.ySpawnPos) ]
        self.currentEnemyPos = [self.xSpawnPos - (enemyRotation.get_rect().width / 2),
                                self.ySpawnPos - (enemyRotation.get_rect().height / 2)]
        screen.blit(enemyRotation, self.currentEnemyPos)

        # pygame.draw.circle(screen, RED, self.hitEpicenter, self.hitBox) # DRAW HITBOX


    def enemyMove(self):
        enemyAngle = math.atan2(Player1.spawnPos[1] - self.ySpawnPos, Player1.spawnPos[0] - self.xSpawnPos)
        xMove = math.cos(enemyAngle) * self.currentEnemySpeed
        yMove = math.sin(enemyAngle) * self.currentEnemySpeed
        self.xSpawnPos += xMove
        self.ySpawnPos += yMove


    def setEnemyHealth(self, health):
        self.enemyHealth = health


    def setEnemySpeed(self, newSpeed):
        self.currentEnemySpeed = newSpeed

