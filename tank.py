import pygame
from pygame.locals import *
import sys


if __name__ == '__main__':
    #游戏初始化
    pygame.init()
    #设置窗体
    pygame.display.set_mode((600,600))
    while True:
        events=pygame.event.get()
        for event in events:
            #窗体关闭
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)


