import pygame
import sys

pygame.init()
game_window_width = 600
game_window_height = 400
game_window = pygame.display.set_mode((game_window_width, game_window_height))

GAME = True
FPS = 60
timer_fps = pygame.time.Clock()
score_player1 = 0
score_player2 = 0
speed_ball = 3
ball_move_right = True
ball_move_top = False
end_score = 3

player1_font = pygame.font.Font(None, 30)
player2_font = pygame.font.Font(None, 30)
game_over_font = pygame.font.Font(None, 60)

surf_player1 = pygame.Surface((20, 100))
surf_player1.fill(pygame.Color('red'))
player1 = surf_player1.get_rect()
player1.x = 0
player1.y = 150
surf_player2 = pygame.Surface((20, 100))
surf_player2.fill(pygame.Color('blue'))
player2 = surf_player2.get_rect()
player2.x = 580
player2.y = 150

surf_ball = pygame.Surface((30, 30))
ball = surf_ball.get_rect()
ball.x = game_window_width // 2 - 15
ball.y = game_window_height // 2 - 15

def game_close():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

comp_up = False
comp_speed = 3

while GAME:
    game_window.fill(pygame.Color('white'))
    game_close()
    timer_fps.tick(FPS)

    game_window.blit(surf_player1, player1)
    game_window.blit(surf_player2, player2)
    game_window.blit(surf_ball, ball)

    key_player = pygame.key.get_pressed()
    if key_player[pygame.K_w] and player1.y > 0:
        player1.y -= 10
    elif key_player[pygame.K_s] and player1.bottom < game_window_height:
        player1.y += 10
    key_player2 = pygame.key.get_pressed()
    if key_player2[pygame.K_UP] and player2.y > 0:
        player2.y -= 10
    elif key_player2[pygame.K_DOWN] and player2.bottom < game_window_height:
        player2.y += 10

    if ball_move_top == True:
        ball.y -= speed_ball
    else:
        ball.y += speed_ball

    if ball_move_right == True:
        ball.x += speed_ball
    else:
        ball.x -= speed_ball
    if ball.y <= 0:
        ball_move_top = False
    if ball.y >= game_window_height:
        ball_move_top = True

    if comp_up == True:
        if player1.y > 0:
            player1.y -= comp_speed
    else:
        if player1.y < game_window_height and player1.bottom < game_window_height:
            player1.y += comp_speed
    if player1.y < ball.y:
        comp_up = False
    if player1.y > ball.y:
        comp_up = True

    if player1.y < ball.y:
        comp_up = False
    if player1.y > ball.y:
        comp_up = True
    if ball.colliderect(player1):
        ball_move_right = True
        speed_ball += 0.1
    if ball.colliderect(player2):
        ball_move_right = False
        speed_ball += 0.1

    if ball.x + 30 >= game_window_width:
        score_player1 += 1
        ball.x = game_window_width // 2 - 15
        ball.y = game_window_height // 2 - 15
        speed_ball = 3
    if ball.x <= 0:
        score_player2 += 1
        ball.x = game_window_width // 2 - 15
        ball.y = game_window_height // 2 - 15
        speed_ball = 3

    render_player1_font = player1_font.render(f"Player1: {score_player1}", True, pygame.Color('black'))
    render_player2_font = player2_font.render(f"Player2: {score_player2}", True, pygame.Color('black'))
    render_game_over = game_over_font.render(f"GAME OVER", True, pygame.Color('red'))
    game_window.blit(render_player1_font, (0, 10))
    game_window.blit(render_player2_font, (500, 10))

    if score_player1 >= end_score or score_player2 >= end_score:
        while True:
            game_window.blit(render_game_over, (game_window_width // 2 - 120, game_window_height // 2.2))
            pygame.display.update()
            game_close()
    pygame.display.update()
