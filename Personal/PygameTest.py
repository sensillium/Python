import pygame, sys
import random
from pygame.locals import *

# constants representing colours
BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# constants representing the different resources
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3

# a dictionary linking resources to colours
textures = {
    DIRT : pygame.image.load(r"D:\OneDrive\Workspace\local\python\Personal\dirt.png"),
    GRASS : pygame.image.load(r"D:\OneDrive\Workspace\local\python\Personal\grass.png"),
    WATER : pygame.image.load(r"D:\OneDrive\Workspace\local\python\Personal\water.png"),
    COAL : pygame.image.load(r"D:\OneDrive\Workspace\local\python\Personal\coal.png")
}

inventory = {
    DIRT : 0,
    GRASS : 0,
    WATER : 0,
    COAL : 0
}

# a list representing our tilemap
tilemap = [
    [GRASS, COAL, DIRT],
    [WATER, WATER, GRASS],
    [COAL, GRASS, WATER],
    [DIRT, GRASS, COAL],
    [GRASS, WATER, DIRT]
]

# useful game dimensions
TILESIZE = 40
MAPWIDTH = 30
MAPHEIGHT = 20

# the player image
PLAYER = pygame.image.load(r"D:\OneDrive\Workspace\local\python\Personal\player.png")
# the position of the player
playerPos = [0, 0]

# a list of resources
resources = [DIRT, GRASS, WATER, COAL]

# use list comprehension to create our tilemap
tilemap = [[DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]

# initialise the pygame module
pygame.init()

# create a new drawing surface
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))

# font for inventory
INVFONT = pygame.font.Font('FreeSansBold.ttf', 18)

for rw in range(MAPHEIGHT):
    for cl in range(MAPWIDTH):
        randomNumber = random.randint(0, 15)
        if randomNumber == 0:
            tile = COAL
        elif randomNumber == 1 or randomNumber == 2:
            tile = WATER
        elif 3 <= randomNumber <= 7:
            tile = GRASS
        else:
            tile = DIRT
        tilemap[rw][cl] = tile

# loop forever
while True:
    # get all the user events
    for event in pygame.event.get():
        if event.type == QUIT:
            # end the game and close the window
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT and playerPos[0] < MAPWIDTH - 1:
                playerPos[0] += 1
            if event.key == K_LEFT and playerPos[0] > 0:
                playerPos[0] -= 1
            if event.key == K_UP and playerPos[1] > 0:
                playerPos[1] -= 1
            if event.key == K_DOWN and playerPos[1] < MAPHEIGHT -1:
                playerPos[1] += 1
            if event.key == K_SPACE:
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                inventory[currentTile] += 1
                tilemap[playerPos[1]][playerPos[0]] = DIRT

            if event.key == K_1:
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[DIRT] > 0:
                    inventory[DIRT] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = DIRT
                    inventory[currentTile] += 1

    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE))

    DISPLAYSURF.blit(PLAYER, (playerPos[0] * TILESIZE, playerPos[1] * TILESIZE))

    # display the inventory
    placePosition = 10
    for item in resources:
        DISPLAYSURF.blit(textures[item], (placePosition, MAPHEIGHT*TILESIZE+20))
        placePosition += 30
        textObj = INVFONT.render(str(inventory[item]), True, WHITE, BLACK)
        DISPLAYSURF.blit(textObj, (placePosition, MAPHEIGHT*TILESIZE+20))
        placePosition += 50

    # update the display
    pygame.display.update()
