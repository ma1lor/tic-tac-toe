import pygame
import sys
from main_class import Game

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")


#downloading all images
image_x = pygame.image.load('images/image_x.png')
image_o = pygame.image.load('images/image_o.png')
background_image = pygame.image.load("images/background.png")


#transforming to normal size
transformed_image_x = pygame.transform.scale(image_x, (100, 100))
transformed_image_o = pygame.transform.scale(image_o, (100, 100))


# for game itself
line_width = 8
line_length = 200

# vertical lines
vertical_line_left_start = (325, 100)
vertical_line_left_end = (325, 500)

vertical_line_right_start = (475, 100)
vertical_line_right_end = (475, 500)

#horizontal lines
horizontal_line_top_start = (200, 225)
horizontal_line_top_end = (600, 225)

horizontal_line_bottom_start = (200, 375)
horizontal_line_bottom_end = (600, 375)


# colours
black = (0, 0, 0)
white = (255, 255, 255)
gray = (200, 200, 200)

# buttons
button_width, button_height = 300, 70
button_x, button_y = (width - button_width) // 2, (height - button_height) // 2

# text
font = pygame.font.SysFont('microsofttaile', 36)
title_font = pygame.font.SysFont('microsofttaile', 72)
button_text = font.render("Start the game", True, black)
title_text = title_font.render("Tic Tac Toe", True, black)
title_rect = title_text.get_rect(center=(width // 2, 150))












game = Game()
game_run = False






def get_coords(mouse_x, mouse_y):
    square1 = [(200, 100), (325, 225)]
    square2 = [(325, 100), (475, 225)]
    square3 = [(475, 100), (600, 225)]

    square4 = [(200, 225), (325, 375)]
    square5 = [(325, 225), (475, 375)]
    square6 = [(475, 225), (600, 375)]

    square7 = [(200, 375), (325, 500)]
    square8 = [(325, 375), (475, 500)]
    square9 = [(475, 375), (600, 500)]
    
    for index, square in enumerate([square1, square2, square3, square4, square5, square6, square7, square8, square9], start=1):
        if square[0][0] < mouse_x < square[1][0] and square[0][1] < mouse_y < square[1][1]:
            game.make_move(index)






def draw_board(board):

    x = 0
    y = 0
    for row in range(3):
        for col in range(3):
            x = 205 + (145 * (col))
            y = 105 + (145 * (row))

            symbol = board[row][col]
            if symbol == 'X':
                screen.blit(transformed_image_x, (x, y))
            elif symbol == 'O':
                screen.blit(transformed_image_o, (x, y))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if game_run:
                get_coords(mouse_x, mouse_y)
            elif button_x < mouse_x < button_x + button_width and button_y < mouse_y < button_y + button_height:
                game_run = True


    screen.blit(background_image, (0, 0))

    if not game_run:
        
        pygame.draw.rect(screen, gray, (width // 2 - 220, 105, 440, 80))
        pygame.draw.rect(screen, black, (width // 2 - 220, 105, 440, 80), 2)

        screen.blit(title_text, title_rect)

        pygame.draw.rect(screen, gray, (button_x, button_y, button_width, button_height))
        pygame.draw.rect(screen, black, (button_x, button_y, button_width, button_height), 2)
        screen.blit(button_text, ((width - button_width) // 2 + 30, (height - button_height) // 2 + 15))
    else:
        screen.fill(black)
        pygame.draw.line(screen, white, vertical_line_left_start, vertical_line_left_end, line_width)
        pygame.draw.line(screen, white, vertical_line_right_start, vertical_line_right_end, line_width)
        pygame.draw.line(screen, white, horizontal_line_top_start, horizontal_line_top_end, line_width)
        pygame.draw.line(screen, white, horizontal_line_bottom_start, horizontal_line_bottom_end, line_width)
        draw_board(board=game.return_board())

    winner = game.check()
    if winner == 'O' or winner == 'X':
        victory_surface = pygame.Surface((300, 75))
        victory_surface.fill(black)
        victory_text = font.render(f"Player {winner} wins!", True, white)

        victory_rect = victory_text.get_rect(center=(victory_surface.get_width() // 2, victory_surface.get_height() // 2))

        screen.blit(background_image, (0, 0))


        victory_surface.blit(victory_text, victory_rect)

        screen.blit(victory_surface, ((width - victory_surface.get_width()) // 2, (height - victory_surface.get_height()) // 2))
    elif winner == "It's draw!":
        victory_surface = pygame.Surface((200, 75))
        victory_surface.fill(black)
        victory_text = font.render(f"It's a draw!", True, white)

        victory_rect = victory_text.get_rect(center=(victory_surface.get_width() // 2, victory_surface.get_height() // 2))

        screen.blit(background_image, (0, 0))


        victory_surface.blit(victory_text, victory_rect)

        screen.blit(victory_surface, ((width - victory_surface.get_width()) // 2, (height - victory_surface.get_height()) // 2))
        


    pygame.display.flip()