import pygame

class GameInitializer:
    def __init__(
            self, 
            car_path, 
            cassowary_path, 
            heavy_forest_tile_1_path, 
            heavy_forest_tile_2_path, 
            heavy_forest_tile_3_path, 
            heavy_forest_tile_4_path, 
            window_size):
        self.cassowary_unscaled = None
        self.car_unscaled = None
        self.heavy_forest_tile_1_unscaled = None
        self.heavy_forest_tile_2_unscaled = None
        self.heavy_forest_tile_3_unscaled = None
        self.heavy_forest_tile_4_unscaled = None
        self.lane_lines = None
        self.lane_amount = 4
        self.tiles = []
        self.car_path = car_path
        self.cassowary_path = cassowary_path
        self.heavy_forest_tile_1_path = heavy_forest_tile_1_path
        self.heavy_forest_tile_2_path = heavy_forest_tile_2_path
        self.heavy_forest_tile_3_path = heavy_forest_tile_3_path
        self.heavy_forest_tile_4_path = heavy_forest_tile_4_path
        self.init_assets()
        self.init_game_vars(window_size)
        self.init_background(window_size)

    def init_assets(self):
        self.cassowary_unscaled = pygame.image.load(self.cassowary_path)
        self.car_unscaled = pygame.image.load(self.car_path)
        self.heavy_forest_tile_1_unscaled = pygame.image.load(self.heavy_forest_tile_1_path)
        self.heavy_forest_tile_2_unscaled = pygame.image.load(self.heavy_forest_tile_2_path)
        self.heavy_forest_tile_3_unscaled = pygame.image.load(self.heavy_forest_tile_3_path)
        self.heavy_forest_tile_4_unscaled = pygame.image.load(self.heavy_forest_tile_4_path)

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
        self.tile_textures = [[],[],[],[]]
        temp = self.tile_textures
        self.tile_amount = (window_size[0] // 128 + 1, window_size[1] // 128 + 1)
        for x in range(0, self.tile_amount[0]):
            for y in range(0, self.tile_amount[1]):
                self.tiles.append((x * 128, y * 128))