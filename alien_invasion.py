'''
Descripttion: 
version: 
Author: ahtoh
Date: 2022-02-26 20:55:05
LastEditors: ahtoh
LastEditTime: 2022-02-27 19:33:08
'''

import sys
from bullet import Bullet
from settings import Settings
import pygame
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
