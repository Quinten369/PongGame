import pygame

class Paddle:
    def __init__(self, x, sx, sy, color):
        # Initializes a paddle object with given parameters
        self.x = x
        self.y = 100
        self.width = sx
        self.height = sy
        self.color = color

    def draw(self, screen):
        # Draws the paddle on the screen
        pygame.draw.rect(screen, self.color, [[self.x, self.y], [self.width, self.height]])

    def update(self, screen_size, screen_border, pos):
        # Updates the position of the paddle and handles collisions with the screen borders
        self.y = pos

        if self.y < 0:
            self.y = 0
        elif self.y > screen_size[1] - screen_border - self.height:
            self.y = screen_size[1] - screen_border - self.height




