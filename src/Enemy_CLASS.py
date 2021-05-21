
from Image_Imports import *
from Character_CLASS import *

class Enemy():
    def __init__(self, image, enemySpeed, enemyDamage, enemyHealth, xcor, ycor, xdimension, ydimension):
        self.image = image
        self.enemySpeed = enemySpeed
        self.enemyDamage = enemyDamage
        self.enemyHealth = enemyHealth
        self.xcor = xcor
        self.ycor = ycor
        self.xdimension = xdimension
        self.ydimension = ydimension
        self.enemyPos = (0, 0)

    def Enemy_Control(self):
        radconvert = (360 / (2 * math.pi))
        enemyAngle = math.atan2(Player1.Get_playerPos()[1] - self.ycor, Player1.Get_playerPos()[0] - self.xcor)
        #global enemyRotation
        enemyRotation = pygame.transform.rotate(self.image, 360 - enemyAngle * radconvert)
        self.enemyPos = [self.xcor - (enemyRotation.get_rect().width / 2 - 30),
                         self.ycor - (enemyRotation.get_rect().height / 2 - 30)]
        screen.blit(enemyRotation, self.enemyPos)

    def Enemy_Move(self):
        enemyAngle = math.atan2(Player1.Get_playerPos()[1] - self.ycor, Player1.Get_playerPos()[0] - self.xcor)
        xmove = math.cos(enemyAngle) * self.enemySpeed
        ymove = math.sin(enemyAngle) * self.enemySpeed
        self.xcor += xmove
        self.ycor += ymove

    def Get_enemyPos(self):
        return self.enemyPos

    def Get_enemyDamage(self):
        return self.enemyDamage

    def Get_enemyHealth(self):
        return self.enemyHealth

    def Get_enemyDimensions(self):
        x = self.xdimension
        y = self.ydimension
        enemyDimensions = (x, y)
        return enemyDimensions

    def Set_enemyHealth(self, health):
        self.enemyHealth = health

    def Get_enemyspeed(self):
        return self.enemySpeed



def Get_Enemy(SpawnLocation):
    EnemySelect = randint(1, 4)
    if EnemySelect == 1:
        SelectedEnemy = Enemy(enemy_one, 1.5, 0.3, 13, SpawnLocation[0], SpawnLocation[1], enemy_one.get_rect().width,
                              enemy_one.get_rect().height)
        return SelectedEnemy
    if EnemySelect == 2:
        SelectedEnemy = Enemy(enemy_two, 0.9, 0.5, 21, SpawnLocation[0], SpawnLocation[1], enemy_two.get_rect().width,
                              enemy_two.get_rect().height)
        return SelectedEnemy
    if EnemySelect == 3:
        SelectedEnemy = Enemy(enemy_three, 1.8, 0.2, 8, SpawnLocation[0], SpawnLocation[1],
                              enemy_three.get_rect().width - 65, enemy_three.get_rect().height)
        return SelectedEnemy
    if EnemySelect == 4:
        SelectedEnemy = Enemy(enemy_four, .65, 1, 32, SpawnLocation[0], SpawnLocation[1], enemy_four.get_rect().width,
                              enemy_four.get_rect().height)
        return SelectedEnemy
