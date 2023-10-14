import pygame
from pygame.locals import *

# 初始化游戏
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Super Mario")

# 加载角色和背景图像
background = pygame.image.load("background.png")
player = pygame.image.load("mario.png")

# 设置角色的初始位置和速度
player_rect = player.get_rect()
player_rect.topleft = (100, 100)
player_speed = 5

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        player_rect.x -= player_speed
    if keys[K_RIGHT]:
        player_rect.x += player_speed
    if keys[K_UP]:
        player_rect.y -= player_speed
    if keys[K_DOWN]:
        player_rect.y += player_speed

    # 更新屏幕
    screen.blit(background, (0, 0))
    screen.blit(player, player_rect)
    pygame.display.flip()

# 退出游戏
pygame.quit()
