import pygame
from pygame.locals import *
import sys
import time

from locals import *

if __name__ == '__main__':
    #游戏初始化
    pygame.init()
    #设置窗体
    pygame.display.set_mode((600,600))
    #FPS值
    fps=0
    while True:
        #获取开始时间戳
        start=time.time()
        #事件
        events=pygame.event.get()
        for event in events:
            #窗体关闭
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
        end=time.time()
        #获取耗时
        cost=end-start
        if cost<DEFAULT_DELAY:
            sleep=DEFAULT_DELAY-cost
        else:
            sleep=0
        time.sleep(sleep)
        end=time.time()
        fps=1.0/(end-start)



