import pygame
import random
from ball import Ball
from paddle import Paddle
from TSPDecoder import TSPDecoder

def main():
    # Define game parameters
    size = (1000, 800)
    border = 100
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    ballX = size[0] / 2
    ballY = (size[1] - border) / 2
    ballXspeed = random.choice([4, -4])
    ballYspeed = random.uniform(-2, 2)
    point_player_1 = 0
    point_player_2 = 0
    p1pos = size[1] / 2
    p2pos = size[1] / 2
    radius = 20
    high_left = float("-inf")
    high_right = float("-inf")
    left_pos = None
    right_pos = None
    grid_size = (size[0], size[1] - border)

    pygame.init()
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    # Create a Ball and Paddle object
    b = Ball(ballX, ballY, ballXspeed, ballYspeed, radius, green)
    p1 = Paddle(100, 15, 100, red)
    p2 = Paddle(size[0] - 100, 15, 100, red)

    # Initialize the TSPDecoder instance
    tsp_decoder = TSPDecoder()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Update the game objects
        b.update(size, border)
        p1.update(size, border, p1pos)
        p2.update(size, border, p2pos)
        b.check_collision(p1, p2)

        # Get the current frame data from the touchpad
        frame = tsp_decoder.readFrame()

        # Detect touches on the touchpad
        for row in range(min(grid_size[0], len(frame))):
            for column in range(min(grid_size[1] - border, len(frame[0]))):
                if column < len(frame[0]) // 2:  # Left half of the touchpad
                    if frame[row][column] > high_left:  # Detect touch intensity
                        high_left = frame[row][column]  # Update highest vallue
                        left_pos = row * 25  # Calculate position of touch
                elif column >= len(frame[0]) // 2:  # Right half of the touchpad
                    if frame[row][column] > high_right:  # Detect touch intensity
                        high_right = frame[row][column]  # Update highest vallue
                        right_pos = row * 25  # Calculate position of touch

        # Update paddle positions based on detected touches and reset for next frame
        p1pos = left_pos
        p2pos = right_pos
        high_left = 0
        high_right = 0

        # Draw the canvas
        screen.fill((8, 143, 143))
        pygame.draw.rect(screen, black, [[0, 0], [size[0], size[1] - border]])

        # Call the draw method of the ball and paddles object
        b.draw(screen)
        p1.draw(screen)
        p2.draw(screen)

        # Check if the game is over and update events
        if point_player_1 < 5 and point_player_2 < 5:
            font = pygame.font.SysFont('Times', 50)
            text_p1 = font.render(f"Player 1: {point_player_1}     Player 2: {point_player_2}", True, (255, 255, 255))
            if b.check_point_1(size):
                point_player_1 += 1
                b.reset_ball(size, border)

            if b.check_point_2():
                point_player_2 += 1
                b.reset_ball(size, border)
        else:
            text_p1 = font.render(f"Game Over", True, (255, 255, 255))

        text_rect = text_p1.get_rect(center=(size[0] // 2, size[1] - border // 2 - 10))
        screen.blit(text_p1, text_rect)

        # Update the entire canvas
        pygame.display.flip()
        # Limit the frame rate
        clock.tick(60)

if __name__ == "__main__":
    main()