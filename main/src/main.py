import pygame
import sys
import random
import threading
from game_init import GameInitializer

pygame.init()
pygame.font.init()

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
        self.tiles_temp = [[],[],[],[]]
        for tile in self.tiles:
            temp_random = random.randint(0, 3)
            self.tile_textures[temp_random].append(tile)
            self.tiles_temp[temp_random].append((tile[0], -tile[1]))
        for i in range(0, 4):
            for tile in self.tiles_temp[i]:
                self.tile_textures[i].append(tile)


        self.is_game_started = True
        screen.fill((255, 255, 255))
        self.car.pos = (self.lane_lines[self.car.lane][1][0] + 60, window_size[1] - 72)

        animations.drive()

    def update(self):
        if self.is_game_started:
            screen.fill((255, 255, 255))  # Clear the screen

            self.polygon_points = []

            # Draw all the tiles
            for i in range(4):
                for tile in self.tile_textures[i]:
                    if i == 0:
                        screen.blit(self.heavy_forest_tile_1, tile)
                    elif i == 1:
                        screen.blit(self.heavy_forest_tile_2, tile)
                    elif i == 2:
                        screen.blit(self.heavy_forest_tile_3, tile)
                    elif i == 3:
                        screen.blit(self.heavy_forest_tile_4, tile)

            for i in range(1, round(self.lane_amount / 2) + 1):
                window_size[0] // 2 - (i * 200)
            
            self.polygon_points.append((window_size[0] // 2 - (round(self.lane_amount / 2)) * 200, window_size[1]))
            self.polygon_points.append((-(window_size[0] // 2 - (round(self.lane_amount / 2)) * 200), window_size[1])) # work in progress, Ill fix these numbers when I'm not going insane
            self.polygon_points.append((window_size[0] // 2, 0))
            print(self.polygon_points)

            pygame.draw.polygon(screen, (122, 122, 122), self.polygon_points)

            # Draw lane lines and the car sprite

            for line in self.lane_lines:
                pygame.draw.line(screen, (0, 0, 0), line[0], line[1], 1)
            self.car.pos = (self.lane_lines[self.car.lane][1][0] + 60, window_size[1] - 72)
            screen.blit(self.car_sprite, self.car.pos)


game = Game()

class Animations:
    drive_speed = 8  # Adjust for desired animation speed

    def drive(self):
        for i in range(4):  # Iterate through all rows of tiles
            for j in range(len(game.tile_textures[i])):
                x, y = game.tile_textures[i][j]
                new_y = y + self.drive_speed  # Move the tile down
                # Wrap the tile if it goes beyond the bottom of the screen
                if new_y >= window_size[1]:
                    new_y -= window_size[1] * 2  # Reset it to the top (with buffer)
                game.tile_textures[i][j] = (x, new_y)


animations = Animations()
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

    animations.drive()

    game.update()

    pygame.display.flip()
    clock.tick(60)
