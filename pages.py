from pygame.locals import *
from abc import *
import pygame

'''
当前显示页面
'''
__current=None

def go(page):
    if page is not None and isinstance(page, Page):
        global __current
        #进入某页面
        __current=page

def render():
    if __current is not None and isinstance(__current, Page):
        '''渲染页面'''
        __current.render()

def key_down(key):
    '''键盘按下事件'''
    if __current is not None and isinstance(__current, Page):
        __current.key_down(key)

def key_up(key):
    '''键盘抬起事件'''
    if __current is not None and isinstance(__current, Page):
        __current.key_up(key)

def key_pressed(keys):
    '''键盘长按事件'''
    if __current is not None and isinstance(__current, Page):
        __current.key_pressed(keys)

#页面对象

class Page(metaclass=ABCMeta):
    '''
    如创造新的页面需继承我，
    需要吧page做成抽象类 abstract class
    起规范作用，自身不可实例化
    '''
    def __init__(self,surface):
        if isinstance(surface,pygame.Surface):
            self.surface=surface

    @abstractmethod
    def render(self):
        '''
        渲染页面，所有子类必须实现
        :return:
        '''
    def key_down(self,key):
        '''
        键盘按下事件，非必需，不用定义成抽象方法，子类可选择复写函数
        :param key:按下的键
        :return:
        '''
    def key_up(self,key):
        pass
    def key_pressed(self,keys):
        pass



class FirstPage(Page):

    def __init__(self, surface):
        super().__init__(surface)

    def render(self):
        self.surface.fill((0xff,0,0))

    def key_down(self,key):
        if key==K_RETURN:
            go(SecondPage(self.surface))



class SecondPage(Page):

    def __init__(self, surface):
        super().__init__(surface)

    def render(self):
        self.surface.fill((0,0xff,0))

    def key_down(self, key):
        '''
        key down事件
        :param key:用户按下的键
        :return:
        '''
    def key_pressed(self,keys):
        if keys[K_m]:
            print('m')

            pass