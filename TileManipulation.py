import random
import Constants

def newRandTile(tiles):
    rand_x = random.randint(0, Constants.tiles_across-1)
    rand_y = random.randint(0, Constants.tiles_across-1)
    while tiles[rand_x][rand_y].value != 0:
        rand_x = random.randint(0, Constants.tiles_across-1)
        rand_y = random.randint(0, Constants.tiles_across-1)
    tiles[rand_x][rand_y].value = 2
    tiles[rand_x][rand_y].color = Constants.tile_colors[2]
    return tiles[rand_x][rand_y]

def clear(fromTile):
    fromTile.value = 0
    fromTile.color = Constants.tile_colors[0]

def reset(tiles):
    for row in tiles:
        for tile in row:
            tile.changed = False

def shift(fromTile, toTile):
    toTile.value = fromTile.value
    toTile.color = fromTile.color
    clear(fromTile)

def merge(fromTile, toTile):
    toTile.value = fromTile.value*2
    toTile.color = Constants.tile_colors[toTile.value]
    clear(fromTile)
    toTile.changed = True

def mergeOrShift(tile, comp_tile, prior_comp_tile, adjacentComparison):
    validTurn = False
    if comp_tile.value == tile.value:
        merge(tile, comp_tile)
        validTurn = True
    elif comp_tile.value != 0 and comp_tile.value != tile.value and adjacentComparison == False:
        comp_tile = prior_comp_tile
        shift(tile, comp_tile)
        validTurn = True
    elif comp_tile.value == 0:
        shift(tile, comp_tile)
        validTurn = True
    return validTurn

def left(tiles):
    validTurn = False
    i = 1
    #iterate through all tiles, left to right
    for row in tiles:
        for tile in row:
            if tile.value == 0:
                continue
            if tile.column-1 < 0:
                continue
            adjacentComparison = True
            comp_tile = tiles[tile.row][tile.column-1]
            prior_comp_tile = ""
            if comp_tile.value == 0:
                i = 2
                while comp_tile.value == 0 and comp_tile.column > 0:
                    adjacentComparison = False
                    prior_comp_tile = comp_tile
                    comp_tile = tiles[tile.row][tile.column-i]
                    i += 1
            if mergeOrShift(tile, comp_tile, prior_comp_tile, adjacentComparison):
                validTurn = True
    return validTurn

def right(tiles):
    validTurn = False
    i = 1
    for row in tiles: 
        for tile in reversed(row):
            if tile.value == 0:
                continue
            if tile.column+1 >= Constants.tiles_across:
                continue
            adjacentComparison = True
            comp_tile = tiles[tile.row][tile.column+1]
            prior_comp_tile = ""
            if comp_tile.value == 0:
                i = 2
                while comp_tile.value == 0 and comp_tile.column < Constants.tiles_across-1:
                    adjacentComparison = False
                    prior_comp_tile = comp_tile
                    comp_tile = tiles[tile.row][tile.column+i]
                    i += 1
            if mergeOrShift(tile, comp_tile, prior_comp_tile, adjacentComparison):
                validTurn = True
    return validTurn

def up(tiles):
    validTurn = False
    i = 1
    for row in tiles:
        for tile in row:
            if tile.value == 0:
                continue
            if tile.row-1 <0:
                continue
            adjacentComparison = True
            comp_tile = tiles[tile.row-1][tile.column]
            prior_comp_tile = ""
            if comp_tile.value == 0:
                i = 2
                while comp_tile.value == 0 and comp_tile.row > 0:
                    adjacentComparison = False
                    prior_comp_tile = comp_tile
                    comp_tile = tiles[tile.row-i][tile.column]
                    i += 1
            if mergeOrShift(tile, comp_tile, prior_comp_tile, adjacentComparison):
                validTurn = True
    return validTurn

def down(tiles):
    validTurn = False
    i = 1
    for row in reversed(tiles):
        for tile in row:
            if tile.value == 0:
                continue
            if tile.row+1 >= Constants.tiles_across:
                continue
            adjacentComparison = True
            comp_tile = tiles[tile.row+1][tile.column]
            prior_comp_tile = ""
            if comp_tile.value == 0:
                i = 2
                while comp_tile.value == 0 and comp_tile.row < Constants.tiles_across-1:
                    adjacentComparison = False
                    prior_comp_tile = comp_tile
                    comp_tile = tiles[tile.row+i][tile.column]
                    i += 1
            if mergeOrShift(tile, comp_tile, prior_comp_tile, adjacentComparison):
                validTurn = True
    return validTurn