import pygame
import sys
import random
from game_init import GameInitializer
from info import Vocab, HumanImpacts

pygame.init()
pygame.font.init()

def screen_init():
    global screen, window_size, clock

    window_size = (1024, 640)
    icon_path = r'main\src\assets\icon.png'

    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption('Keystone Game')

    icon = pygame.image.load(icon_path)
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()

    screen.fill((255, 255, 255))

screen_init()

class Game:
    def __init__(self):
        self.difficulty_levels = ['easy', 'normal', 'hard', 'impossible', 'for the love of god don\'t play this']
        self.difficulty_index = 0  # Start with 'easy'
        
        self.initializer = GameInitializer(
            r'main\src\assets\car.png',
            r'main\src\assets\backdrops\heavy_forest\heavy_forest_tile_1.png',
            r'main\src\assets\backdrops\heavy_forest\heavy_forest_tile_2.png',
            r'main\src\assets\backdrops\heavy_forest\heavy_forest_tile_3.png',
            r'main\src\assets\backdrops\heavy_forest\heavy_forest_tile_4.png',
            r'main\src\assets\backdrops\dying_forest\dying_forest_tile_1.png',
            r'main\src\assets\backdrops\dying_forest\dying_forest_tile_2.png',
            r'main\src\assets\backdrops\dying_forest\dying_forest_tile_3.png',
            r'main\src\assets\backdrops\dying_forest\dying_forest_tile_4.png',
            r'main\src\assets\backdrops\dirt.png',
            r'main\src\assets\frames\cassowary\running\cassowary_running_1.png',
            r'main\src\assets\frames\cassowary\running\cassowary_running_2.png',
            r'main\src\assets\frames\cassowary\running\cassowary_running_3.png',
            r'main\src\assets\frames\cassowary\running\cassowary_running_4.png',
            r'main\src\assets\frames\cassowary\running\cassowary_running_5.png',
            r'main\src\assets\frames\cassowary\running\cassowary_running_6.png',
            window_size
        )

        self.car_sprite = pygame.transform.scale2x(self.initializer.car_unscaled)
        self.cassowary_sprites = [
            pygame.transform.scale2x(self.initializer.cassowary_running_1_unscaled),
            pygame.transform.scale2x(self.initializer.cassowary_running_2_unscaled),
            pygame.transform.scale2x(self.initializer.cassowary_running_3_unscaled),
            pygame.transform.scale2x(self.initializer.cassowary_running_4_unscaled),
            pygame.transform.scale2x(self.initializer.cassowary_running_5_unscaled),
            pygame.transform.scale2x(self.initializer.cassowary_running_6_unscaled)
        ]
        self.forest_tiles = [
            [
                pygame.transform.scale_by(self.initializer.heavy_forest_tile_1_unscaled, 4),
                pygame.transform.scale_by(self.initializer.heavy_forest_tile_2_unscaled, 4),
                pygame.transform.scale_by(self.initializer.heavy_forest_tile_3_unscaled, 4),
                pygame.transform.scale_by(self.initializer.heavy_forest_tile_4_unscaled, 4)
            ],
            [
                pygame.transform.scale_by(self.initializer.dying_forest_tile_1_unscaled, 4),
                pygame.transform.scale_by(self.initializer.dying_forest_tile_2_unscaled, 4),
                pygame.transform.scale_by(self.initializer.dying_forest_tile_3_unscaled, 4),
                pygame.transform.scale_by(self.initializer.dying_forest_tile_4_unscaled, 4)
            ]
        ]

        self.forest_stage = 0

        self.dirt_tile = pygame.transform.scale_by(self.initializer.dirt_unscaled, 4)

        self.tiles = self.initializer.tiles
        self.lane_lines = self.initializer.lane_lines
        self.lane_amount = self.initializer.lane_amount
        self.score = 0

        self.car = self.Car()
        self.cassowary = self.Cassowary()
        self.is_game_started = False

        self.polygon_points = []
        
    class Car:
        def __init__(self):
            self.lane = 0
            self.pos = None

        def check_collision(self):
            to_remove = []
            car_width = 42
            car_height = 32
            cassowary_width = 32
            cassowary_height = 32

            for cassowary_pos in game.cassowary.pos:
                car_left = self.pos[0]
                car_right = self.pos[0] + car_width
                car_top = self.pos[1]
                car_bottom = self.pos[1] + car_height
                
                cassowary_left = cassowary_pos[0]
                cassowary_right = cassowary_pos[0] + cassowary_width
                cassowary_top = cassowary_pos[1]
                cassowary_bottom = cassowary_pos[1] + cassowary_height

                if (car_left < cassowary_right and car_right > cassowary_left and 
                    car_top < cassowary_bottom and car_bottom > cassowary_top):
                    to_remove.append(cassowary_pos)

            for cassowary in to_remove:
                game.cassowary.pos.remove(cassowary)
                game.cassowary.deaths += 1
                game.score -= 10000

    class Cassowary:
        def __init__(self):
            self.speed_x = None
            self.speed_y = None
            self.frequency = None
            self.pos = []
            self.deaths = 0

        def spawn(self):
            if self.frequency != 0:
                if random.randint(1, round(100 / self.frequency)) == 1:
                    spawn_side = random.choice([0, window_size[0] - 32])
                    spawn_y = random.randint(window_size[1] // 10, window_size[1] // 2)
                    self.pos.append([spawn_side, spawn_y, 0, 1 if spawn_side == 0 else -1])

        def run(self):
            for pos in self.pos:
                pos[0] += self.speed_x * pos[3]
                if pos[0] < -32 or pos[0] > window_size[0]:
                    self.pos.remove(pos)

    def boot(self):
        self.render_start_screen()

    def render_start_screen(self):
        screen.fill((255, 255, 255))  # Fill the screen with white

        font = pygame.font.SysFont('Comic Sans MS', 50)
        title_text = font.render('Cassowaries', True, (173, 216, 230))  # Light blue
        start_button_font = pygame.font.SysFont('Comic Sans MS', 30)
        start_button = start_button_font.render('Start Game', True, (255, 0, 0))  # Red

        # Render the difficulty text
        self.difficulty_text = start_button_font.render(self.difficulty_levels[self.difficulty_index], True, (0, 0, 0))

        screen.blit(title_text, (200, 20))
        screen.blit(start_button, (window_size[0] - 250, 80))
        screen.blit(self.difficulty_text, (window_size[0] - 200, 160) if self.difficulty_index != 4 else (window_size[0] - 600, 160))

        # Draw arrows
        left_arrow = start_button_font.render('<', True, (0, 0, 0))
        right_arrow = start_button_font.render('>', True, (0, 0, 0))
        screen.blit(left_arrow, (window_size[0] - 250, 160))  # Left arrow
        screen.blit(right_arrow, (window_size[0] - 100, 160))  # Right arrow

        info_font = pygame.font.SysFont('Comic Sans MS', 25)
        info_button = info_font.render('Click For Information', True, (0, 0, 0))

        screen.blit(info_button, (215, 80))

    def change_difficulty(self, direction):
        # Change the difficulty index based on arrow direction
        if direction == 'left':
            self.difficulty_index = (self.difficulty_index - 1) % len(self.difficulty_levels)
        elif direction == 'right':
            self.difficulty_index = (self.difficulty_index + 1) % len(self.difficulty_levels)
        # Update the difficulty text
        self.render_start_screen()  # Re-render the start screen to show the updated difficulty text

    def boot_info(self):
        screen.fill((255, 255, 255))
        vocab = Vocab()
        
        self.on_vocab = True
        vocab.list_vocab(screen, window_size)

    def boot_human_impacts(self):
        screen.fill((255, 255, 255))
        human_impacts = HumanImpacts()

        self.on_human_impacts = True
        human_impacts.display_impacts(screen, window_size)

    def start(self):
        self.is_game_started = True
        screen.fill((255, 255, 255))  # Fill the screen white for the game screen
        self.car.pos = (self.lane_lines[self.car.lane][1][0] + 60, window_size[1] - 72)
        print(self.difficulty_index)
        game.cassowary.speed_x = 6 if game.difficulty_index == 0 else 8 if game.difficulty_index == 1 else 12 if game.difficulty_index == 2 else 16 if game.difficulty_index == 3 else 32
        game.cassowary.speed_y = 4 if game.difficulty_index == 0 else 4 if game.difficulty_index == 1 else 8 if game.difficulty_index == 2 else 10 if game.difficulty_index == 3 else 16
        game.cassowary.frequency = 1 if game.difficulty_index == 0 else 2 if game.difficulty_index == 1 else 5 if game.difficulty_index == 2 else 7 if game.difficulty_index == 3 else 15
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def update(self):
        if self.is_game_started:
            screen.fill((255, 255, 255))  # Clear screen for game update

            for ((x, y), value) in self.tiles:
                screen.blit(self.dirt_tile, (x, y))
            if self.forest_stage != 2:
                for ((x, y), value) in self.tiles:
                    screen.blit(self.forest_tiles[self.forest_stage][value - 1], (x, y))

            self.polygon_points = [
                ((window_size[0] // 2) - ((self.lane_amount / 2) * 200), window_size[1]),
                ((window_size[0] // 2) + ((self.lane_amount / 2) * 200), window_size[1]),
                (window_size[0] // 2, 0)
            ]
            pygame.draw.polygon(screen, (122, 122, 122), self.polygon_points)

            for line in self.lane_lines:
                pygame.draw.line(screen, (0, 0, 0), line[0], line[1], 1)

            for i in range(len(self.cassowary.pos)):
                sprite = self.cassowary_sprites[self.cassowary.pos[i][2]]

                if self.cassowary.pos[i][3] == 1:
                    screen.blit(sprite, (self.cassowary.pos[i][0], self.cassowary.pos[i][1]))
                else:
                    flipped_sprite = pygame.transform.flip(sprite, True, False)
                    screen.blit(flipped_sprite, (self.cassowary.pos[i][0], self.cassowary.pos[i][1]))

            self.car.pos = (self.lane_lines[self.car.lane][1][0] + 60, window_size[1] - 72)
            screen.blit(self.car_sprite, self.car.pos)

            score_text = self.font.render(f'Score: {self.score}', False, (0, 0, 0))
            screen.blit(score_text, (10, 10))

    def end_game(self):
        """Renders the game over screen."""
        font = pygame.font.SysFont('Comic Sans MS', 50)
        game_over_text = font.render('Game Over', True, (255, 0, 0))
        score_text = self.font.render(f'Final Score: {self.score}', True, (0, 0, 0))

        screen.blit(game_over_text, (window_size[0] // 2 - 100, window_size[1] // 2 - 50))
        screen.blit(score_text, (window_size[0] // 2 - 100, window_size[1] // 2 - 100))

game = Game()

class Animations:
    def __init__(self):
        self.scroll_speed = 8 if game.difficulty_index == 0 else 10 if game.difficulty_index == 1 else 16 if game.difficulty_index == 2 else 20 if game.difficulty_index == 3 else 40
        self.tile_size = 256

        # Calculate rows and columns, including extra rows for seamless looping
        self.rows = (window_size[1] // self.tile_size) + 2  # One extra row for smooth looping
        self.cols = window_size[0] // self.tile_size  # Fill the width exactly

        self.initialize_tiles()

    def initialize_tiles(self):
        game.tiles = []
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * self.tile_size
                y = row * self.tile_size
                value = random.randint(1, 4)  # Random tile value for diversity
                game.tiles.append(((x, y), value))

    def drive(self):
        for i, ((x, y), value) in enumerate(game.tiles):
            # Move the tile downward
            new_y = y + self.scroll_speed

            # If the tile moves completely out of view, wrap it back to the top
            if new_y >= window_size[1]:
                new_y -= self.rows * self.tile_size  # Wrap above the visible area

            # Update the tile position
            game.tiles[i] = ((x, new_y), value)

        for i in range(len(game.cassowary.pos)):
            game.cassowary.pos[i][1] += game.cassowary.speed_y
            if game.cassowary.pos[i][2] < 5:
                game.cassowary.pos[i][2] += 1
            else:
                game.cassowary.pos[i][2] = 0

animations = Animations()
game.boot()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if window_size[0] - 250 <= event.pos[0] <= window_size[0] - 100 and 80 <= event.pos[1] <= 120 and not game.is_game_started:
                game.start()
            elif window_size[0] - 250 <= event.pos[0] <= window_size[0] - 200 and 160 <= event.pos[1] <= 200 and not game.is_game_started:
                game.change_difficulty('left')
            elif window_size[0] - 100 <= event.pos[0] <= window_size[0] - 50 and 160 <= event.pos[1] <= 200 and not game.is_game_started:
                game.change_difficulty('right')
            elif event.pos[0] in range(215, 470) and event.pos[1] in range(80, 105):
                game.boot_info()
            elif event.pos[0] in range(10, 70) and event.pos[1] in range(10, 40) and game.on_vocab:
                game.boot()
            elif event.pos[0] in range(window_size[0] - 80, window_size[0] - 10) and event.pos[1] in range(10, 40) and game.on_vocab:
                game.boot_human_impacts()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and game.car.lane < game.lane_amount - 1:
                game.car.lane += 1
            elif event.key == pygame.K_LEFT and game.car.lane > 0:
                game.car.lane -= 1

    if game.is_game_started:
        game.score += (game.cassowary.deaths * game.cassowary.deaths * (game.difficulty_index + 1))
        if game.cassowary.deaths in range(10, 20):
            game.forest_stage = 1
        elif game.cassowary.deaths >= 20:
            game.forest_stage = 2
            game.cassowary.frequency = 0
            game.is_game_started = False
            game.end_game()
        animations.drive()
        game.cassowary.run()
        game.cassowary.spawn()
        game.car.check_collision()
        game.update()

    pygame.display.flip()
    clock.tick(60)
