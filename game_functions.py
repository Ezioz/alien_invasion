'''
Descripttion:
version:
Author: ahtoh
Date: 2022-02-27 11:23:45
LastEditors: ahtoh
LastEditTime: 2022-02-27 19:55:05
'''

import sys
import pygame
from bullet import Bullet


def check_events(ai_settings, screen ,ship, bullets):
    # 响应按键和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)



def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # 响应按键
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 创建一颗子弹，并使其加入到编组bullets中
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
    # elif event.key == pygame.K_UP:
    #     ship.moving_top = True
        


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    # elif event.key == pygame.K_UP:
    #     ship.moving_top = False


def update_screen(ai_settings, screen, ship, bullets):
    # 更新屏幕上的图像，并切换到新屏幕
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()
