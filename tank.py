import pygame
from pygame.locals import *
import sys
import time
from pages import *
from locals import *

if __name__ == '__main__':
    #游戏初始化
    pygame.init()
    #设置窗体
    window=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    #FPS值
    fps=0

    surface=pygame.Surface(WINDOW_SIZE)

    #进入第一个页面

    go(HomePage(surface))

    # page = FirstPage(surface)
    # page = SecondPage(surface)

    while True:
        #获取开始时间戳
        start=time.time()
        #渲染逻辑事件
        # 页面渲染的容器surface
        window.blit(surface,(0,0))
        render()
        #flip
        pygame.display.flip()
        #事件
        events=pygame.event.get()
        for event in events:
            #窗体关闭
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type==K_DOWN:
                key_down(event.key)
            if event.type == K_UP:
                key_up(event.key)
        #长按事件
        keys=pygame.key.get_pressed()
        key_pressed(keys)


        #获取结束时间戳
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



