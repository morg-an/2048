import Constants
import Classes
import random
import math

def loadGrid(tiles):
    i = 0
    j = 0
    while i < Constants.tiles_across:
        tiles.append([])
        while j < Constants.tiles_across:
            tiles[i].append(Classes.Tile(0, Constants.tile_colors[0], i, j))
            j+=1
        j=0
        i+=1

def populateGrid(tiles):
    # randomly generate 2 tiles to start with value of 2
    rand_tiles = random.sample(range(Constants.tiles_across*Constants.tiles_across), 2)
    for tile in rand_tiles:
        # calculates what row the random tile is in by dividing the rand number by the grid width
        row = math.floor(tile/Constants.tiles_across)
        # calculates the column of the rand tile by finding the remainder after dividing by grid width
        column = tile%Constants.tiles_across
        # assign value of rand tiles to 2
        tiles[row][column].value = 2
        tiles[row][column].color = Constants.tile_colors[2]
    return tiles