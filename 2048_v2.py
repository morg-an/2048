# STILL TO Fix:
# Remove empty tiles at end of the turn does not work correctly when there are 2 or more '0' value tiles in a row. 
# For example a row of [16, 0, 0, 4] will become [0, 16, 0, 4] after removeRight()

# colors for 512 and 32 are too similar

import pygame
import random
import math

#create variable to control when game is running
running = True

#display variables
size = width, height = (500, 500)
game_board = pygame.display.set_mode(size)
tiles_across = 3
background_color = (245, 223, 187)
tile_colors = {
    0:(231, 213, 181), 
    2:(148,93,94), 
    4:(113,103,124), 
    8:(39,60,44), 
    16:(14,149,148), 
    32:(177,116,15), 
    64:(239,118,122), 
    128:(9,12,155), 
    256:(94,11,21), 
    512:(190,124,77),
    1024: (196,32,33), 
    2048: (247,92,3),
    4096: (15, 240, 8)} 
tiles = []

def generateTileSize(tiles_across):
    tile_size = (int((width*.8)/tiles_across), int((height*.8)/tiles_across))
    return tile_size

tile_size = generateTileSize(tiles_across)

def main():
    #initialize screen
    pygame.init()
    pygame.display.set_caption('2048')

    #set background
    background = pygame.Surface(size)
    #converting the background speeds up rendering
    background = background.convert()
    background.fill(background_color)

    #display text
    #   Step 1: Set font
    # font = pygame.font.Font(None, 36)
    #   Step 2: Set text content, aliased(?), and color
    #text = font.render("Let's Play 2048!", True, tile_colors[2048])
    #   Step 3: set rectangle as container for text
    #textpos = text.get_rect()
    #   Step 4: position the text
    #textpos.center = background.get_rect().center
    #   Step 5: render the text to the background
    #background.blit(text, textpos)
    #   Step 6: render the background to the game board
    game_board.blit(background, (0,0))

    #update the display
    pygame.display.update()
    loadGrid()
    #populateGrid()
    setTestScenario()

    #draw tiles
    draw(game_board)

class Tile:
    def __init__(self, value, color, row, column) -> None:
        self.value = value
        self.color = color
        self.row = row
        self.column = column
        self.coordinate = [int((width*.05)+(((width*.9)/tiles_across)*column)), int((height*.05)+(((height*.9)/tiles_across)*row))]
        #tile.changed is used to prevent the same file from merging twice on the same turn.
        self.changed = False

    def toString(self):
        return("Value: ", str(self.value),
        "; Color: ", str(self.color), 
        "; Row: ", str(self.row), 
        "; Column: ", str(self.column), 
        "; Coordinate: ", str(self.coordinate))

def draw(game_board):
    font = pygame.font.Font(None, 36)
    for row in tiles:
        for tile in row:
            pygame.draw.rect(game_board, tile.color, (tile.coordinate[0], tile.coordinate[1], tile_size[0], tile_size[1]))
            text_surface = font.render(str(tile.value), False, (255, 255, 255))
            textpos = text_surface.get_rect()
            textpos.center = text_surface.get_rect().center
            text_surface.blit(text_surface, textpos)
            game_board.blit(text_surface, (tile.coordinate))
    pygame.display.update()

def clear(fromTile):
    #use to reset value and color of tile
    fromTile.value = 0
    fromTile.color = tile_colors[0]

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
    toTile.color = tile_colors[toTile.value]
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

# def redraw():
#     #redraw the tile
#     pygame.draw.rect(game_board, tile[3], (tile[1][0], tile[1][1], tile_size[0], tile_size[1]))
#     #redraw the comparison
#     pygame.draw.rect(game_board, comparison[3], (comparison[1][0], comparison[1][1], tile_size[0], tile_size[1]))
#     #display update
#     pygame.display.update

def loadGrid():
    i = 0
    j = 0
    while i < tiles_across:
        tiles.append([])
        while j < tiles_across:
            tiles[i].append(Tile(0, tile_colors[0], i, j))
            j+=1
        j=0
        i+=1
    #return tiles

def populateGrid():
    # randomly generate 2 tiles to start with value of 2
    rand_tiles = random.sample(range(tiles_across*tiles_across), 2)
    for tile in rand_tiles:
        # calculates what row the random tile is in by dividing the rand number by the grid width
        row = math.floor(tile/tiles_across)
        # calculates the column of the rand tile by finding the remainder after dividing by grid width
        column = tile%tiles_across
        # assign value of rand tiles to 2
        tiles[row][column].value = 2
        tiles[row][column].color = tile_colors[2]
    return tiles

def setTestScenario():
    value2 = [tiles[3][0], tiles[3][1], tiles[3][2]]
    value4 = []
    for tile in value2:
        tile.value = 2
        tile.color = tile_colors[2]
    for tile in value4:
        tile.value = 4
        tile.color = tile_colors[4]
    return tiles

def isEndgame():
# identify if all tiles contain value >= 2
    endgame = True
    for row in tiles:
        for tile in row:
            if tile.value == 0:
                endgame = False
    return endgame

def newTile():
#random generate new tile for each turn
    rand_x = random.randint(0, tiles_across-1)
    rand_y = random.randint(0, tiles_across-1)
    #if the randomly generated tile is not zero, generate a new random tile
    while tiles[rand_x][rand_y].value != 0:
        rand_x = random.randint(0, tiles_across-1)
        rand_y = random.randint(0, tiles_across-1)
    #set the value & color of new randomly generated tile. 
    tiles[rand_x][rand_y].value = 2
    tiles[rand_x][rand_y].color = tile_colors[2]
    print("add value to random empty tile")
    return tiles[rand_x][rand_y]


def printGrid():
    for row in tiles:
        print("New Row")
        for tile in row:
            print(tile.toString())

def reset():
    for row in tiles:
        for tile in row:
            tile.changed = False

def left():
    validTurn = False
    for row in tiles:
        for tile in row:
            if tile.column != 0 and tile.value != 0:
                comp_tile = tiles[tile.row][tile.column-1]
                if mergeOrShift(tile, comp_tile) == True:
                    validTurn = True
    removeLeft()
    return validTurn

def removeLeft():
    for row in tiles:
        for tile in row:
            #check for zero value tiles that are not in the last column and where the tile to the right is non-zero
            if tile.value == 0 and tile.column != tiles_across-1 and tiles[tile.row][tile.column+1].value != 0:
                comp_tile = tiles[tile.row][tile.column+1]
                shift(comp_tile, tile)

def right():
    validTurn = False
    for row in tiles: 
        for tile in reversed(row):
            if tile.column != tiles_across-1 and tile.value !=0:
                comp_tile = tiles[tile.row][tile.column+1]
                if mergeOrShift(tile, comp_tile) == True:
                    validTurn = True
    removeRight()
    return validTurn

def removeRight():
    for row in tiles:
        for tile in row:
            #check for zero value tiles that are not in the first column and where the tile to the left is non-zero
            if tile.value == 0 and tile.column != 0 and tiles[tile.row][tile.column-1].value != 0:
                comp_tile = tiles[tile.row][tile.column-1]
                shift(comp_tile, tile)

def up():
    validTurn = False
    for row in reversed(tiles):
        for tile in row:
            if tile.row != 0 and tile.value != 0:
                comp_tile = tiles[tile.row-1][tile.column]
                if mergeOrShift(tile, comp_tile) == True:
                    validTurn = True
    removeUp()
    return validTurn

def removeUp():
    for row in tiles:
        for tile in row:
            #check for zero value tiles that are not in the last row and where the tile below is non-zero
            if tile.value == 0 and tile.row != tiles_across-1 and tiles[tile.row+1][tile.column].value != 0:
                comp_tile = tiles[tile.row+1][tile.column]
                shift(comp_tile, tile)

def down():
    validTurn = False
    for row in reversed(tiles):
        for tile in row:
            if tile.row != tiles_across-1 and tile.value != 0:
                comp_tile = tiles[tile.row+1][tile.column]
                if mergeOrShift(tile, comp_tile) == True:
                    validTurn = True
    removeDown()
    return validTurn

def removeDown():
    for row in tiles:
        for tile in row:
            #check for zero value tiles that are not in the first row and where the tile above is non-zero
            if tile.value == 0 and tile.row != 0 and tiles[tile.row-1][tile.column].value != 0:
                comp_tile = tiles[tile.row-1][tile.column]
                shift(comp_tile, tile)
#event loop
main()

while running:
    for event in pygame.event.get():
        validTurn = False
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            #listen for key presses
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                print("Right")
                validTurn = right()
                print("Valid Turn?", validTurn)
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                print("Left")
                validTurn = left()
                print("Valid Turn?", validTurn)
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                print("Up")
                validTurn = up()
                print("Valid Turn?", validTurn)
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                print("Down")
                validTurn = down()
                print("Valid Turn?", validTurn)
            elif event.key == pygame.K_ESCAPE:
                print("You quit")
                running = False
            else:
                print("That is not a valid input.")
            reset()
            if isEndgame() == False:
                if validTurn == True:
                    #only generate new tile if last turn merged or shifted an existing tile.
                    newTile()
                draw(game_board)
            else:
                running = False
                print("Game Over")
                pygame.quit()

#quit game while out of event loop
pygame.quit()


