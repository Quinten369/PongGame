import pygame

class Ball:
    def __init__(self, x, y, dx, dy, diameter, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.diameter = diameter
        self.color = color

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, [[self.x, self.y], [self.diameter, self.diameter]])

    def update(self, screen_size, screen_border):
        self.x += self.dx
        self.y += self.dy

        # Check boundaries to ensure the bubble stays within the screen
        if self.x < 0:
            self.x = 0
            self.dx = abs(self.dx)
        elif self.x > screen_size[0] - self.diameter:
            self.x = screen_size[0] - self.diameter
            self.dx = -abs(self.dx)

        if self.y < 0:
            self.y = 0
            self.dy = abs(self.dy)
        elif self.y > screen_size[1] - screen_border - self.diameter:
            self.y = screen_size[1] - screen_border - self.diameter
            self.dy = -abs(self.dy)

