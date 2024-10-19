import pygame

class GameInitializer:
    def __init__(self, car_path, cassowary_path):
        self.cassowary_unscaled = None
        self.car_unscaled = None
        self.lane_lines = None
        self.lane_amount = 4
        self.car_path = car_path
        self.cassowary_path = cassowary_path
        self.init_assets()
        self.init_game_vars()  # Call to initialize game variables here

    def init_assets(self):
        # Load images using the provided paths
        self.cassowary_unscaled = pygame.image.load(self.cassowary_path)
        self.car_unscaled = pygame.image.load(self.car_path)

    def init_game_vars(self):
        # Initialize game variables
        self.lane_lines = [((1000 // 2, 0), (1000 // 2, 600))]  # Use fixed values here or pass window size as an argument

        for i in range(1, round(self.lane_amount / 2) + 1):
            self.lane_lines.append(
                ((1000 // 2, 0), (1000 // 2 - (i * 200), 600))
            )
            self.lane_lines.append(
                ((1000 // 2, 0), (1000 // 2 + (i * 200), 600))
            )

        self.lane_lines = sorted(self.lane_lines, key=lambda x: x[1][0])
        print(self.lane_lines)
