import pygame

class Paddle:
    def __init__(self, x, sX, sY, color):
        self.x = x
        self.y = 100
        self.width = sX
        self.height = sY
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [[self.x, self.y], [self.width, self.height]])

    def update(self, screen_size, screen_border):
        # Get mouse y position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        self.y = mouse_y - self.height / 2

        if self.y < 0:
            self.y = 0
        elif self.y > screen_size - screen_border - self.height:
            self.y = screen_size - screen_border - self.height




