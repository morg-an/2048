import pygame
import random
import Constants
import Setup
import Testing

running = True
game_board = pygame.display.set_mode(Constants.size)
tiles = []

def main():
    #initialize screen
    pygame.init()
    pygame.display.set_caption('2048')

    #set background
    background = pygame.Surface(Constants.size)
    #converting the background speeds up rendering
    background = background.convert()
    background.fill(Constants.background_color)
    game_board.blit(background, (0,0))

    #update the display
    pygame.display.update()

    #generate the tile objects for the game board
    Setup.loadGrid(tiles)

    # To toggle between random and testing setups, comment out one of the following two lines:
    Setup.populateGrid(tiles)
    #Testing.setTestScenario(tiles)

    #draw tiles to the game board
    draw(game_board)

def draw(game_board):
    font = pygame.font.Font(None, 36)
    for row in tiles:
        for tile in row:
            pygame.draw.rect(game_board, tile.color, (tile.coordinate[0], tile.coordinate[1], Constants.tile_size[0], Constants.tile_size[1]))
            text_surface = font.render(str(tile.value), False, (255, 255, 255))
            textpos = text_surface.get_rect()
            textpos.center = text_surface.get_rect().center
            text_surface.blit(text_surface, textpos)
            game_board.blit(text_surface, (tile.coordinate))
    pygame.display.update()

def clear(fromTile):
    #use to reset value and color of tile
    fromTile.value = 0
    fromTile.color = Constants.tile_colors[0]

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
            if tile.value == 0 and tile.column != Constants.tiles_across-1 and tiles[tile.row][tile.column+1].value != 0:
                comp_tile = tiles[tile.row][tile.column+1]
                shift(comp_tile, tile)

def right():
    validTurn = False
    for row in tiles: 
        for tile in reversed(row):
            if tile.column != Constants.tiles_across-1 and tile.value !=0:
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
            if tile.value == 0 and tile.row != Constants.tiles_across-1 and tiles[tile.row+1][tile.column].value != 0:
                comp_tile = tiles[tile.row+1][tile.column]
                shift(comp_tile, tile)

def down():
    validTurn = False
    for row in reversed(tiles):
        for tile in row:
            if tile.row != Constants.tiles_across-1 and tile.value != 0:
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