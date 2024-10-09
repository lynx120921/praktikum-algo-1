import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monster Game")

BLACK = (0, 0, 0)
DARK_GRAY = (40, 40, 40)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

level = 1
lives = 3
max_lives = 3
enemy_position = 0
font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 24)
box_size = 100
game_mode = None 
time_limit = 10
time_left = time_limit
username = ""
clock = pygame.time.Clock()

def draw_boxes(level, selected=None, reveal_enemy=False):
    window.fill(DARK_GRAY)
    num_boxes = level + 1
    box_positions = []
    
    for i in range(num_boxes):
        x = i * (box_size + 20) + 50
        y = HEIGHT // 2 - box_size // 2
        box_positions.append((x, y))
        color = BLUE if selected == i else WHITE
        pygame.draw.rect(window, color, (x, y, box_size, box_size), 3)

    
        number_text = small_font.render(str(i + 1), True, BLACK)
        window.blit(number_text, (x + box_size // 2 - 10, y + box_size // 2 - 10))

       
        if reveal_enemy and i == enemy_position:
            draw_monster(x, y)  

    return box_positions

def draw_monster(x, y):
    pygame.draw.circle(window, RED, (x + box_size // 2, y + box_size // 2), 30) 
    pygame.draw.circle(window, BLACK, (x + box_size // 2 - 10, y + box_size // 2 - 10), 5) 
    pygame.draw.circle(window, BLACK, (x + box_size // 2 + 10, y + box_size // 2 - 10), 5) 
    pygame.draw.arc(window, BLACK, (x + box_size // 2 - 15, y + box_size // 2, 30, 15), 3.14, 0, 3)  
def display_message(message, color, pos):
    text = font.render(message, True, color)
    window.blit(text, pos)

def update_timer():
    global time_left
    if time_left > 0:
        time_left -= 1 / 60  
    display_message(f"Time Left: {int(time_left)}", WHITE, (10, 10))

def start_screen():
    global username
    input_active = True
    username = ""
    
    while True:
        window.fill(DARK_GRAY)
        display_message("Welcome to Monster Game!", BLUE, (WIDTH // 2 - 250, 50))
        display_message("Masukkan Nama Anda:", WHITE, (WIDTH // 2 - 150, 150))
        display_message(username, WHITE, (WIDTH // 2 - 150, 200)) 
        display_message("Tekan ENTER untuk melanjutkan", WHITE, (WIDTH // 2 - 200, 250))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if input_active and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and username:  
                    game_mode_selection()  
                elif event.key == pygame.K_BACKSPACE:  
                    username = username[:-1]
                else:
                    username += event.unicode 

        pygame.display.update()

def game_mode_selection():
    global game_mode
    window.fill(DARK_GRAY)
    display_message(f"Halo {username}, Pilih Mode Permainan!", BLUE, (WIDTH // 2 - 250, 50))

    modes = ["1. Normal", "2. Time Attack", "3. Random Guess"]
    for i, mode in enumerate(modes):
        display_message(mode, WHITE, (WIDTH // 2 - 100, 150 + i * 50))

    pygame.display.update()

    selected_mode = False
    while not selected_mode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_mode = "Normal"
                    selected_mode = True
                elif event.key == pygame.K_2:
                    game_mode = "Time Attack"
                    selected_mode = True
                elif event.key == pygame.K_3:
                    game_mode = "Random Guess"
                    selected_mode = True

    main_game()

def main_game():
    global level, lives, enemy_position, time_left
    lives = max_lives 
    enemy_position = random.randint(0, level)
    running = True

    while running:
        box_positions = draw_boxes(level)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, (x, y) in enumerate(box_positions):
                    if x < mouse_pos[0] < x + box_size and y < mouse_pos[1] < y + box_size:
                        if i == enemy_position:
                            display_message("Benar!", GREEN, (WIDTH // 2 - 50, 50))
                            pygame.display.update()
                            pygame.time.wait(500) 
                            level += 1
                            enemy_position = random.randint(0, level)  
                            lives = max_lives 
                            time_left = time_limit  
                        else:
                            lives -= 1
                            display_message(f"Salah! Monster berada di kotak {enemy_position + 1}", RED, (WIDTH // 2 - 200, 50))
                            draw_boxes(level, reveal_enemy=True)
                            pygame.display.update()
                            pygame.time.wait(1000) 
                            if lives == 0:
                                game_over("No Lives Left!")

        enemy_position = random.randint(0, level)
    
        if game_mode == "Time Attack":
            update_timer()
            if time_left <= 0:
                game_over("Time's Up!")
        display_message(f"Level: {level}", WHITE, (10, 50))
        display_message(f"Lives: {lives}", WHITE, (10, 90))
        pygame.display.update()
        
        clock.tick(60)  

def game_over(reason):
    global level, lives, time_left
    window.fill(DARK_GRAY)
    display_message(f"Game Over! {reason}", RED, (WIDTH // 2 - 200, HEIGHT // 2 - 50))
    display_message("1. Mulai Ulang dari Level 1", WHITE, (WIDTH // 2 - 250, HEIGHT // 2 + 20))
    display_message("2. Ganti Mode", WHITE, (WIDTH // 2 - 250, HEIGHT // 2 + 60))
    display_message("3. Keluar", WHITE, (WIDTH // 2 - 250, HEIGHT // 2 + 100))
    pygame.display.update()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1: 
                    level = 1
                    lives = max_lives
                    time_left = time_limit
                    main_game()
                elif event.key == pygame.K_2:   
                    game_mode_selection()
                elif event.key == pygame.K_3:   
                    start_screen()

start_screen()
