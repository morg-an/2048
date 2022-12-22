import pygame
import Constants
import Setup
import Testing
import TileManipulation

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
    #Setup.populateGrid(tiles)
    Testing.setTestScenario(tiles)

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

def isEndgame():
# identify if all tiles contain value >= 2
    endgame = True
    for row in tiles:
        for tile in row:
            if tile.value == 0:
                endgame = False
    return endgame

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
                validTurn = TileManipulation.right(tiles)
                print("Valid Turn?", validTurn)
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                print("Left")
                validTurn = TileManipulation.left(tiles)
                print("Valid Turn?", validTurn)
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                print("Up")
                validTurn = TileManipulation.up(tiles)
                print("Valid Turn?", validTurn)
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                print("Down")
                validTurn = TileManipulation.down(tiles)
                print("Valid Turn?", validTurn)
            elif event.key == pygame.K_ESCAPE:
                print("You quit")
                running = False
            else:
                print("That is not a valid input.")
            TileManipulation.reset(tiles)
            if isEndgame() == False:
                if validTurn == True:
                    #only generate new tile if last turn merged or shifted an existing tile.
                    TileManipulation.newRandTile(tiles)
                draw(game_board)
            else:
                running = False
                print("Game Over")
                pygame.quit()

#quit game while out of event loop
pygame.quit()