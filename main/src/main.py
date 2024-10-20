import pygame
import sys
import random
import threading
from game_init import GameInitializer

# Initialize Pygame and font
pygame.init()
pygame.font.init()

# Define startup functions
def screen_init():
    global screen, window_size, clock

    window_size  = (1024, 640)
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
        heavy_forest_tile_1_path = r'main\src\assets\heavy_forest_tile_1.png'
        heavy_forest_tile_2_path = r'main\src\assets\heavy_forest_tile_2.png'
        heavy_forest_tile_3_path = r'main\src\assets\heavy_forest_tile_3.png'
        heavy_forest_tile_4_path = r'main\src\assets\heavy_forest_tile_4.png'

    def __init__(self):
        self.initializer = GameInitializer(
            self.assets.car_path, 
            self.assets.cassowary_path, 
            self.assets.heavy_forest_tile_1_path,
            self.assets.heavy_forest_tile_2_path,
            self.assets.heavy_forest_tile_3_path,
            self.assets.heavy_forest_tile_4_path,
            window_size)
        self.car_sprite = pygame.transform.scale2x(self.initializer.car_unscaled)
        self.heavy_forest_tile_1 = pygame.transform.scale_by(self.initializer.heavy_forest_tile_1_unscaled, 4)
        self.heavy_forest_tile_2 = pygame.transform.scale_by(self.initializer.heavy_forest_tile_2_unscaled, 4)
        self.heavy_forest_tile_3 = pygame.transform.scale_by(self.initializer.heavy_forest_tile_3_unscaled, 4)
        self.heavy_forest_tile_4 = pygame.transform.scale_by(self.initializer.heavy_forest_tile_4_unscaled, 4)
        self.tile_textures = self.initializer.tile_textures
        self.lane_lines = self.initializer.lane_lines
        self.lane_amount = self.initializer.lane_amount
        self.tiles = self.initializer.tiles
        self.car = self.Car()
        self.is_game_started = False

    class Car:
        def __init__(self):
            self.lane = 0
            self.pos = None

    def boot(self):
        comic_sans = pygame.font.SysFont('Comic Sans MS', 30)
        title_text = comic_sans.render('Cassowaries', False, (0, 0, 0))
        start_button = comic_sans.render('Start game', False, (255, 0, 0))
        screen.blit(title_text, (200, 20))
        screen.blit(start_button, (200, 80))

    def start(self):
        for tile in self.tiles:
            self.tile_textures[random.randint(0,3)].append(tile)
        for tile in self.tile_textures[0]:
            screen.blit(self.heavy_forest_tile_1, tile)
        for tile in self.tile_textures[1]:
            screen.blit(self.heavy_forest_tile_2, tile)
        for tile in self.tile_textures[2]:
            screen.blit(self.heavy_forest_tile_3, tile)
        for tile in self.tile_textures[3]:
                screen.blit(self.heavy_forest_tile_4, tile)

        self.is_game_started = True
        screen.fill((255, 255, 255))
        self.car.pos = (self.lane_lines[self.car.lane][1][0] + 60, window_size[1] - 72)
        screen.blit(self.car_sprite, self.car.pos)
        for line in self.lane_lines:
            pygame.draw.line(screen, (0, 0, 0), line[0], line[1], 1)

    def update(self):
        if self.is_game_started:
            screen.fill((255, 255, 255))
            for tile in self.tile_textures[0]:
                screen.blit(self.heavy_forest_tile_1, tile)
            for tile in self.tile_textures[1]:
                screen.blit(self.heavy_forest_tile_2, tile)
            for tile in self.tile_textures[2]:
                screen.blit(self.heavy_forest_tile_3, tile)
            for tile in self.tile_textures[3]:
                screen.blit(self.heavy_forest_tile_4, tile)
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
            if pos[0] >= 200 and pos[0] <= 360 and pos[1] >= 80 and pos[1] <= 120:
                game.start()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and game.car.lane < game.lane_amount - 1:
                game.car.lane += 1
            elif event.key == pygame.K_LEFT and game.car.lane > 0:
                game.car.lane -= 1

    game.update()

    pygame.display.flip()
    clock.tick(60)  # Cap the frame rate to 60 FPS
