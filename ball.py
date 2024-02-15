import pygame
import random

class Ball:
    def __init__(self, x, y, dx, dy, diameter, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.diameter = diameter
        self.color = color

    def __del__(self):
        print("Object gets destroyed");

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, [[self.x, self.y], [self.diameter, self.diameter]])

    def update(self, screen_size, screen_border):
        self.x += self.dx
        self.y += self.dy

        # Check boundaries to ensure the bubble stays within the screen
        """
        if self.x < 0:
            self.x = 0
            self.dx = abs(self.dx)
        elif self.x > screen_size[0] - self.diameter:
            self.x = screen_size[0] - self.diameter
            self.dx = -abs(self.dx)
        """

        if self.y < 0:
            self.y = 0
            self.dy = abs(self.dy)
        elif self.y > screen_size[1] - screen_border - self.diameter:
            self.y = screen_size[1] - screen_border - self.diameter
            self.dy = -abs(self.dy)

    def check_collision(self, paddle, screen_size):
        radius = self.diameter / 2
        if self.x - radius < 100 and paddle.y < self.y < (paddle.y + paddle.height):
            self.dx = -self.dx
        elif (self.x + radius > ((screen_size[0] - 100) - paddle.width)
              and paddle.y < self.y < (paddle.y + paddle.height)):
            self.dx = -self.dx

    def check_point(self, screen_size, screen_border):
        pointp1 = 0
        pointp2 = 0
        if self.x <= 0:
            pointp1 += 1
            self.__del__()
            self.x = screen_size[0]/2
            self.y = (screen_size[1] - screen_border) / 2
            self.dx = random.choice([4, -4])
            self.dy = random.uniform(-2, 2)
            self.__init__(self.x, self.y, self.dx, self.dy, self.diameter, self.color)
        elif self.x + self.diameter >= screen_size[0]:
            pointp2 += 1
            self.__del__()
            self.x = screen_size[0] / 2
            self.y = (screen_size[1] - screen_border) / 2
            self.dx = random.choice([4, -4])
            self.dy = random.uniform(-2, 2)
            self.__init__(self.x, self.y, self.dx, self.dy, self.diameter, self.color)



