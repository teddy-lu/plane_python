# coding=utf-8
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
'''


class HeroPlane(object):
    def __init__(self, screen):
        # 设置飞机位置
        self.x = 230
        self.y = 700

        # 设置窗口
        self.screen = screen

        self.imgName = "./plane/hero1.png"

        self.image = pygame.image.load(self.imgName).convert()

        # 添加一个子弹
        self.bulletList = []

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        for bullet in self.bulletList:
            bullet.display()  # 显示子弹位置
            bullet.move()  # 子弹移动

    def moveLeft(self):
        self.x -= 10

    def moveRight(self):
        self.x += 10

    def sheBullet(self):
        newBullet = Bullet(self.x, self.y, self.screen)
        self.bulletList.append(newBullet)


class Bullet(object):
    def __init__(self, x, y, screen):
        self.x = x + 40
        self.y = y - 20
        self.screen = screen
        self.image = pygame.image.load("./plane/bullet.png").convert()

    def move(self):
        self.y -= 5

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))


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

    hero_plane = HeroPlane(screen)

    # 3 把背景图片放到窗口中显示
    while True:
        # 设定显示的背景图
        screen.blit(background, (0, 0))

        hero_plane.display()

        key_control(hero_plane)

        # 更新显示的内容
        pygame.display.update()


if __name__ == '__main__':
    main()
