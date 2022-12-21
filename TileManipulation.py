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
    #printGrid()
    #set boolian to show that merge happened on keypress - used to verify before new rand tile generates.
    return True

def merge(fromTile, toTile):
    #multiply value by 2 and increment color
    toTile.value = fromTile.value*2
    toTile.color = Constants.tile_colors[toTile.value]
    clear(fromTile)
    #mark that tile already changed to prevent the same tile from merging twice on same turn
    toTile.changed = True
    print("Merged from: Row ", fromTile.row, "Column ", fromTile.column)
    print("Merged to: Row", toTile.row, "Column ", toTile.column)
    #printGrid()
    #set boolian to show that merge happened on keypress - used to verify before new rand tile generates.
    return True

def mergeOrShift(tile, comp_tile):
    if comp_tile.value == tile.value and tile.changed == False:
        return(merge(tile, comp_tile))
    elif comp_tile.value == 0:
        return(shift(tile, comp_tile))
    else:
        return False

def left(tiles):
    validTurn = False
    for row in tiles:
        for tile in row:
            if tile.column != 0 and tile.value != 0:
                comp_tile = tiles[tile.row][tile.column-1]
                if mergeOrShift(tile, comp_tile) == True:
                    validTurn = True
    removeLeft(tiles)
    return validTurn

def removeLeft(tiles):
    for row in tiles:
        for tile in row:
            #check for zero value tiles that are not in the last column and where the tile to the right is non-zero
            if tile.value == 0 and tile.column != Constants.tiles_across-1 and tiles[tile.row][tile.column+1].value != 0:
                comp_tile = tiles[tile.row][tile.column+1]
                shift(comp_tile, tile)

def right(tiles):
    validTurn = False
    for row in tiles: 
        for tile in reversed(row):
            if tile.column != Constants.tiles_across-1 and tile.value !=0:
                comp_tile = tiles[tile.row][tile.column+1]
                if mergeOrShift(tile, comp_tile) == True:
                    validTurn = True
    removeRight(tiles)
    return validTurn

def removeRight(tiles):
    for row in tiles:
        for tile in row:
            #check for zero value tiles that are not in the first column and where the tile to the left is non-zero
            if tile.value == 0 and tile.column != 0 and tiles[tile.row][tile.column-1].value != 0:
                comp_tile = tiles[tile.row][tile.column-1]
                shift(comp_tile, tile)

def up(tiles):
    validTurn = False
    for row in reversed(tiles):
        for tile in row:
            if tile.row != 0 and tile.value != 0:
                comp_tile = tiles[tile.row-1][tile.column]
                if mergeOrShift(tile, comp_tile) == True:
                    validTurn = True
    removeUp(tiles)
    return validTurn

def removeUp(tiles):
    for row in tiles:
        for tile in row:
            #check for zero value tiles that are not in the last row and where the tile below is non-zero
            if tile.value == 0 and tile.row != Constants.tiles_across-1 and tiles[tile.row+1][tile.column].value != 0:
                comp_tile = tiles[tile.row+1][tile.column]
                shift(comp_tile, tile)

def down(tiles):
    validTurn = False
    for row in reversed(tiles):
        for tile in row:
            if tile.row != Constants.tiles_across-1 and tile.value != 0:
                comp_tile = tiles[tile.row+1][tile.column]
                if mergeOrShift(tile, comp_tile) == True:
                    validTurn = True
    removeDown(tiles)
    return validTurn

def removeDown(tiles):
    for row in tiles:
        for tile in row:
            #check for zero value tiles that are not in the first row and where the tile above is non-zero
            if tile.value == 0 and tile.row != 0 and tiles[tile.row-1][tile.column].value != 0:
                comp_tile = tiles[tile.row-1][tile.column]
                shift(comp_tile, tile)