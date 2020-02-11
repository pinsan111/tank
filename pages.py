from pygame.locals import *

class FirstPage:

    def __init__(self,surface):
        self.surface=surface
    def render(self):
        self.surface.fill((0xff,0,0))
    def key_down(self,key):
        '''
        key down事件
        :param key:用户按下的键
        :return:
        '''
        if key==K_RETURN:
            print('切换')
        print('page1')

        pass


class SecondPage:

    def __init__(self,surface):
        self.surface=surface
    def render(self):
        self.surface.fill((0,0xff,0))
        '''
        key down事件
        :param key:用户按下的键
        :return:
        '''
        print('page2')


        pass