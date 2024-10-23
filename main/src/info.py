import pygame

pygame.init()

class Vocab:
    def __init__(self):
        # Fonts
        self.title_font = pygame.font.SysFont('Calibri', 40, True)
        self.subtitle_font = pygame.font.SysFont('Calibri', 30)
        self.body_font = pygame.font.SysFont('Calibri', 20)

        # Prepare the vocabulary sections
        self.keystone_species = [
            self.subtitle_font.render('Keystone Species', True, (0, 0, 0)),
            self.body_font.render('A keystone species is a species in an ecosystem', True, (0, 0, 0)),
            self.body_font.render('that the ecosystem relies on to stay stable.', True, (0, 0, 0))
        ]

        self.ecosystem = [
            self.subtitle_font.render('Ecosystems', True, (0, 0, 0)),
            self.body_font.render('An ecosystem is an interconnected collection of', True, (0, 0, 0)),
            self.body_font.render('organisms living in one area.', True, (0, 0, 0)),
        ]

        self.stability = [
            self.subtitle_font.render('Stability and Equilibrium', True, (0, 0, 0)),
            self.body_font.render('Stability and equilibrium are the terms used to', True, (0, 0, 0)),
            self.body_font.render('describe the balancing point in an ecosystem.', True, (0, 0, 0))
        ]

        self.human_impacts = [
            self.subtitle_font.render('Human Impacts', True, (0, 0, 0)),
            self.body_font.render('Human impacts are the effects of human', True, (0, 0, 0)),
            self.body_font.render('interaction in an ecosystem.', True, (0, 0, 0))
        ]

        self.biodiversity = [
            self.subtitle_font.render('Biodiversity', True, (0, 0, 0)),
            self.body_font.render('Biodiversity is the amount of different', True, (0, 0, 0)),
            self.body_font.render('species inside of an ecosystem.', True, (0, 0, 0))
        ]

        self.resilience = [
            self.subtitle_font.render('Resiliency', True, (0, 0, 0)),
            self.body_font.render('Resiliency is the ability to bounce back from', True, (0, 0, 0)),
            self.body_font.render('a time of struggle.', True, (0, 0, 0))
        ]

        self.back_button = self.body_font.render('Back', True, (0, 0, 0))
        self.next_button = self.body_font.render('Next', True, (0, 0, 0))

    def list_vocab(self, screen, window_size):
        # Colors
        black = (0, 0, 0)
        white = (255, 255, 255)

        # Title rendering
        title = self.title_font.render('Vocabulary', True, black)

        # All vocab sections grouped for easy iteration
        vocab_sections = [
            self.keystone_species,
            self.ecosystem,
            self.stability,
            self.human_impacts,
            self.biodiversity,
            self.resilience
        ]

        # Clear the screen and fill with white background
        screen.fill(white)

        # Center the title horizontally and blit it
        title_x = (window_size[0] - title.get_width()) // 2
        screen.blit(title, (title_x, 20))

        # Initial y-coordinate, below the title
        y = 100

        for i in range(len(vocab_sections) // 2):
            for line in vocab_sections[i]:
                screen.blit(line, (50, y))
                y += line.get_height() + 5
            y += 20

        y = 100
        
        for i in range(len(vocab_sections) // 2):
            for line in vocab_sections[i + (len(vocab_sections) // 2)]:
                screen.blit(line, (500, y))
                y += line.get_height() + 5
            y += 20

        screen.blit(self.back_button, (10, 10))
        screen.blit(self.next_button, (window_size[0] - 80, 10))

        # Update the display
        pygame.display.flip()

class HumanImpacts:
    def __init__(self):
        # Fonts
        self.title_font = pygame.font.SysFont('Calibri', 40, True)
        self.subtitle_font = pygame.font.SysFont('Calibri', 30)
        self.body_font = pygame.font.SysFont('Calibri', 20)

        # Text Sections for Human Impacts
        self.content = [
            self.title_font.render('Human Impacts', True, (0, 0, 0)),
            
            self.subtitle_font.render('Climate Change', True, (0, 0, 0)),
            self.body_font.render('Climate change destroys the tropical environments', True, (0, 0, 0)),
            self.body_font.render('that cassowaries live in, causing hundreds to die out.', True, (0, 0, 0)),
            self.body_font.render('This is one of the leading causes of broader impacts.', True, (0, 0, 0)),

            self.subtitle_font.render('Habitat Loss', True, (0, 0, 0)),
            self.body_font.render('Cassowaries lose their habitats due to climate change,', True, (0, 0, 0)),
            self.body_font.render('agricultural expansion, and deforestation.', True, (0, 0, 0)),
            self.body_font.render('These factors are deadly to both cassowaries and ecosystems.', True, (0, 0, 0)),

            self.subtitle_font.render('Motorway Accidents', True, (0, 0, 0)),
            self.body_font.render('55% of cassowary deaths result from being hit by cars.', True, (0, 0, 0)),
            self.body_font.render('Over half of all cassowaries will die after such accidents.', True, (0, 0, 0)),
            self.body_font.render('This is the largest human impact on cassowaries.', True, (0, 0, 0))
        ]

        self.back_button = self.body_font.render('Back', True, (0, 0, 0))

        

    def display_impacts(self, screen, window_size):
        # Clear the screen
        screen.fill((255, 255, 255))

        # Title positioning
        y = 30

        # Render and display each line of the content
        for line in self.content:
            screen.blit(line, (50, y))
            y += line.get_height() + 5  # Small gap between lines

        screen.blit(self.back_button, (10, 10))
        # Update the display
        pygame.display.flip()
