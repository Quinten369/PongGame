import pygame
from ball import Ball
from paddle import Paddle


def main():
    size = (1000, 800)
    border = 100
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    ballX = 100
    ballY = 100
    ballXspeed = 1
    ballYspeed = 2
    diameter = 50

    pygame.init()
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    # Create a Bubble object
    b = Ball(ballX, ballY, ballXspeed, ballYspeed, diameter, green)
    b2 = Ball(20, 20, 1, 1, 20, green)
    p1 = Paddle(100, 10, 50, red)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Update the position of the bubble
        b.update(size, border)
        b2.update(size, border)



        # Draw the canvas and bubble
        screen.fill((8, 143, 143))
        pygame.draw.rect(screen, black, [[0, 0], [size[0], size[1] - border]])

        # Call the draw method of the Bubble object
        b.draw(screen)
        b2.draw(screen)
        p1.draw(screen)


        # Update the entire canvas
        pygame.display.flip()
        # Limit the frame rate
        clock.tick(60)


if __name__ == "__main__":
    main()
