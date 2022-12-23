import Constants

def setTestScenario(tiles):
    value2 = [tiles[1][2]]
    value4 = [tiles[1][3]]
    for tile in value2:
        tile.value = 2
        tile.color = Constants.tile_colors[2]
    for tile in value4:
        tile.value = 4
        tile.color = Constants.tile_colors[4]
    return tiles

