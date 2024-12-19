
from Character import *

class Item:

    def __init__(self, image, hitBox, spawnPosition):
        self.image = image
        self.hitBox = hitBox

        self.hitEpicenter = spawnPosition
        self.currentPos = spawnPosition

        self.spawnDuration = 1000


    def drawItem(self):
        finalPos = [self.currentPos[0] - self.image.get_rect().width/2,
                    self.currentPos[1] - self.image.get_rect().height/2]
        screen.blit(self.image, finalPos)

        # pygame.draw.circle(screen, BLUE, self.hitEpicenter, self.hitBox)  # DRAW HITBOX


class Gold(Item):
    def __init__(self, image, hitBox, spawnPosition, goldAmount):
        super().__init__(image, hitBox, spawnPosition)
        self.goldAmount = goldAmount

    def applyEffect(self):
        Player1.INVENTORY["Gold"] += self.goldAmount


class HealthPotion(Item):
    def __init__(self, image, hitBox, spawnPosition, healthAmount):
        super().__init__(image, hitBox, spawnPosition)
        self.healthAmount = healthAmount

    def applyEffect(self):
        Player1.getHealth(self.healthAmount)
