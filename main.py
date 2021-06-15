import os
import sys
import pygame
import random

start_width = 500
start_height = 200
window_width = 180

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
filled_boxes = []
player_chance = 0
curr_game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def main():
    global screen, clock, filled_boxes, player_chance, curr_game
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_width), flags=pygame.NOFRAME)
    clock = pygame.time.Clock()
    pygame.display.set_caption("O-X")
    screen.fill(white)
    drawgrid()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos1 = pygame.mouse.get_pos()
                pos = [pos1[0], pos1[1]]
                if pos[0] < 60:
                    pos[0] = 0
                elif pos[0] < 120:
                    pos[0] = 60
                else:
                    pos[0] = 120
                if pos[1] < 60:
                    pos[1] = 0
                elif pos[1] < 120:
                    pos[1] = 60
                else:
                    pos[1] = 120
                if pos in filled_boxes:
                    continue
                filled_boxes.append(pos)
                if player_chance == 0:
                    fill_col(pos, red)
                    curr_game[pos[0] // 60][pos[1] // 60] = 1
                    player_chance = 1
                else:
                    fill_col(pos, green)
                    curr_game[pos[0] // 60][pos[1] // 60] = 2
                    player_chance = 0
        pygame.display.update()
        check()


def check():
    global curr_game
    l = curr_game
    for i in range(0, 3):
        if l[i][0] == 1 and l[i][1] == 1 and l[i][2] == 1:
            draw_block(i * 60, 0, red)
            draw_block(i * 60, 60, red)
            draw_block(i * 60, 120, red)
            pygame.time.delay(50)
            pygame.quit()
            gameover(0)
        elif l[i][0] == 2 and l[i][1] == 2 and l[i][2] == 2:
            draw_block(i * 60, 0, green)
            draw_block(i * 60, 60, green)
            draw_block(i * 60, 120, green)
            pygame.time.delay(50)
            pygame.quit()
            gameover(1)
        if l[0][i] == 1 and l[1][i] == 1 and l[2][i] == 1:
            draw_block(0, i * 60, red)
            draw_block(60, i * 60, red)
            draw_block(120, i * 60, red)
            pygame.time.delay(50)
            pygame.quit()
            gameover(0)
        elif l[0][i] == 2 and l[1][i] == 2 and l[2][i] == 2:
            draw_block(0, i * 60, green)
            draw_block(60, i * 60, green)
            draw_block(120, i * 60, green)
            pygame.time.delay(50)
            pygame.quit()
            gameover(1)
    if l[0][0] == l[1][1] and l[1][1] == l[2][2] and l[0][0] != 0:
        if l[0][0] == 0:
            ch = red
        else:
            ch = green
        draw_block(0, 0, ch)
        draw_block(60, 60, ch)
        draw_block(120, 120, ch)
        pygame.time.delay(50)
        pygame.quit()
        gameover(l[0][0] - 1)
    if l[0][2] == l[1][1] and l[1][1] == l[2][0] and l[1][1] != 0:
        if l[0][0] == 0:
            ch = red
        else:
            ch = green
        draw_block(0, 120, ch)
        draw_block(60, 60, ch)
        draw_block(120, 0, ch)
        pygame.time.delay(50)
        pygame.quit()
        gameover(l[1][1] - 1)
    for x in l:
        for y in x:
            if y == 0:
                return
    pygame.time.delay(50)
    pygame.quit()
    gameover(2)


def draw_block(x, y, col):
    rect = pygame.Rect(x, y, 60, 60)
    pygame.draw.rect(screen, col, rect, 6)
    pygame.display.update()
    pygame.time.delay(500)


def gameover(x):
    global screen, clock, window_width
    pygame.init()
    pygame.display.set_caption("!!!RESULT!!!")
    window_height = window_width - 60
    window_width += 600
    screen = pygame.display.set_mode((window_width, window_height))
    screen = pygame.display.set_mode((window_width, window_height))
    screen.fill(white)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        font = pygame.font.SysFont('century', 54, bold=True)
        if x == 0:
            s = "Player One Wins!!!"
        elif x == 1:
            s = "Player Two Wins!!!"
        else:
            s = "Match Draw"
        text = font.render(s, True, green)
        text_rect = text.get_rect()
        text_rect.center = (window_width // 2, window_height // 2)
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.delay(500)
        pygame.quit()
        sys.exit()


def fill_col(pos, col):
    if col == red:
        s = "X"
    else:
        s = "O"
    font = pygame.font.SysFont('century', 54, bold=True)
    text = font.render(s, True, black)
    text_rect = text.get_rect()
    text_rect.center = (pos[0] + 30, pos[1] + 30)
    screen.blit(text, text_rect)


def drawgrid():
    block_size = 60
    for i in range(0, window_width, block_size):
        for j in range(0, window_width, block_size):
            rect = pygame.Rect(i, j, block_size, block_size)
            pygame.draw.rect(screen, black, rect, 1)


def start():
    done = True
    pygame.init()
    screen = pygame.display.set_mode((start_width, start_height))
    pygame.display.set_caption("Tic-Tac-Toe Game")
    filepath = os.path.realpath("space_start.jpg")
    image = pygame.image.load(filepath)
    image_rect = image.get_rect()
    image_rect.center = (start_width // 2, start_height // 2)
    screen.blit(image, image_rect)
    font = pygame.font.SysFont('century', 60, bold=True)
    text = font.render("Tic-Tac-Toe", True, green)
    text_rect = text.get_rect()
    text_rect.center = (start_width // 2, 40)
    screen.blit(text, text_rect)
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    return
        pygame.display.update()


if __name__ == "__main__":
    start()
    main()
