import pygame
import random


def gettext(message, color, x, y):
    font = pygame.font.SysFont("Calibri", 36)
    text = font.render(message, True, color)
    place = text.get_rect(center=(x, y))
    sc.blit(text, place)


def win():
    global restarttrigger
    player = ""
    if lp > rp:
        player = "left"
        color = BLUE
    elif rp > lp:
        player = "right"
        color = RED
    else:
        player = "both"
        color = LIGHTBLUE
    sc.fill(color)
    gettext(f"{player} won!", WHITE, WIDTH // 2, HEIGHT // 2)
    pygame.display.flip()
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                exit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_1 and not restarttrigger:
                    restarttrigger = True
                    draw()
                    return


def draw():
    global vx, vy, padspeed, rp, lp, ball, pads, rightpad, leftpad
    vx = random.choice((-5, 5))
    vy = 0
    padspeed = 4
    rp = 0
    lp = 0
    leftpad = pygame.Surface((20, 80)).get_rect(center=(20, HEIGHT // 2))
    rightpad = pygame.Surface((20, 80)).get_rect(center=(WIDTH - 20, HEIGHT // 2))
    ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)
    pads = [leftpad, rightpad]

    pygame.draw.rect(sc, BLUE, leftpad)
    pygame.draw.rect(sc, RED, rightpad)
    pygame.draw.rect(sc, BLACK, ball)
    pygame.draw.line(sc, BLACK, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 1)
    gettext(f"{lp}", BLUE, WIDTH // 2 - 20, 20)
    gettext(f"{rp}", RED, WIDTH // 2 + 20, 20)


pygame.init()
restarttrigger = True

HEIGHT = 600
WIDTH = 800
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHTBLUE = (115, 215, 255)
BROWN = (123, 63, 0)
YELLOW = (255, 255, 0)
GRASGREEN = (34, 139, 34)

sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("example")
clock = pygame.time.Clock()
vx = random.choice((-5, 5))
vy = 0
padspeed = 4
rp = 0
lp = 0
leftpad = pygame.Surface((20, 80)).get_rect(center=(20, HEIGHT // 2))
rightpad = pygame.Surface((20, 80)).get_rect(center=(WIDTH - 20, HEIGHT // 2))
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)
pads = [leftpad, rightpad]
play = True
trigger = False

while play:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN and not trigger:
            if event.key == pygame.K_SPACE:
                trigger = True

    if trigger:
        ball.move_ip(vx, vy)
    if ball.collidelist(pads) >= 0:
        vy = random.randint(-8, 8)
        vx = (-vx) * 1.1
        padspeed = padspeed * 1.1
    if ball.y >= HEIGHT or ball.y <= 0:
        vy = -vy
    if ball.x <= 0 or ball.x >= WIDTH:
        if ball.x <= 0:
            rp += 1
        else:
            lp += 1
        vx = random.choice((-5, 5))
        vy = 0
        ball.x = WIDTH // 2 - 10
        ball.y = HEIGHT // 2 - 10
        trigger = False
        padspeed = 4
        leftpad.center = 20, HEIGHT // 2
        rightpad.center = WIDTH - 20, HEIGHT // 2
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and leftpad.y > 0:
        leftpad.y -= padspeed
    if keys[pygame.K_a] and leftpad.x > 0:
        leftpad.x -= padspeed
    if keys[pygame.K_s] and leftpad.y < HEIGHT - 80:
        leftpad.y += padspeed
    if keys[pygame.K_d] and leftpad.x < WIDTH // 2 - 20:
        leftpad.x += padspeed

    if keys[pygame.K_UP] and rightpad.y > 0:
        rightpad.y -= padspeed
    if keys[pygame.K_LEFT] and rightpad.x > WIDTH // 2:
        rightpad.x -= padspeed
    if keys[pygame.K_DOWN] and rightpad.y < HEIGHT - 80:
        rightpad.y += padspeed
    if keys[pygame.K_RIGHT] and WIDTH - 20 > rightpad.x:
        rightpad.x += padspeed

    if lp == 10 or rp == 10:
        trigger = False
        print(restarttrigger)
        restarttrigger = False
        win()

    sc.fill(LIGHTBLUE)
    pygame.draw.rect(sc, BLUE, leftpad)
    pygame.draw.rect(sc, RED, rightpad)
    pygame.draw.rect(sc, BLACK, ball)
    pygame.draw.line(sc, BLACK, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 1)
    gettext(f"{lp}", BLUE, WIDTH // 2 - 20, 20)
    gettext(f"{rp}", RED, WIDTH // 2 + 20, 20)

    pygame.display.flip()
pygame.quit()
