import pygame
import random
from ball import Ball
from paddle import Paddle
from TSPDecoder import TSPDecoder  # Import the TSPDecoder class

def main():
    size = (1000, 800)
    border = 100
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    ballX = size[0] / 2
    ballY = (size[1] - border) / 2
    ballXspeed = random.choice([4, -4])
    ballYspeed = random.uniform(-2, 2)
    p1pos = size[1] / 2
    p2pos = size[1] / 2
    diameter = 25
    threshold = 50
    grid_size = (size[0], size[1] - border)

    pygame.init()
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    # Create a Ball and Paddle object
    b = Ball(ballX, ballY, ballXspeed, ballYspeed, diameter, green)
    p1 = Paddle(100, 15, 100, red)
    p2 = Paddle(size[0] - 100, 15, 100, red)

    # Initialize the TSPDecoder instance
    tsp_decoder = TSPDecoder()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Update the position of the bubble
        b.update(size, border)
        p1.update(size, border, p1pos)
        p2.update(size, border, p2pos)
        b.check_collision(p1, size)
        b.check_collision(p2, size)
        b.check_point(size, border)

        # Get the current frame data from the touchpad
        frame = tsp_decoder.readFrame()

        # Iterate over the frame data to detect touches
        for row in range(min(grid_size[0], len(frame))):
            for column in range(min(grid_size[1] - border, len(frame[0]))):
                # If a cell is touched, do something
                if frame[row][column] > threshold:
                    # Here you can implement the logic to handle the touch
                    if column < len(frame[0]) // 2:
                        p1pos = row * 20
                    else:
                        p2pos = row * 20

        # Draw the canvas and bubble
        screen.fill((8, 143, 143))
        pygame.draw.rect(screen, black, [[0, 0], [size[0], size[1] - border]])

        # Call the draw method of the Bubble object
        b.draw(screen)
        p1.draw(screen)
        p2.draw(screen)

        # Update the entire canvas
        pygame.display.flip()
        # Limit the frame rate
        clock.tick(60)

if __name__ == "__main__":
    main()
