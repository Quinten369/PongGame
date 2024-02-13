import pygame

class Paddle:
    def __init__(self, x, sX, sY, color):
        self.x = x
        self.width = sX
        self.height = sY
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [[self.x, 100], [self.width, self.height]])

    def update(self, screen_size, screen_border):
        self.x = self.x

