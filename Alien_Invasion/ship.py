import pygame
from pygame.sprite import Sprite
# Pygame中原点(0,0)位于屏幕左上角,往右下方移动的话,坐标增大
class Ship(Sprite):
    def __init__(self,setting,screen):
        self.setting=setting
        # 初始化飞船并设置相应位置
        super().__init__()
        self.screen=screen
        # 加载飞船图像并获得其外接矩形
        self.image=pygame.image.load('images/ship.bmp')
        # 给你的图片套上一个紧贴边缘的“隐形长方形盒子”
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()
        # 把飞船移动到屏幕底部的中心点
        # 在飞船的属性center中存储小数值
        self.rect.centerx=self.screen_rect.centerx
        self.center=float(self.rect.centerx)
        self.rect.bottom=self.screen_rect.bottom
        # 持续移动标志
        self.moving_right=False
        self.moving_left=False

    def update(self):
        '''根据移动标志调整飞船位置'''
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center+=self.setting.ship_speed_factor
        if self.moving_left and self.rect.left>self.screen_rect.left:
            self.center-=self.setting.ship_speed_factor
        self.rect.centerx=self.center
        
    def blitme(self):
        '''在指定位置绘制飞机'''
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        '''让飞船在屏幕上居中'''
        self.center=self.screen_rect.centerx