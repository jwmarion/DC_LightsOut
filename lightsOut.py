#project 1b 'lights out'
import pygame

grid = [[False]*5]*5

# def drawGrid(screen):



def main():
    width = 800
    height = 600
    blue_color = (97, 159, 182)
    black_color = (255,255,255)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Draw background
        screen.fill(blue_color)

        grid[1][2] = True
        # grid [2][1] = True
        for x in range(5):
            for y in range(5):
                pygame.draw.rect(screen, (0,0,0),  ((10+(x * 100)),  (10 + (y * 100)),   100,   100), 4)
                if grid[x][y] == True:
                    pygame.draw.rect(screen, (159, 59, 164),  ((10+(x * 100)),  (10 + (x * 100)),   100,   100))


        # Game display

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
