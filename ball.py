import pygame
import random

class Ball:
    # points variable
    point_player_1 = 0
    point_player_2 = 0

    def __init__(self, x, y, dx, dy, radius, color):
        # Initializes a Ball object with given parameters
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.color = color

    def __del__(self):
        print("Object gets destroyed");

    def draw(self, screen):
        # Draws the ball on the screen
        pygame.draw.ellipse(screen, self.color, [[self.x, self.y], [self.radius * 2, self.radius * 2]])

    def update(self, screen_size, screen_border):
        # Updates the position of the ball and handles collisions with the screen borders
        self.x += self.dx
        self.y += self.dy

        # Handle collisions with top and bottom borders
        if self.y < 0:
            self.y = 0
            self.dy = abs(self.dy)
        elif self.y > screen_size[1] - screen_border - self.radius * 2:
            self.y = screen_size[1] - screen_border - self.radius * 2
            self.dy = -abs(self.dy)

    def check_collision(self, left_paddle, right_paddle):
        # Checks for collisions between the ball and the paddles
        max_vel = 5
        if self.dx < 0:  # Ball is moving left
            if left_paddle.x <= self.x <= left_paddle.x + left_paddle.width:
                if left_paddle.y <= self.y + self.radius <= left_paddle.y + left_paddle.height or left_paddle.y <= self.y <= left_paddle.y + left_paddle.height:
                    # Change direction of the ball
                    self.dx *= -1

                    # Calculate the vertical velocity based on where the ball hit the paddle
                    middle_y = left_paddle.y + left_paddle.height / 2
                    difference_in_y = middle_y - self.y
                    reduction_factor = (left_paddle.height / 2) / max_vel
                    self.dy = difference_in_y / reduction_factor
                    self.dy = -1 * self.dy
        else:  # Ball is moving right
            if right_paddle.x <= self.x + self.radius * 2 <= right_paddle.x + right_paddle.width:
                if right_paddle.y <= self.y + self.radius <= right_paddle.y + right_paddle.height or right_paddle.y <= self.y <= right_paddle.y + right_paddle.height:
                    # Change direction of the ball
                    self.dx *= -1

                    # Calculate the vertical velocity based on where the ball hit the paddle
                    middle_y = right_paddle.y + right_paddle.height / 2
                    difference_in_y = middle_y - self.y
                    reduction_factor = (right_paddle.height / 2) / max_vel
                    self.dy = difference_in_y / reduction_factor
                    self.dy = -1 * self.dy

    def check_point_1(self, screen_size):
        # Checks if the ball has passed player 1's paddle and scored a point
        if self.x + self.radius * 2 >= screen_size[0]:
            return True
        return False

    def check_point_2(self):
        # Checks if the ball has passed player 1's paddle and scored a point
        if self.x <= 0:
            return True
        return False

    def reset_ball(self, screen_size, screen_border):
        # Resets the position and velocity of the ball
        self.x = screen_size[0] / 2
        self.y = (screen_size[1] - screen_border) / 2
        self.dx = random.choice([4, -4])  # Randomly choose initial horizontal velocity
        self.dy = random.uniform(-2, 2)    # Randomly choose initial vertical velocity
