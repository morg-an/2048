import random
import Constants

def newRandTile(tiles):
#random generate new tile for each turn
    rand_x = random.randint(0, Constants.tiles_across-1)
    rand_y = random.randint(0, Constants.tiles_across-1)
    #if the randomly generated tile is not zero, generate a new random tile
    while tiles[rand_x][rand_y].value != 0:
        rand_x = random.randint(0, Constants.tiles_across-1)
        rand_y = random.randint(0, Constants.tiles_across-1)
    #set the value & color of new randomly generated tile. 
    tiles[rand_x][rand_y].value = 2
    tiles[rand_x][rand_y].color = Constants.tile_colors[2]
    print("add value to random empty tile")
    return tiles[rand_x][rand_y]

def clear(fromTile):
    #use to reset value and color of tile
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
    print("Shifted from: Row ", fromTile.row, "Column ", fromTile.column)
    print("shifted to: Row", toTile.row, "Column ", toTile.column)

def merge(fromTile, toTile):
    #multiply value by 2 and increment color
    toTile.value = fromTile.value*2
    toTile.color = Constants.tile_colors[toTile.value]
    clear(fromTile)
    #mark that tile already changed to prevent the same tile from merging twice on same turn
    toTile.changed = True
    print("Merged from: Row ", fromTile.row, "Column ", fromTile.column)
    print("Merged to: Row", toTile.row, "Column ", toTile.column)

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