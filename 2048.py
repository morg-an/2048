import pygame
pygame.init()

# Used pygame.get_init() to verify that pygame is initialized.
#print(pygame.get_init())

#create variable to control when game is running/quit
running = True

#set display variables
size = width, height = (500,500)
tiles_across = 4
background_color = (245,223,187)
empty_tile_color = (231, 213, 181)
tile_color = [
    (148,93,94), 
    (113,103,124), 
    (39,60,44),
    (14,149,148), 
    (177,116,15), 
    (239,118,122), 
    (9,12,155), 
    (94,11,21), 
    (190,124,77), 
    (196,32,33), 
    (247,92,3)
    ]


#function generates the top right corner for each tile on gameboard
def generateTileCoordinates(tiles_across, size):
    row = 0
    column = 0
    tile_coordinates = []
    while row < tiles_across:
        while column < tiles_across:
            tile_coordinates.append([
                int((width*.05)+(((width*.9)/tiles_across)*column)),
                int((height*.05)+(((height*.9)/tiles_across)*row))])
            column += 1
        column = 0
        row+=1
    return tile_coordinates
tile_coordinates = generateTileCoordinates(tiles_across, size)

#fuction generates the tile size to allow spacing between tiles
def generateTileSize(tiles_across, size):
    tile_size = (int((width*.8)/tiles_across), int((height*.8)/tiles_across))
    return tile_size
tile_size = generateTileSize(tiles_across, size)

#create game surface(window size; background color; game title)
game_board = pygame.display.set_mode(size)
game_board.fill(background_color)
pygame.display.set_caption('2048')

#draw tiles
for tile in tile_coordinates:
    pygame.draw.rect(game_board, empty_tile_color,(tile[0], tile[1], tile_size[0], tile_size[1]))

#apply above changes to display
pygame.display.update()

#use while loop with running variable to keep game running until user quits
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#once running is not TRUE, quit game
pygame.quit()