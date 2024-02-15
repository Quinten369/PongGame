import pygame

class Paddle:
    def __init__(self, x, sx, sy, color):
        self.x = x
        self.y = 100
        self.width = sx
        self.height = sy
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [[self.x, self.y], [self.width, self.height]])

    def update(self, screen_size, screen_border, pos):
        """# Get mouse y position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        self.y = mouse_y - self.height / 2"""

        self.y = pos

        if self.y < 0:
            self.y = 0
        elif self.y > screen_size[1] - screen_border - self.height:
            self.y = screen_size[1] - screen_border - self.height




