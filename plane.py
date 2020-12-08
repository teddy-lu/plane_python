# coding=utf-8
import random
import time

import pygame
from pygame.locals import *

'''
    1.搭建界面，主要完成窗口和背景图显示
    2.用来检测事件，比如按键操作
    3.使用面相过程的方式显示一个飞机，并控制其左右移动
    4.使用面向对象的方式显示飞机，以及控制左右移动
        1.实现飞机在你想要的位置显示
        2.实现按键控制飞机移动
    5.实现玩家发射子弹
        1.按下空格键发射子弹
    6.显示敌人
    7.优化代码：发射出的子弹
    8.让敌人移动
    9.让敌人发射子弹
    代码优化：抽出基类
'''


class Plane(object):
    def __init__(self, screen, imageName):
        self.screen = screen
        self.image = pygame.image.load(imageName).convert()

        self.bulletList = []

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        needDelItemList = []

        # 保存需要删除的对象
        for i in self.bulletList:
            if i.judge():
                needDelItemList.append(i)

        # 删除bulletlist中需要删除的对象
        for i in needDelItemList:
            self.bulletList.remove(i)

        # 因为needDelItemList也保存了刚刚删除的对象的引用，所以可以删除整个列表，那么
        # 整个列表中的引用就不存在了，也可以不调用下面的代码，因为needDelItemList是局部变量
        # 当这个方法的调用结束时，这个局部变量也就不存在了
        # del needDelItemList

        for bullet in self.bulletList:
            bullet.display()  # 显示子弹位置
            bullet.move()  # 子弹移动


class HeroPlane(Plane):
    def __init__(self, screen):
        super(HeroPlane, self).__init__(screen, "./plane/hero1.png")
        # 设置飞机位置
        self.x = 230
        self.y = 700

    def moveLeft(self):
        self.x -= 10

    def moveRight(self):
        self.x += 10

    def sheBullet(self):
        newBullet = Bullet(self.x, self.y, self.screen, "hero")
        self.bulletList.append(newBullet)


class EnemyPlane(Plane):
    def __init__(self, screen):
        super(EnemyPlane, self).__init__(screen, "./plane/enemy0.png")
        self.x = 0
        self.y = 0

        self.direction = "right"

    def move(self):
        # 如果碰到右边届就往左走，如果碰到左边届就往右走
        if self.direction == "right":
            self.x += 4
        elif self.direction == "left":
            self.x -= 4

        if self.x > 480 - 50:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"

    def sheBullet(self):
        num = random.randint(1, 100)
        if num == 88:
            newBullet = Bullet(self.x, self.y, self.screen, "enemy")
            self.bulletList.append(newBullet)


class Bullet(object):
    def __init__(self, x, y, screen, planeName):
        self.name = planeName
        self.screen = screen

        if self.name == "hero":
            self.x = x + 40
            self.y = y - 20
            imageName = "./plane/bullet.png"

        if self.name == "enemy":
            self.x = x + 30
            self.y = y + 30
            imageName = "./plane/bullet1.png"
        self.image = pygame.image.load(imageName).convert()

    def move(self):
        if self.name == "hero":
            self.y -= 5
        elif self.name == "enemy":
            self.y += 4

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def judge(self):
        if self.y < 0 or self.y > 852:
            return True
        else:
            return False


def key_control(heroPlane):
    # 获取事件，比如按键等
    for event in pygame.event.get():
        # 判断是否点击了退出
        if event.type == QUIT:
            print("exit")
            exit()
        # 判断是否是按下了键
        elif event.type == KEYDOWN:
            # 检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print("left")
                heroPlane.moveLeft()
            # 检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print("right")
                heroPlane.moveRight()
            # 检测按键是否是空格键
            elif event.key == K_SPACE:
                print("space")
                heroPlane.sheBullet()


def main():
    # 1 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480, 852), 0, 32)

    # 2 创建一个盒窗口大小的图片，用了填充背景
    background = pygame.image.load("./plane/background.png").convert()

    # 创建玩家飞机
    hero_plane = HeroPlane(screen)
    # 创建敌人
    enemyPlane = EnemyPlane(screen)

    # 3 把背景图片放到窗口中显示
    while True:
        # 设定显示的背景图
        screen.blit(background, (0, 0))

        hero_plane.display()

        enemyPlane.move()
        enemyPlane.display()
        enemyPlane.sheBullet()

        key_control(hero_plane)

        # 更新显示的内容
        pygame.display.update()

        # 通过延时的方式，来降低这个while循环的循环速度，从而降低了cpu占用率
        time.sleep(0.01)


if __name__ == '__main__':
    main()
