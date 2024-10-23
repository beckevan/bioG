import pygame
import random

class GameInitializer:
    def __init__(
            self, 
            car_path, 
            heavy_forest_tile_1_path, 
            heavy_forest_tile_2_path, 
            heavy_forest_tile_3_path, 
            heavy_forest_tile_4_path,
            dying_forest_tile_1_path,
            dying_forest_tile_2_path,
            dying_forest_tile_3_path,
            dying_forest_tile_4_path,
            dirt_path,
            cassowary_running_1_path,
            cassowary_running_2_path,
            cassowary_running_3_path,
            cassowary_running_4_path,
            cassowary_running_5_path,
            cassowary_running_6_path,
            window_size):
        self.car_unscaled = None
        self.cassowary_running_1_unscaled = None
        self.cassowary_running_2_unscaled = None
        self.cassowary_running_3_unscaled = None
        self.cassowary_running_4_unscaled = None
        self.cassowary_running_5_unscaled = None
        self.cassowary_running_6_unscaled = None
        self.heavy_forest_tile_1_unscaled = None
        self.heavy_forest_tile_2_unscaled = None
        self.heavy_forest_tile_3_unscaled = None
        self.heavy_forest_tile_4_unscaled = None
        self.dying_forest_tile_1_unscaled = None
        self.dying_forest_tile_2_unscaled = None
        self.dying_forest_tile_3_unscaled = None
        self.dying_forest_tile_4_unscaled = None
        self.dirt_unscaled = None
        self.lane_lines = None
        self.lane_amount = 4
        self.tiles = []
        self.car_path = car_path
        self.cassowary_running_1_path = cassowary_running_1_path
        self.cassowary_running_2_path = cassowary_running_2_path
        self.cassowary_running_3_path = cassowary_running_3_path
        self.cassowary_running_4_path = cassowary_running_4_path
        self.cassowary_running_5_path = cassowary_running_5_path
        self.cassowary_running_6_path = cassowary_running_6_path
        self.heavy_forest_tile_1_path = heavy_forest_tile_1_path
        self.heavy_forest_tile_2_path = heavy_forest_tile_2_path
        self.heavy_forest_tile_3_path = heavy_forest_tile_3_path
        self.heavy_forest_tile_4_path = heavy_forest_tile_4_path
        self.dying_forest_tile_1_path = dying_forest_tile_1_path
        self.dying_forest_tile_2_path = dying_forest_tile_2_path
        self.dying_forest_tile_3_path = dying_forest_tile_3_path
        self.dying_forest_tile_4_path = dying_forest_tile_4_path
        self.dirt_path = dirt_path
        self.init_assets()
        self.init_game_vars(window_size)
        self.init_background(window_size)

    def init_assets(self):
        self.car_unscaled = pygame.image.load(self.car_path)
        self.cassowary_running_1_unscaled = pygame.image.load(self.cassowary_running_1_path)
        self.cassowary_running_2_unscaled = pygame.image.load(self.cassowary_running_2_path)
        self.cassowary_running_3_unscaled = pygame.image.load(self.cassowary_running_3_path)
        self.cassowary_running_4_unscaled = pygame.image.load(self.cassowary_running_4_path)
        self.cassowary_running_5_unscaled = pygame.image.load(self.cassowary_running_5_path)
        self.cassowary_running_6_unscaled = pygame.image.load(self.cassowary_running_6_path)
        self.heavy_forest_tile_1_unscaled = pygame.image.load(self.heavy_forest_tile_1_path)
        self.heavy_forest_tile_2_unscaled = pygame.image.load(self.heavy_forest_tile_2_path)
        self.heavy_forest_tile_3_unscaled = pygame.image.load(self.heavy_forest_tile_3_path)
        self.heavy_forest_tile_4_unscaled = pygame.image.load(self.heavy_forest_tile_4_path)
        self.dying_forest_tile_1_unscaled = pygame.image.load(self.dying_forest_tile_1_path)
        self.dying_forest_tile_2_unscaled = pygame.image.load(self.dying_forest_tile_2_path)
        self.dying_forest_tile_3_unscaled = pygame.image.load(self.dying_forest_tile_3_path)
        self.dying_forest_tile_4_unscaled = pygame.image.load(self.dying_forest_tile_4_path)
        self.dirt_unscaled = pygame.image.load(self.dirt_path)

    def init_game_vars(self, window_size):
        self.lane_lines = [((window_size[0] // 2, 0), (window_size[0] // 2, window_size[1]))]

        for i in range(1, round(self.lane_amount / 2) + 1):
            self.lane_lines.append(
                ((window_size[0] // 2, 0), (window_size[0] // 2 - (i * 200), window_size[1]))
            )
            self.lane_lines.append(
                ((window_size[0] // 2, 0), (window_size[0] // 2 + (i * 200), window_size[1]))
            )

        self.lane_lines = sorted(self.lane_lines, key=lambda x: x[1][0])

    def init_background(self, window_size):
        self.tile_textures = [[], [], [], []]
        self.tile_amount = (window_size[0] // 256, window_size[1] // 256)

        for x in range(self.tile_amount[0]):
            for y in range(self.tile_amount[1]):
                # Store (x, y, value) as a tuple
                value = random.randint(1, 4)  # Random texture value between 1 and 4
                self.tiles.append(((x * 256, y * 256), value))