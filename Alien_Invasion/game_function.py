import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event,setting,stats,sb,screen,ship,aliens,bullets):
    '''响应按键'''
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key==pygame.K_SPACE:
        fire_bullets(setting,screen,ship,bullets)
    elif event.key==pygame.K_q:
        stats.save_scores()
        pygame.quit()
        sys.exit()
    elif event.key==pygame.K_p:
        start_game_keyboard(setting,screen,stats,sb,ship,aliens,bullets)

def fire_bullets(setting,screen,ship,bullets):
    # 判断子弹数目是否少于最大容许数量
    # 如果没有达到限制,发射一颗子弹
    if len(bullets)<setting.bullets_allowed:
        # 创建一颗子弹,并将其加入到编组bullets中
        new_bullets=Bullet(setting,screen,ship)
        bullets.add(new_bullets)

def check_keyup_events(event,ship):
    '''响应松开'''
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    if event.key==pygame.K_LEFT:
        ship.moving_left=False 

def check_events(setting,screen,stats,sb,play_button,ship,aliens,bullets):
    # 监控键盘和鼠标事件
    # 事件循环,用来监听事件,根据发生的事情执行相应的任务
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,setting,stats,sb,screen,ship,aliens,bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship) 
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(setting,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)

def start_game(setting,stats,sb,screen,ship,aliens,bullets):
    # 重置游戏统计信息
    stats.reset_stats()
    # 重置游戏设置
    setting.initialize_dynamic_settings()
    # 隐藏光标
    pygame.mouse.set_visible(False)
    # 激活游戏信息
    stats.game_active=True
    # 重置记分牌图像
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()
    # 清空外星人列表和子弹列表
    aliens.empty()
    bullets.empty()
    # 创建一群新的外星人,并让飞船居中
    create_fleet(setting,screen,ship,aliens)
    ship.center_ship()

def start_game_keyboard(setting,screen,stats,sb,ship,aliens,bullets):
    if not stats.game_active:
        start_game(setting,stats,sb,screen,ship,aliens,bullets)

def check_play_button(setting,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    '''在玩家单击Play按钮时开始新游戏'''
    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
       start_game(setting,stats,sb,screen,ship,aliens,bullets)

def get_number_aliens(setting,alien):
    '''计算一行可以容纳多少个外星人'''
    alien_width=alien.rect.width
    available_width=setting.screen_width-2*alien_width
    number_aliens=int(available_width/(2*alien_width))
    return number_aliens

def get_number_rows(setting,ship_height,alien_height):
     '''计算屏幕可以容纳多少行外星人'''
     availabe_space=setting.screen_height-3*alien_height-ship_height
     number_rows=int(availabe_space/(2*alien_height))
     return number_rows

def create_alien(setting,screen,aliens,alien_number,row_number):
    '''创建一个外星人并放在当前行'''
    alien=Alien(setting,screen)
    alien_width=alien.rect.width
    alien.x=alien_width+2*alien_width*alien_number
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
    aliens.add(alien)

def create_fleet(setting,screen,ship,aliens):
    '''创建外星人群'''
    # 创建一个外星人,并计算一行可以容纳多少个外星人
    # 外星人间距为外星人宽度
    alien=Alien(setting,screen)
    number_aliens=get_number_aliens(setting,alien)
    number_rows=get_number_rows(setting,ship.rect.height,alien.rect.height)
    # 创建外星人群
    for number_row in range(number_rows):
        # 创建第一行外星人
        for alien_number in range(number_aliens):
            # 创建一个外星人并将其加入当前行
            create_alien(setting,screen,aliens,alien_number,number_row)   

def update_srceen(ai_setting,screen,stats,sb,ship,aliens,bullets,play_button):
    '''更新屏幕上的图像,并切换到新屏幕'''
    # 每次循环的时候都重绘屏幕
    screen.fill(ai_setting.bg_color)
    # 在飞船和外星人后面重新绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 绘制外星人
    aliens.draw(screen)
    # 绘制飞船
    ship.blitme()
    # 显示得分
    sb.show_score()
    # 如果游戏处于非活动状态就绘制Play按钮
    # 放在最后防止被覆盖
    if not stats.game_active:
        play_button.draw_button()
    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(setting,screen,stats,sb,ship,aliens,bullets):
    '''更新子弹的位置并且删除已消失的子弹'''
    # 对编组使用update方法,相当于对编组内部的每个对象调用update方法
    bullets.update()
    # 这里使用for循环的时候不应该从列表或者编组中删除条目,所以需要使用副本遍历
    for bullet in bullets.copy():
        if bullet.rect.bottom<0:
            bullets.remove(bullet)
    # 检查是否有子弹击中外星人
    check_bullet_alien_collisions(setting,screen,stats,sb,ship,aliens,bullets)

def check_bullet_alien_collisions(setting,screen,stats,sb,ship,aliens,bullets):
    '''响应子弹和外星人的碰撞'''
    # 如果是这样,就需要删除相应的子弹和外星人
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
    if len(aliens)==0:
        # 删除现有的子弹并新建一批外星人
        bullets.empty()
        setting.increase_speed()
        create_fleet(setting,screen,ship,aliens)
        # 提高等级
        stats.level+=1
        sb.prep_level()
    if collisions:
        for aliens in collisions.values():
            stats.score+=setting.alien_point*len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)
def update_aliens(setting,stats,screen,sb,ship,aliens,bullets):
    '''更新外星人群中所有外星人的位置'''
    check_fleet_edges(setting,aliens)
    aliens.update()
    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        print('SHIP HIT!!!')
        ship_hit(setting,stats,screen,sb,ship,aliens,bullets)
    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(setting,stats,screen,sb,ship,aliens,bullets)

def check_high_score(stats,sb):
    '''检查是否诞生了新的最高得分'''
    if stats.score>stats.high_score:
        stats.high_score=stats.score
        sb.prep_high_score()

def check_fleet_edges(setting,aliens):
    '''有外星人到达边缘时采取相应的措施'''
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(setting,aliens)
            break

def change_fleet_direction(setting,aliens):
    '''将整体外星人下移,并改变他们的方向'''
    for alien in aliens.sprites():
        alien.rect.y+=setting.fleet_drop_speed
    setting.fleet_direction*=-1

def ship_hit(setting,stats,screen,sb,ship,aliens,bullets):
    '''响应被外星人撞到的飞船'''
    if stats.ships_left>0:
        # 将ships_left减1
        stats.ships_left-=1
        # 更新生命
        sb.prep_ships()
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        # 创建一群新的外星人,并将飞船放到屏幕底端中央
        create_fleet(setting,screen,ship,aliens)
        ship.center_ship()
        # 暂停
        sleep(0.5)
    else:
        stats.save_scores()
        stats.game_active=False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(setting,stats,screen,sb,ship,aliens,bullets):
    '''检查是否有外星人到达了屏幕底端'''
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            ship_hit(setting,stats,screen,sb,ship,aliens,bullets)
            break