
from Game_Files.Character_CLASS import *
from Game_Files.General_Game_Functions import *

ARROW_LIST = []
ENEMY_LIST = []
ITEM_LIST = []



class Arrow:

    def __init__(self, arrowImage, arrowSpeed, arrowDamage, arrowTrajectory):

        self.arrowImage = arrowImage
        self.arrowSpeed = arrowSpeed
        self.arrowDamage = arrowDamage

        self.hitBox = 10
        self.hitEpicenter = [0, 0]

        self.xSpawnPos = Player1.spawnPos[0]
        self.ySpawnPos = Player1.spawnPos[1]
        self.currentArrowPos = [0, 0]

        self.arrowTrajectory = arrowTrajectory

    def setArrowParameters(self, image, speed, damage):

        self.arrowImage = image
        self.arrowSpeed = speed
        self.arrowDamage = damage


    def Basic_DrawArrow(self):

        radConvert = (360 / (2 * math.pi))
        arrowAngle = self.arrowTrajectory
        arrowRotation = pygame.transform.rotate(self.arrowImage, 360 - arrowAngle * radConvert)
        self.hitEpicenter = [round(self.xSpawnPos), round(self.ySpawnPos)]
        self.currentArrowPos = [self.xSpawnPos - arrowRotation.get_rect().width / 2,
                                self.ySpawnPos - arrowRotation.get_rect().height / 2]

        screen.blit(arrowRotation, self.currentArrowPos)

        # pygame.draw.circle(screen, PURPLE, self.hitEpicenter, self.hitBox)  # DRAW HITBOX

    def Basic_MoveArrow(self):

        xMove = math.cos(self.arrowTrajectory) * self.arrowSpeed
        yMove = math.sin(self.arrowTrajectory) * self.arrowSpeed
        self.xSpawnPos += xMove
        self.ySpawnPos += yMove
        self.hitEpicenter[0] += xMove
        self.hitEpicenter[1] += yMove

        index = 0
        if self.currentArrowPos[0] < -64 or self.currentArrowPos[1] > displayWidth or self.currentArrowPos[1] < -64 or self.currentArrowPos[1] > displayHeight:
            ARROW_LIST.pop(index)


class IronArrow(Arrow):
    pass

class SteelArrow(Arrow):
    pass

class HollowpointArrow(Arrow):
    pass

class TriArrow(Arrow):
    pass

class FrostArrow(Arrow):
    pass




