from pygame.locals import *
'''
当前显示页面
'''
__current=None

def go(page):
    global __current
    #进入某页面
    __current=page

def render():
    '''渲染页面'''
    __current.render()

def key_down(key):
    '''键盘按下事件'''
    __current.key_down(key)



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
            go(SecondPage(self.surface))

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


        pass