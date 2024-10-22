import pygame
import sys
import random
from game_init import GameInitializer

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
        self.initializer = GameInitializer(
            r'main\src\assets\car.png',
            r'main\src\assets\heavy_forest_tile_1.png',
            r'main\src\assets\heavy_forest_tile_2.png',
            r'main\src\assets\heavy_forest_tile_3.png',
            r'main\src\assets\heavy_forest_tile_4.png',
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
            pygame.transform.scale_by(self.initializer.heavy_forest_tile_1_unscaled, 4),
            pygame.transform.scale_by(self.initializer.heavy_forest_tile_2_unscaled, 4),
            pygame.transform.scale_by(self.initializer.heavy_forest_tile_3_unscaled, 4),
            pygame.transform.scale_by(self.initializer.heavy_forest_tile_4_unscaled, 4)
        ]

        self.tiles = self.initializer.tiles
        self.lane_lines = self.initializer.lane_lines
        self.lane_amount = self.initializer.lane_amount

        self.car = self.Car()
        self.cassowary = self.Cassowary()
        self.is_game_started = False

        self.polygon_points = []
    class Car:

        def __init__(self):
            self.lane = 0
            self.pos = None

        def check_collision(self):
            to_remove = []  # List to store positions to remove
            car_width = 42   # Width of the car
            car_height = 32  # Height of the car
            cassowary_width = 32  # Width of the cassowary
            cassowary_height = 32  # Height of the cassowary
            
            for cassowary_pos in game.cassowary.pos:
                # Calculate the edges of the car
                car_left = self.pos[0]
                car_right = self.pos[0] + car_width
                car_top = self.pos[1]
                car_bottom = self.pos[1] + car_height
                
                # Calculate the edges of the cassowary
                cassowary_left = cassowary_pos[0]
                cassowary_right = cassowary_pos[0] + cassowary_width
                cassowary_top = cassowary_pos[1]
                cassowary_bottom = cassowary_pos[1] + cassowary_height
                
                # Check for collision
                if (car_left < cassowary_right and car_right > cassowary_left and 
                    car_top < cassowary_bottom and car_bottom > cassowary_top):
                    to_remove.append(cassowary_pos)  # Mark for removal

            # Now remove all cassowaries that collided
            for cassowary in to_remove:
                game.cassowary.pos.remove(cassowary)
                game.cassowary.deaths += 1

    class Cassowary:

        def __init__(self):
            self.speed_x = 8
            self.speed_y = 4
            self.frequency = 5
            self.pos = []
            self.deaths = 0

        def spawn(self):
            if random.randint(1, round(100 / self.frequency)) == 1:
                spawn_side = random.choice([0, window_size[0] - 32])
                spawn_y = random.randint(window_size[1] // 10, window_size[1] // 2)
                self.pos.append([spawn_side, spawn_y, 1, 1 if spawn_side == 0 else -1])

        def run(self):
            for pos in self.pos:
                pos[0] += self.speed_x * pos[3]
                # If the cassowary has moved off-screen, remove it
                if pos[0] < -32 or pos[0] > window_size[0]:  # Assuming cassowary width is around 32
                    self.pos.remove(pos)

    def boot(self):
        font = pygame.font.SysFont('Comic Sans MS', 30)
        title_text = font.render('Cassowaries', False, (0, 0, 0))
        start_button = font.render('Start Game', False, (255, 0, 0))

        screen.blit(title_text, (200, 20))
        screen.blit(start_button, (200, 80))

    def start(self):
        self.is_game_started = True
        screen.fill((255, 255, 255))
        self.car.pos = (self.lane_lines[self.car.lane][1][0] + 60, window_size[1] - 72)

    def update(self):
        if self.is_game_started:
            screen.fill((255, 255, 255))  # Clear the screen

            # Draw background tiles
            for x, y in self.tiles:
                tile_surface = random.choice(self.forest_tiles)
                screen.blit(tile_surface, (x, y))

            # Draw the road polygon
            self.polygon_points = [
                ((window_size[0] // 2) - ((self.lane_amount / 2) * 200), window_size[1]),
                ((window_size[0] // 2) + ((self.lane_amount / 2) * 200), window_size[1]),
                (window_size[0] // 2, 0)
            ]
            pygame.draw.polygon(screen, (122, 122, 122), self.polygon_points)

            # Draw lanes
            for line in self.lane_lines:
                pygame.draw.line(screen, (0, 0, 0), line[0], line[1], 1)

            # Draw cassowaries            
            for i in range(len(self.cassowary.pos)):
                sprite = self.cassowary_sprites[self.cassowary.pos[i][2] % len(self.cassowary_sprites)]
                
                # Flip the sprite based on position
                if self.cassowary.pos[i][3] == 1:  # If the cassowary is on the left side
                    screen.blit(sprite, (self.cassowary.pos[i][0], self.cassowary.pos[i][1]))
                else:  # If the cassowary is on the right side
                    flipped_sprite = pygame.transform.flip(sprite, True, False)  # Flip horizontally
                    screen.blit(flipped_sprite, (self.cassowary.pos[i][0], self.cassowary.pos[i][1]))


            # Update car position
            self.car.pos = (self.lane_lines[self.car.lane][1][0] + 60, window_size[1] - 72)
            screen.blit(self.car_sprite, self.car.pos)


game = Game()

class Animations:
    def drive(self):
        speed = 8
        for i, (x, y) in enumerate(game.tiles):
            new_y = y + speed
            if new_y >= window_size[1]:
                new_y -= window_size[1] + 128
            game.tiles[i] = (x, new_y)

        for pos in game.cassowary.pos:
            pos[1] += game.cassowary.speed_y
            pos[2] = (pos[2] + 1) % len(game.cassowary_sprites)

animations = Animations()
game.boot()

# Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if 200 <= event.pos[0] <= 360 and 80 <= event.pos[1] <= 120:
                game.start()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and game.car.lane < game.lane_amount - 1:
                game.car.lane += 1
            elif event.key == pygame.K_LEFT and game.car.lane > 0:
                game.car.lane -= 1

    if game.is_game_started:
        animations.drive()
        game.cassowary.run()
        game.cassowary.spawn()
        game.car.check_collision()
        game.update()

    pygame.display.flip()
    clock.tick(60)