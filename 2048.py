import pygame
import random
pygame.init()

# Used pygame.get_init() to verify that pygame is initialized.
#print(pygame.get_init())

#create variable to control when game is running/quit
running = True

#set display variables
size = width, height = (500,500)
tiles_across = 4
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

def generateTileCoordinates(tiles_across, size):
    row = 0
    column = 0
    tiles = []
    while row < tiles_across:
        while column < tiles_across:
            tiles.append([
                [row, column],
                [int((width*.05)+(((width*.9)/tiles_across)*column)), int((height*.05)+(((height*.9)/tiles_across)*row))], 
                0, 
                tile_dict[0]])
            column += 1
        column = 0
        row+=1
    rand_tiles = random.sample(range(len(tiles)), 2)
    for tile in rand_tiles:
        tiles[tile][2] = 2
        tiles[tile][3] = tile_dict[2]
    print(tiles)
    return tiles
tiles = generateTileCoordinates(tiles_across, size)

#fuction generates the tile size to allow spacing between tiles
def generateTileSize(tiles_across, size):
    tile_size = (int((width*.8)/tiles_across), int((height*.8)/tiles_across))
    return tile_size
tile_size = generateTileSize(tiles_across, size)

def newRandTile(tiles_across):
    rand_tile = random.randint(0,len(tiles)-1)
    print(rand_tile)
    if tiles[rand_tile][2] != 0:
        # Need to fix this to be game over when there are no longer any available spaces for new tiles to fit.
        newRandTile(tiles_across)
    else:
        tiles[rand_tile][2] = 2
        tiles[rand_tile][3] = tile_dict[2]
    pygame.draw.rect(game_board, tiles[rand_tile][3], (tiles[rand_tile][1][0], tiles[rand_tile][1][1], tile_size[0], tile_size[1]))
    return rand_tile
            
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
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                print("Left")
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                print("Up")
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                print("Down")
                for index, tile in reversed(list(enumerate(tiles))):
                    print(index)
                    print("Evaluating tile:", tile)
                    #check if tile is on bottom row
                    if tile[0][0] != tiles_across-1:
                        #checks if tile value is not empty.
                        if tile[2] != 0:
                            comparison = tiles[index+tiles_across]
                                #checks if the tile under it is empty - if so, move tile.
                            if comparison[2] == 0:
                                print("Tile under is empty. Let's shift down.")
                                #reassign values
                                comparison[2] = tile[2]
                                tile[2] = 0
                                #reassign colors
                                comparison[3] = tile[3]
                                tile[3] = tile_dict[0] 

                                #check if the tile under it is the same value
                            elif tile[2] == comparison[2]:
                                print("Get ready to double!")
                                #reassign value & color to merged tile
                                comparison[2] = tile[2]*2
                                comparison[3] = tile_dict[tile[2]*2]
                                #reset now empty tile
                                tile[2] = 0
                                tile[3] = tile_dict[0]

                            #check if tile under it is larger
                            elif tile[2] < comparison[2]:
                                print("Tile under is larger. Do nothing.")

                            #check if tile under it is larger
                            elif tile[2] > comparison[2]:
                                print("Tile under is smaller. Do nothing.")

                            #checks if the tile under it is larger
                            else:
                                print("Whoops - I didn't think of that.")
                        
                        #redraw the tile
                            pygame.draw.rect(game_board, tile[3], (tile[1][0], tile[1][1], tile_size[0], tile_size[1]))
                            #redraw the comparison
                            pygame.draw.rect(game_board, comparison[3], (comparison[1][0], comparison[1][1], tile_size[0], tile_size[1]))
                            #display update
                            pygame.display.update

            #quit the game by pressing space
            elif event.key == pygame.K_SPACE:
                running = False
            #handle non-sensical keyboard input
            else:
                print("Use the direction arrows to control the game.")    
            
            #generate one new tile per keydown
            print("Generating new tile...")
            newRandTile(tiles_across)
            
            pygame.display.update()

#once running is not TRUE, quit game
pygame.quit();