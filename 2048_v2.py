import pygame
import random
import math

#create variable to control when game is running
running = True

#display variables
size = width, height = (500, 500)
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
    2048: (247,92,3)} 
tiles = []

def main():
    #initialize screen
    pygame.init()
    game_board = pygame.display.set_mode(size)
    pygame.display.set_caption('2048')

    #set background
    background = pygame.Surface(size)
    #converting the background speeds up rendering
    background = background.convert()
    background.fill(background_color)

    #display text
    #   Step 1: Set font
    font = pygame.font.Font(None, 36)
    #   Step 2: Set text content, aliased(?), and color
    text = font.render("Let's Play 2048!", True, tile_colors[2048])
    #   Step 3: set rectangle as container for text
    textpos = text.get_rect()
    #   Step 4: position the text
    textpos.center = background.get_rect().center
    #   Step 5: render the text to the background
    background.blit(text, textpos)
    #   Step 6: render the background to the game board
    game_board.blit(background, (0,0))

    #update the display
    pygame.display.update()
    loadGrid()

class Tile:
    def __init__(self, value, color) -> None:
        self.value = value
        self.color = color

    def toString(self):
        return("Value: ", str(self.value),"; Color: ", str(self.color))

def loadGrid():
    i = 0
    j = 0
    while i < tiles_across:
        tiles.append([])
        while j < tiles_across:
            tiles[i].append(Tile(0, tile_colors[0]))
            j+=1
        j=0
        i+=1
    # randomly generate 2 tiles to start with value of 2
    rand_tiles = random.sample(range(tiles_across*tiles_across), 2)
    print(rand_tiles)
    for tile in rand_tiles:
        row = math.floor(tile/tiles_across)
        column = tile%tiles_across
        print("Tile: ", tile, "Row: ", row, "Column: ", column)
        # assign value of rand tiles to 2
        tiles[row][column].value = 2
        tiles[row][column].color = tile_colors[2]
    return tiles

def printGrid():
    for row in tiles:
        print("New Row")
        for tile in row:
            print(tile.toString())

#event loop
main()
printGrid()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            #listen for key presses
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                print("Right")
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                print("Left")
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                print("Up")
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                print("Down")
            elif event.key == pygame.K_ESCAPE:
                print("You quit")
                running = False
            else:
                print("That is not a valid input.")
    

#quit game while out of event loop
pygame.quit()