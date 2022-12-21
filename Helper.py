def generateTileSize(width, height, tiles_across):
    tile_size = (int((width*.8)/tiles_across), int((height*.8)/tiles_across))
    return tile_size

def printGrid(tiles):
    for row in tiles:
        print("New Row")
        for tile in row:
            print(tile.toString())