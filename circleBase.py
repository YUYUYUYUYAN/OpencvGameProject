import random

import pygame


class Circle:    # 暂时没用上
    def __init__(self, posX, posY, surface, r=30, color=(255, 0, 255)):
        self.r = r
        self.color = color
        self.posX = posX
        self.posY = posY
        self.surface = surface

    def draw_circle(self):
        pygame.draw.circle(self.surface, self.color, [self.posX, self.posY], self.r)


class Ring:     # 暂时没用上
    def __init__(self, posX, posY, surface, r=90, color=(208, 32, 144)):
        self.r = r
        self.color = color
        self.posX = posX
        self.posY = posY
        self.surface = surface

    def draw_ring(self):
        pygame.draw.circle(self.surface, self.color, [self.posX, self.posY], self.r, 2)


class Item:             # 主要组件
    def __init__(self, surface, r=30, color=(0, 255, 0)):
        self.circleR = r
        self.ringR = 120
        self.color = color
        self.posX = 320
        self.posY = 320
        self.surface = surface
        # self.randomItemLocation()
        self.circle = Circle(self.posX, self.posY, self.surface)
        self.ring = Ring(self.posX, self.posY, self.surface)

    def randomItemLocation(self):   # 随机生成坐标
        self.posX = random.randint(100, 1000)
        self.posY = random.randint(100, 600)

    def draw_item(self):    #绘制组件
        pygame.draw.circle(self.surface, self.color, [self.posX, self.posY], self.circleR)
        pygame.draw.circle(self.surface, self.color, [self.posX, self.posY], self.ringR, 2)

    def update(self):   # 关键游戏更新进程
        if self.ringR == 30:
            self.randomItemLocation()
            self.ringR = 120
        else:
            self.ringR -= 5
