def generateTileSize(width, height, tiles_across):
    tile_size = (int((width*.8)/tiles_across), int((height*.8)/tiles_across))
    return tile_size