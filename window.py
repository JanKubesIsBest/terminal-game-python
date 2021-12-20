from map import map
from fill_char_array import char_array 

class window(map):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.map = char_array(self, ".")
    def add_text(self, text, text_positionX, text_positionY):
        #for x in range(len(text)):
        self.map[2][0] = text
        print(self.map)