
from Game_Files.Image_Imports import *

playerInitialPos = [displayWidth * 0.5, displayHeight * 0.5]

class Character:
    def __init__(self, image, playerSpeed, playerHealth, WeaponType):
        self.image = image
        self.playerSpeed = playerSpeed
        self.resetPlayerSpeed = playerSpeed

        self.currentHealth = playerHealth
        self.targetHealth = playerHealth
        self.maximumHealth = playerHealth
        self.healthBarLength = 800
        self.healthRatio = self.maximumHealth / self.healthBarLength
        self.healthChangeSpeed = 2.5

        self.WeaponType = WeaponType

        self.hitBox = 50
        self.hitEpicenter = 0

        self.playerScore = 0

        self.spawnPos = [displayWidth * 0.5 , displayHeight * 0.5]  # Initialized to the center of the screen
        self.currentPlayerPos = [0, 0]


    def update(self):
        self.animatedHealthBar()

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

    def animatedHealthBar(self):
        transitionWidth = 0
        transitionColor = RED

        if self.currentHealth < self.targetHealth:
            self.currentHealth += self.healthChangeSpeed
            transitionWidth = int( (self.targetHealth - self.currentHealth) / self.healthRatio )
            transitionColor = GREEN
        if self.currentHealth > self.targetHealth:
            self.currentHealth -= self.healthChangeSpeed
            transitionWidth = int( (self.targetHealth - self.currentHealth) / self.healthRatio )
            transitionColor = YELLOW

        healthBarRECT = pygame.Rect( 15, 15, self.currentHealth / self.healthRatio, 50 )
        transitionBarRECT = pygame.Rect( healthBarRECT.right, 15, transitionWidth, 50 )

        pygame.draw.rect( screen, RED, healthBarRECT )
        pygame.draw.rect( screen, transitionColor, transitionBarRECT )
        pygame.draw.rect( screen, WHITE, (15, 15, self.healthBarLength, 50), 4 )



    def playerSetup(self):
        radConvert = (360 / (2 * math.pi))
        mousePos = pygame.mouse.get_pos()
        playerAngle = math.atan2(mousePos[1] - self.spawnPos[1], mousePos[0] - self.spawnPos[0])
        playerRotation = pygame.transform.rotate(player, 360 - playerAngle * radConvert)
        self.hitEpicenter = [ round(self.spawnPos[0]), round(self.spawnPos[1]) ]
        self.currentPlayerPos = [self.spawnPos[0] - playerRotation.get_rect().width / 2,
                                 self.spawnPos[1] - playerRotation.get_rect().height / 2]
        screen.blit(playerRotation, self.currentPlayerPos)

        # pygame.draw.circle(screen, GREEN, self.hitEpicenter, self.hitBox ) # DRAW HITBOX



Player1 = Character(player, 7.5, 200, "")
