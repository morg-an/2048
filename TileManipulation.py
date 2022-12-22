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

def mergeOrShift(tile, comp_tile, prior_comp_tile, adjacentComparison):
    validTurn = False
    #if the value of the comparison tile is the same, merge
    if comp_tile.value == tile.value:
        print("The tiles will merge because they have the same values (", tile.value, ")")
        merge(tile, comp_tile)
        validTurn = True
    #if the value of an adjacent comparison value is different, but non-zero, do nothinng.
    elif comp_tile.value != 0 and comp_tile.value != tile.value and adjacentComparison == True:
        print("The tiles won't merge or shift because the adjacent comparison tile has a different value.")
    #if the value of a non-adjacent comparisn value is different, but non-zero,
    #   shift to tile immediately to the right of the comparison tile (which should have a non-zero value).
    elif comp_tile.value != 0 and comp_tile.value != tile.value and adjacentComparison == False:
        comp_tile = prior_comp_tile
        print("The non-adjacent comp tile has a non-zero and non-matching value, so tile will shift to new comp_tile (column: ", comp_tile.column, ")")
        shift(tile, comp_tile)
        validTurn = True
    #if comparison value is empty, shift to the comparison tile
    elif comp_tile.value == 0:
        print("Tile will shift to the empty comp tile.")
        shift(tile, comp_tile)
        validTurn = True
    else:
        print("Something went wrong.")      
    return validTurn

def left(tiles):
    validTurn = False
    i = 1
    #iterate through all tiles, left to right
    for row in tiles:
        for tile in row:
            print("Checking Row: ", tile.row, " Column: ", tile.column)
            #identify if the tile has a value other than 0
            if tile.value != 0:
                print("This tile has a value of ", tile.value)
                #check if there is a tile to the left, and if so set it as the comparison tile
                if tile.column-1 >= 0:
                    adjacentComparison = True
                    comp_tile = tiles[tile.row][tile.column-1]
                    prior_comp_tile = ""
                    print("This tile is not in the first column, so the comparison tile is in Column ", comp_tile.column, " and has a value of ", comp_tile.value)
                    #if the value of the comparison tile is zero
                    if comp_tile.value == 0:
                        print("The comparison tile is empty. Continue looking for new comparison.")
                        i = 2
                        #contine looping for as long as the comparison tile remains a value of zero and is not in the first column
                        while comp_tile.value == 0 and comp_tile.column > 0:
                            adjacentComparison = False
                            prior_comp_tile = comp_tile
                            comp_tile = tiles[tile.row][tile.column-i]
                            print("Comparison Tile changed to Row: ", comp_tile.row, "Column: ", comp_tile.column)
                            i += 1
                        print("Final Comparison Tile at Row: ", comp_tile.row, " Column: ", comp_tile.column)
                    if mergeOrShift(tile, comp_tile, prior_comp_tile, adjacentComparison):
                        validTurn = True
                else:
                    continue
    return validTurn

def right(tiles):
    validTurn = False
    i = 1
    #iterate through all tiles, right to left (reversed columns)
    for row in tiles: 
        for tile in reversed(row):
            print("Checking Row: ", tile.row, " Column: ", tile.column)
            #identify if the tile has a value other than 0
            if tile.value != 0:
                print("This tile has a value of ", tile.value)
                #check if there is a tile to the right, and if so set it as the comparison tile
                if tile.column+1 < Constants.tiles_across:
                    adjacentComparison = True
                    comp_tile = tiles[tile.row][tile.column+1]
                    prior_comp_tile = ""
                    print("This tile is not in the last column, so the comparison tile is in Column ", comp_tile.column, " and has a value of ", comp_tile.value)
                    #if the value of the comparison tile is zero
                    if comp_tile.value == 0:
                        print("The comparison tile is empty. Continue looking for new comparison.")
                        i = 2
                        #contine looping for as long as the comparison tile remains a value of zero and is not in the first column
                        while comp_tile.value == 0 and comp_tile.column < Constants.tiles_across-1:
                            adjacentComparison = False
                            prior_comp_tile = comp_tile
                            comp_tile = tiles[tile.row][tile.column+i]
                            print("Comparison Tile changed to Row: ", comp_tile.row, "Column: ", comp_tile.column)
                            i += 1
                        print("Final Comparison Tile at Row: ", comp_tile.row, " Column: ", comp_tile.column)
                    if mergeOrShift(tile, comp_tile, prior_comp_tile, adjacentComparison):
                        validTurn = True
                else:
                    continue
    return validTurn

def up(tiles):
    validTurn = False
    i = 1
    #iterate through all tiles, top to bottom
    for row in tiles:
        for tile in row:
            print("Checking Row: ", tile.row, " Column: ", tile.column)
            #identify if the tile has a value other than 0
            if tile.value != 0:
                print("This tile has a value of ", tile.value)
                #check if there is a tile above, and if so set it as the comparison tile
                if tile.row-1 >= 0:
                    adjacentComparison = True
                    comp_tile = tiles[tile.row-1][tile.column]
                    prior_comp_tile = ""
                    print("This tile is not in the first row, so the comparison tile is in Row ", comp_tile.row, " and has a value of ", comp_tile.value)
                    #if the value of the comparison tile is zero
                    if comp_tile.value == 0:
                        print("The comparison tile is empty. Continue looking for new comparison.")
                        i = 2
                        #contine looping for as long as the comparison tile remains a value of zero and is not in the first row
                        while comp_tile.value == 0 and comp_tile.row > 0:
                            adjacentComparison = False
                            prior_comp_tile = comp_tile
                            comp_tile = tiles[tile.row-i][tile.column]
                            print("Comparison Tile changed to Row: ", comp_tile.row, "Column: ", comp_tile.column)
                            i += 1
                        print("Final Comparison Tile at Row: ", comp_tile.row, " Column: ", comp_tile.column)
                    if mergeOrShift(tile, comp_tile, prior_comp_tile, adjacentComparison):
                        validTurn = True
                else:
                    continue
    return validTurn

def down(tiles):
    validTurn = False
    i = 1
    #iterate through all tiles, bottom to top (reversed rows)
    for row in reversed(tiles):
        for tile in row:
            print("Checking Row: ", tile.row, " Column: ", tile.column)
            #identify if the tile has a value other than 0
            if tile.value != 0:
                print("This tile has a value of ", tile.value)
                #check if there is a tile below, and if so set it as the comparison tile
                if tile.row+1 < Constants.tiles_across:
                    adjacentComparison = True
                    comp_tile = tiles[tile.row+1][tile.column]
                    prior_comp_tile = ""
                    print("This tile is not in the first row, so the comparison tile is in Row ", comp_tile.row, " and has a value of ", comp_tile.value)
                    #if the value of the comparison tile is zero
                    if comp_tile.value == 0:
                        print("The comparison tile is empty. Continue looking for new comparison.")
                        i = 2
                        #contine looping for as long as the comparison tile remains a value of zero and is not in the first row
                        while comp_tile.value == 0 and comp_tile.row < Constants.tiles_across-1:
                            adjacentComparison = False
                            prior_comp_tile = comp_tile
                            comp_tile = tiles[tile.row+i][tile.column]
                            print("Comparison Tile changed to Row: ", comp_tile.row, "Column: ", comp_tile.column)
                            i += 1
                        print("Final Comparison Tile at Row: ", comp_tile.row, " Column: ", comp_tile.column)
                    if mergeOrShift(tile, comp_tile, prior_comp_tile, adjacentComparison):
                        validTurn = True
                else:
                    continue
    return validTurn