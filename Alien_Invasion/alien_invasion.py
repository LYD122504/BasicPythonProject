import pygame
import sys
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from score_board import Scoreboard

def run_game():
    # 初始化一个游戏同时创建一个屏幕对象
    # 初始化背景设置
    pygame.init()
    # 输入用户名
    player_name=input()
    print(player_name)
    # 创建了一个名为screen的显示窗口,其大小为800*600像素的大小
    ai_setting=Settings()
    screen=pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建飞船对象
    ship=Ship(ai_setting,screen)
    # 创建一罐用于存储游戏统计信息的实例
    stats=GameStats(ai_setting,player_name)
    # 创建一个用于存储子弹的编组
    # 不在循环内创建,避免重复创建,消耗计算时间
    bullets=Group()
    # 创建一个用于存储外星人的编组
    aliens=Group()
    # 创建一个计分牌类
    sb=Scoreboard(ai_setting,screen,stats)
    # 创建外星人群,在此创建外星人类
    gf.create_fleet(ai_setting,screen,ship,aliens)
    # 创建一个Play按钮
    msg="Play"
    play_button=Button(ai_setting,screen,msg)
    # 设置游戏主循环
    while True:
        gf.check_events(ai_setting,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_setting,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_setting,stats,screen,sb,ship,aliens,bullets)
        gf.update_srceen(ai_setting,screen,stats,sb,ship,aliens,bullets,play_button)
        
if __name__=='__main__':
    run_game()