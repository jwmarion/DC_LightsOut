#project 1b 'lights out'
import pygame, math

grid = [[-1]*5 for x in range(5)]


def getButton(x,y): #turns inputs into cooresponding button
    if x > 10 and x < 500 and y > 10 and y < 500:
        x = (int(math.floor(x / 100.0)) * 100) /100
        y = (int(math.floor(y / 100.0)) * 100) /100
    return (x,y)

def setLights(x,y):


    if x != 4:
        grid[x + 1][y] = grid[x + 1][y] * -1
    if x != 0:
        grid[x - 1][y] = grid[x - 1][y] * -1

    if y != 4:
        grid[x][y + 1] = grid[x][y + 1] * -1
    if y != 0:
        grid[x][y - 1] = grid[x ][y- 1] * -1

    if grid[x][y] == 1:
        grid[x][y] =  -1
    elif grid[x][y] == -1:
        grid[x][y] = 1

def setLevel(level):
    # global grid
    if level == 1:
        grid[0][2] = 1
        grid[2][2] = 1
        grid[4][2] = 1

    if level == 2:
        grid[0][0] = 1
        grid[0][1] = 1
        grid[0][3] = 1
        grid[0][4] = 1

        grid[2][0] = 1
        grid[2][1] = 1
        grid[2][3] = 1
        grid[2][4] = 1

    if level == 3:
        grid[0][1] = 1
        grid[0][2] = 1
        grid[0][3] = 1

        grid[1][0] = 1
        grid[1][1] = 1
        grid[1][2] = 1
        grid[1][3] = 1
        grid[1][4] = 1

        grid[3][1] = 1
        grid[3][2] = 1
        grid[3][3] = 1
        grid[3][4] = 1

        grid[4][1] = 1
        grid[4][2] = 1
        grid[4][3] = 1

    if level == 4:
        grid[0][1] = 1
        grid[0][3] = 1
        grid[0][4] = 1

        grid[1][1] = 1
        grid[1][4] = 1

        grid[3][1] = 1
        grid[3][4] = 1

        grid[4][1] = 1
        grid[4][3] = 1
        grid[4][4] = 1

    if level == 5:
        grid[0][0] = 1
        grid[0][1] = 1
        grid[0][2] = 1
        grid[0][4] = 1

        grid[1][0] = 1
        grid[1][1] = 1
        grid[1][2] = 1
        grid[1][4] = 1

        grid[2][0] = 1
        grid[2][1] = 1
        grid[2][2] = 1

        grid[3][0] = 1
        grid[3][3] = 1
        grid[3][4] = 1

        grid[4][1] = 1
        grid[4][2] = 1
        grid[4][3] = 1
        grid[4][4] = 1

def main():
    #colors and variables
    width = 520
    height = 600
    blue_color = (147, 148, 150)
    black_color = (255,255,255)
    level = 1
    #inits
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()
    inProgress = False
    #text
    font = pygame.font.Font(None, 25)
    resetText = font.render("Reset", True, (0,0,0))
    levelText = font.render("Level: %d" % level, True, (0,0,0))
    quitText = font.render("Quit", True, (0,0,0))

    background_image = pygame.image.load('/media/river.jpg').convert_alpha()
    fly_image = pygame.image.load('/images/fly.png').convert_alpha()
    tile_image = pygame.image.load('/images/wood.png').convert_alpha()
    # Game initialization


    stop_game = False
    while not stop_game:
        levelText = font.render("Level: %d" % level, True, (0,0,0))
        if inProgress == False:
            setLevel(level)
            inProgress = True




        #Event handling
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                #setLights(getButton(x),getButton(y))
                if y > 510:
                    if x >= 10 and x <=170 and y >= 520 and y <= 590:
                        setLevel(level)
                    if x >=180 and x <= 340 and y >= 520 and y <=590:
                        pass
                    if x >= 350 and x <= 510 and y >= 520 and y <=590:
                        pygame.quit()
                else:
                    t = getButton(x,y)
                    setLights(t[0],t[1])



            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Draw background
        screen.fill(blue_color)
        screen.blit(background_image, (0,0))

        testWin = 0
        for x in range(0,5):
            for y in range(0,5):
                pygame.draw.rect(screen, (0,0,0),  ((10+(x * 100)),  (10 + (y * 100)),   100,   100), 4)
                if (grid[x][y]) == 1:
                    pygame.draw.rect(screen, (159, 59, 164),  ((10+(x * 100)),  (10 + (y * 100)),   100,   100))
                    testWin += 1

        pygame.draw.rect(screen, (61, 104, 177), (10,520, 160,70))
        pygame.draw.rect(screen, (61, 104, 177), (180,520, 160,70))
        pygame.draw.rect(screen, (61, 104, 177), (350,520, 160,70))

        screen.blit(resetText, (65,550 ))
        screen.blit(levelText, (240,550 ))
        screen.blit(quitText, (405,550 ))

        if testWin == 0:
            level += 1
            inProgress = False
            #win

        # Game display

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
