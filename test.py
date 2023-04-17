
import pygame
import random

# 初始化 Pygame 库
pygame.init()

# 游戏窗口大小
window_width = 300
window_height = 600

# 定义颜色，RGB格式
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# 定义方块的大小（长和宽应该相等）
block_size = 30

# 创建游戏窗口
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('俄罗斯方块')


# 绘制文字
def draw_text(text, font_size, color, x, y):
    font = pygame.font.Font(None, font_size)
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    game_window.blit(text_obj, text_rect)


# 绘制一个矩形
def draw_block(color, x, y):
    pygame.draw.rect(game_window, color, [x, y, block_size, block_size])


# 在屏幕上绘制一个网格
def draw_grid():
    for x in range(0, window_width, block_size):
        for y in range(0, window_height, block_size):
            draw_block(gray, x, y)


# 定义一个方块类
class Block:
    def __init__(self, shape):
        self.shape = shape
        self.color = random.choice([red, green, blue])

    # 绘制方块
    def draw(self):
        for row, line in enumerate(self.shape):
            for col, block in enumerate(line):
                if block == '1':
                    draw_block(self.color,
                               col * block_size,
                               row * block_size)

    # 复制一个新的方块实例
    def copy(self):
        return Block(self.shape)


# 定义所有可能的方块形状
blocks = [
    [
        '0000',
        '1111',
        '0000',
        '0000'
    ],
    [
        '0010',
        '0010',
        '0010',
        '0010',
    ],
    [
        '0000',
        '0110',
        '1100',
        '0000'
    ],
    [
        '0100',
        '1100',
        '1000',
        '0000'
    ],
    [
        '0000',
        '1100',
        '0110',
        '0000'
    ],
    [
        '0100',
        '0100',
        '1100',
        '0000'
    ],
    [
        '0000',
        '1100',
        '0100',
        '0100'
    ],
]

# 随机选择一个方块作为当前方块
current_block = Block(random.choice(blocks))

# 当前方块的位置（单位为方块数量）
cx, cy = 4, -4

# 主循环
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 绘制网格和当前方块
    draw_grid()
    current_block.draw()

    # 检测是否按下了“下”键
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        cy += 1

    # 绘制屏幕
    pygame.display.update()
