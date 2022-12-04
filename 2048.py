import pygame
import random
pygame.init()

#create variable to control when game is running/quit
running = True

#set display variables
size = width, height = (500,500)
font = pygame.font.Font(None, 32)
tiles_across = 3
background_color = (245,223,187)
tile_dict = {
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
    2048: (247,92,3)} 

# create array containing the x/y position, coordinates, value, and color of each tile and assigns two random tiles as the starting tiles.
def generateTiles(tiles_across, size):
    row = 0
    column = 0
    tiles = []
    while row < tiles_across:
        while column < tiles_across:
            tiles.append([
                [row, column], #x/y position
                [int((width*.05)+(((width*.9)/tiles_across)*column)), int((height*.05)+(((height*.9)/tiles_across)*row))], #starting coordinates
                0, #value
                tile_dict[0]]) #color
            column += 1
        column = 0
        row+=1
    rand_tiles = random.sample(range(len(tiles)), 2)
    for tile in rand_tiles:
        tiles[tile][2] = 2
        tiles[tile][3] = tile_dict[2]
    return tiles

def generateTileSize(tiles_across, size):
    tile_size = (int((width*.8)/tiles_across), int((height*.8)/tiles_across))
    return tile_size

#generate the starting gameboard.
tiles = generateTiles(tiles_across, size)
tile_size = generateTileSize(tiles_across, size)
text = font.render("Hello World", True, (247,92,3))

def isEndgame(tiles):
    endGame = True
    for tile in tiles:
        if tile[2] == 0:
            endGame = False
    return endGame

#This code is commented out because I re-wrote the function below without using recursion. It works the same way.
# def newRandTile(tiles_across):
#     rand_tile = random.randint(0,len(tiles)-1)
#     if tiles[rand_tile][2] != 0:
#         newRandTile(tiles_across)
#     else:
#         #set the value
#         tiles[rand_tile][2] = 2
#         #set the color
#         tiles[rand_tile][3] = tile_dict[2]
#     pygame.draw.rect(game_board, tiles[rand_tile][3], (tiles[rand_tile][1][0], tiles[rand_tile][1][1], tile_size[0], tile_size[1]))
#     return rand_tile

#re-write the 'newRandTile' function without recursion
def newRandTile2(tiles_across):
    rand_tile = random.randint(0, len(tiles)-1)
    while tiles[rand_tile][2] != 0:
        rand_tile = random.randint(0, len(tiles)-1)
    #set the value
    tiles[rand_tile][2] = 2
    #set the color
    tiles[rand_tile][3] = tile_dict[2]
    pygame.draw.rect(game_board, tiles[rand_tile][3], (tiles[rand_tile][1][0], tiles[rand_tile][1][1], tile_size[0], tile_size[1]))
    return rand_tile

def redraw():
    #redraw the tile
    pygame.draw.rect(game_board, tile[3], (tile[1][0], tile[1][1], tile_size[0], tile_size[1]))
    #redraw the comparison
    pygame.draw.rect(game_board, comparison[3], (comparison[1][0], comparison[1][1], tile_size[0], tile_size[1]))
    #display update
    pygame.display.update

def shift():
    #reassign values
    comparison[2] = tile[2]
    tile[2] = 0
    #reassign colors
    comparison[3] = tile[3]
    tile[3] = tile_dict[0]

def merge():
    #reassign value & color to merged tile
    comparison[2] = tile[2]*2
    comparison[3] = tile_dict[tile[2]*2]
    #reset now empty tile
    tile[2] = 0
    tile[3] = tile_dict[0]

# create game surface(window size; background color; game title)
game_board = pygame.display.set_mode(size)
game_board.fill(background_color)
pygame.display.set_caption('2048')

#draw tiles
for tile in tiles:
    pygame.draw.rect(game_board, tile[3], (tile[1][0], tile[1][1], tile_size[0], tile_size[1]))

#apply above changes to display
pygame.display.update()

#use while loop with running variable to keep game running until user quits
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Checks for when a key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                print("Right")
                for index, tile in reversed(list(enumerate(tiles))):
                    #check if tile is not on the right
                    if tile[0][1] != tiles_across-1:
                        #check if value is not empty
                        if tile[2] != 0:
                            #find comparison
                            comparison = tiles[index+1]
                            if comparison[2] == 0:
                                shift()
                            elif tile[2] == comparison[2]:
                                merge()
                            redraw()

            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                print("Left")
                for index, tile in enumerate(tiles):
                    #check if tile is not on the left
                    if tile[0][1] != 0:
                        #check if value is not empty
                        if tile[2] != 0:
                            #find comparison
                            comparison = tiles[index-1]
                            if comparison[2] == 0:
                                shift()
                            elif tile[2] == comparison[2]:
                                merge()
                            redraw()

            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                print("Up")
                for index, tile in enumerate(tiles):
                    #check if tile is not on top row
                    if tile[0][0] != 0:
                        #check if tile value is not empty
                        if tile[2] != 0:
                            comparison = tiles[index-tiles_across]
                            if comparison[2] == 0:
                                shift()
                            elif tile[2] == comparison[2]:
                                merge()
                            redraw()

            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                print("Down")
                for index, tile in reversed(list(enumerate(tiles))):
                    #check if tile is not on bottom row
                    if tile[0][0] != tiles_across-1:
                        #checks if tile value is not empty.
                        if tile[2] != 0:
                            comparison = tiles[index+tiles_across]
                            if comparison[2] == 0:
                                shift()
                            elif comparison[2] == tile[2]:
                                merge()
                            redraw()

            #quit the game by pressing space
            elif event.key == pygame.K_SPACE:
                running = False
            #handle non-sensical keyboard input
            else:
                print("Use the direction arrows to control the game.")    
            
            pygame.display.update()

            #check if game over to determine whether to quit or generate new tile
            if isEndgame(tiles) == False:
                #generate one new tile per keydown
                newRandTile2(tiles_across)
            else:
                print("Game Over.")
                running = False
            


#once running is not TRUE, quit game
pygame.quit();