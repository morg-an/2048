import Helper 

size = width, height = (500, 500)
tiles_across = 4
tile_size = Helper.generateTileSize(width, height, tiles_across)
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