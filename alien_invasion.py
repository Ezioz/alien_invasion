'''
Descripttion: 
version: 
Author: ahtoh
Date: 2022-02-26 20:55:05
LastEditors: ahtoh
LastEditTime: 2022-02-26 20:57:19
'''

import sys
import pygame


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()


run_game()
