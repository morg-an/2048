import pygame
import random

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

class Tile:
    def __init__(self, value, color) -> None:
        self.value = value
        self.color = color

def loadGrid():

#event loop
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