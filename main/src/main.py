import pygame
import sys

pygame.init()
pygame.font.init()

# Define startup functions

def screen_init():
    global screen, window_size, clock

    window_size  = (1000, 600)
    icon_path = r'main\src\assets\icon.png'

    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption('Keystone Game')

    icon = pygame.image.load(icon_path)
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()

    screen.fill((255, 255, 255))

def boot():
    comic_sans = pygame.font.SysFont('Comic Sans MS', 30)
    title_text = comic_sans.render('Cassowaries', False, (0, 0, 0))
    start_button = comic_sans.render('Start game', False, (255, 0, 0))
    screen.blit(title_text, (200, 20))
    screen.blit(start_button, (200, 70))

def start_game():
    pass

# Initiate

screen_init()
boot()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[0] >= 200 and pos[0] <= 360 and pos[1] >= 80 and pos[1] <= 100:
                start_game()

    pygame.display.flip()
    clock.tick(60)