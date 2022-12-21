import Constants

def setTestScenario(tiles):
    value2 = [tiles[3][0], tiles[3][1], tiles[3][2]]
    value4 = []
    for tile in value2:
        tile.value = 2
        tile.color = Constants.tile_colors[2]
    for tile in value4:
        tile.value = 4
        tile.color = Constants.tile_colors[4]
    return tiles

