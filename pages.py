from pygame.locals import *
from abc import *
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

#页面对象

class Page(metaclass=ABCMeta):
    '''
    如创造新的页面需继承我，
    需要吧page做成抽象类 abstract class
    起规范作用，自身不可实例化
    '''
    pass


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