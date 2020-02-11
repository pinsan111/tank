from pygame.locals import *
from abc import *
import pygame
from locals import *
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



class HomePage(Page):

    def __init__(self, surface):
        super().__init__(surface)

        #导入背景
        self.bg=pygame.image.load('img/bg.png')
        self.bg_w=self.bg.get_width()
        self.bg_h = self.bg.get_height()
        self.bg_x=(WINDOW_WIDTH-self.bg_w)/2
        self.bg_y = (WINDOW_HEIGHT - self.bg_h) / 2

        #当前选项

        self.index=0
        self.positions=[395,450.500]

        self.pointer=pygame.image.load('img/pointer.png')
        self.p_x =395
        self.p_y =self.positions[self.index]

    def render(self):
        #绘制页面
        self.surface.fill((0,0,0))
        #显示北京
        self.surface.blit(self.bg,(self.bg_x,self.bg_y))
        #显示指针
        self.surface.blit(self.pointer,(self.p_x,self.p_y))
    def key_down(self,key):
        if key==K_DOWN():
            #向下移动指针
            self.index+=1
            if self.index>=len(self.positions):
                self.index=0
            self.p_y =self.positions[self.index]


