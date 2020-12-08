# coding=utf-8
import pygame
from pygame.locals import *

'''
    1.搭建界面，主要完成窗口和背景图显示
    2.用来检测事件，比如按键操作
    3.使用面相过程的方式显示一个飞机，并控制其左右移动
'''


def main():
    # 1 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480, 852), 0, 32)

    # 2 创建一个盒窗口大小的图片，用了填充背景
    background = pygame.image.load("./plane/background.png").convert()

    # 测试，用来创建一个玩家飞机的图片
    hero = pygame.image.load("./plane/hero1.png").convert()
    # 飞机的x,y坐标
    x = 0
    y = 0

    # 3 把背景图片放到窗口中显示
    while True:
        # 设定显示的背景图
        screen.blit(background, (0, 0))
        # 设定飞机的图片
        screen.blit(hero, (x, y))

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
                    x -= 5
                # 检测按键是否是d或者right
                elif event.key == K_d or event.key == K_RIGHT:
                    print("right")
                    x += 5
                # 检测按键是否是空格键
                elif event.key == K_SPACE:
                    print("space")

        # 更新显示的内容
        pygame.display.update()


if __name__ == '__main__':
    main()
