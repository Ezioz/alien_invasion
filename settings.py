'''
Descripttion: 
version: 
Author: ahtoh
Date: 2022-02-26 21:53:19
LastEditors: ahtoh
LastEditTime: 2022-02-27 19:26:46
'''


class Settings():
    # 存储《外星人入侵》所有设置的类
    def __init__(self) -> None:
        # 初始化游戏设置
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1.5

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
