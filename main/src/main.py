import pygame
import sys
from game_init import GameInitializer

# Initialize Pygame and font
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

screen_init()

class Game:
    class assets:
        car_path = r'main\src\assets\car.png'
        cassowary_path = r'main\src\assets\cassowary.png'

    def __init__(self):
        self.initializer = GameInitializer(self.assets.car_path, self.assets.cassowary_path)
        self.car_sprite = pygame.transform.scale2x(self.initializer.car_unscaled)
        self.lane_lines = self.initializer.lane_lines
        self.car = self.Car()
        self.is_game_started = False

    class Car:
        def __init__(self):
            self.lane = 1
            self.pos = None

    def boot(self):
        comic_sans = pygame.font.SysFont('Comic Sans MS', 30)
        title_text = comic_sans.render('Cassowaries', False, (0, 0, 0))
        start_button = comic_sans.render('Start game', False, (255, 0, 0))
        screen.blit(title_text, (200, 20))
        screen.blit(start_button, (200, 80))

    def start(self):
        self.is_game_started = True
        screen.fill((255, 255, 255))
        self.car.pos = (self.lane_lines[self.car.lane][1][0] + 60, window_size[1] - 72)
        screen.blit(self.car_sprite, self.car.pos)
        for line in self.lane_lines:
            pygame.draw.line(screen, (0, 0, 0), line[0], line[1], 1)

    def update(self):
        if self.is_game_started:
            screen.fill((255, 255, 255))
            for line in self.lane_lines:
                pygame.draw.line(screen, (0, 0, 0), line[0], line[1], 1)
            self.car.pos = (self.lane_lines[self.car.lane][1][0] + 60, window_size[1] - 72)
            screen.blit(self.car_sprite, self.car.pos)


# Initialize game
game = Game()
game.boot()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            if pos[0] >= 200 and pos[0] <= 360 and pos[1] >= 80 and pos[1] <= 120:
                game.start()

    game.update()

    pygame.display.flip()
    clock.tick(60)  # Cap the frame rate to 60 FPS
