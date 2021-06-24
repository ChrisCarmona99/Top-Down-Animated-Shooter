
from Game_Files.Image_Imports import *

class Character:

    def __init__(self, image, playerSpeed, playerHealth, WeaponType):
        self.image = image
        self.playerSpeed = playerSpeed
        self.resetPlayerSpeed = playerSpeed
        self.WeaponType = WeaponType

        self.hitBox = 50
        self.hitEpicenter = 0

        self.spawnPos = [displayWidth * 0.5, displayHeight * 0.5]  # Initialized to the center of the screen
        self.currentPlayerPos = [0, 0]
        self.playerAngle = 0
        self.playerRotation = None

        self.currentHealth = playerHealth
        self.targetHealth = playerHealth
        self.maximumHealth = playerHealth
        self.healthBarLength = 800
        self.healthRatio = self.maximumHealth / self.healthBarLength
        self.healthChangeSpeed = 2.5

        self.INVENTORY = {'Gold' : 0, 'Iron_Arrows' : math.inf, 'Steel_Arrows' : 10, 'Hollowpoint_Arrows' : 5, 'Tri_Arrows' : 3, 'Frost_Arrows' : 2, 'Fire_Arrows' : 0, 'Poison_Arrows' : 0, 'Tracking_Arrows' : 0}

        self.playerScore = 0




    def getDamage(self, damageAmount):
        if self.targetHealth > 0:
            self.targetHealth -= damageAmount
        if self.targetHealth <= 0:
            self.targetHealth = 0

    def getHealth(self, healAmount):
        if self.targetHealth < self.maximumHealth:
            self.targetHealth += healAmount
        if self.targetHealth >= self.maximumHealth:
            self.targetHealth = self.maximumHealth

    def updateHealthBar(self):
        transitionWidth = 0
        transitionColor = RED

        # if self.currentHealth < self.targetHealth:
        #     self.currentHealth += self.healthChangeSpeed
        #     transitionWidth = int( (self.targetHealth - self.currentHealth) / self.healthRatio )
        #     transitionColor = GREEN
        # if self.currentHealth > self.targetHealth:
        #     self.currentHealth -= self.healthChangeSpeed
        #     transitionWidth = int( (self.targetHealth - self.currentHealth) / self.healthRatio )
        #     transitionColor = YELLOW


        if self.currentHealth > self.targetHealth:
            self.currentHealth -= self.healthChangeSpeed
            transitionWidth = int( (self.targetHealth - self.currentHealth) / self.healthRatio )
            transitionColor = YELLOW
        if self.currentHealth < self.targetHealth:
            self.currentHealth += self.healthChangeSpeed
            transitionWidth = int( (self.targetHealth - self.currentHealth) / self.healthRatio )
            transitionColor = GREEN



        healthBarRECT = pygame.Rect( 15, 15, self.currentHealth / self.healthRatio, 50 )
        transitionBarRECT = pygame.Rect( healthBarRECT.right, 15, transitionWidth, 50 )

        pygame.draw.rect( screen, RED, healthBarRECT )
        pygame.draw.rect( screen, transitionColor, transitionBarRECT )
        pygame.draw.rect( screen, WHITE, (15, 15, self.healthBarLength, 50), 4 )



    def drawPlayer(self):
        radConvert = (360 / (2 * math.pi))
        mousePos = pygame.mouse.get_pos()
        self.playerAngle = math.atan2(mousePos[1] - self.spawnPos[1], mousePos[0] - self.spawnPos[0])
        self.playerRotation = pygame.transform.rotate(player, 360 - self.playerAngle * radConvert)
        self.hitEpicenter = [ round(self.spawnPos[0]), round(self.spawnPos[1]) ]
        self.currentPlayerPos = [self.spawnPos[0] - self.playerRotation.get_rect().width / 2,
                                 self.spawnPos[1] - self.playerRotation.get_rect().height / 2]
        screen.blit(self.playerRotation, self.currentPlayerPos)

        # pygame.draw.circle(screen, GREEN, self.hitEpicenter, self.hitBox ) # DRAW HITBOX



Player1 = Character(player, 7.8, 200, "")
