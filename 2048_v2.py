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

    #display text - this is not working.
    font = pygame.font.Font(None, 36)
    text = font.render("Let's Play 2048!", 1, tile_colors[2048])
    textpos = text.get_rect()
    textpos.center = background.get_rect().center
    background.blit(text, textpos)

    game_board.blit(background, (0,0))
    pygame.display.update()

main()

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
            elif event.key== pygame.K_SPACE:
                print("You quit")
                running = False
            else:
                print("That is not a valid input.")
    

#quit game while out of event loop
pygame.quit()