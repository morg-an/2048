import Constants
import Classes

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
    #return tiles