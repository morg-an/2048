import Constants

class Tile:
    def __init__(self, value, color, row, column) -> None:
        self.value = value
        self.color = color
        self.row = row
        self.column = column
        self.coordinate = [int((Constants.width*.05)+(((Constants.width*.9)/Constants.tiles_across)*column)), 
        int((Constants.height*.05)+(((Constants.height*.9)/Constants.tiles_across)*row))]
        #tile.changed is used to prevent the same file from merging twice on the same turn.
        self.changed = False

    def toString(self):
        return("Value: ", str(self.value),
        "; Color: ", str(self.color), 
        "; Row: ", str(self.row), 
        "; Column: ", str(self.column), 
        "; Coordinate: ", str(self.coordinate))