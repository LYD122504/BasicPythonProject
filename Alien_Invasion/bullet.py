import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''一个对飞船发射的子弹进行管理的类'''
    def __init__(self,setting,screen,ship):
        '''在飞船所在的位置创建一个子弹对象'''
        super().__init__()
        self.screen=screen
        # 在(0,0)处创建一个表示子弹的矩形,在设置正确位置
        # 因为子弹不是基于图像的,所以我们需要用Rect函数从空白创建一个矩形,
        # 需要提供矩形左上角的x和y坐标以及矩形宽度和高度
        self.rect=pygame.Rect(0,0,setting.bullet_width,setting.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        # 用小数存储子弹位置
        self.y=float(self.rect.y)
        self.color=setting.bullet_color
        self.speed_factor=setting.bullet_speed_factor
    
    def update(self):
        '''向上移动子弹'''
        # 更新表示子弹位置的小数值
        self.y-=self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.y=self.y
    
    def draw_bullet(self):
        '''在屏幕上绘制子弹'''
        pygame.draw.rect(self.screen,self.color,self.rect)