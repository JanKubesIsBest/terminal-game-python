import numpy as np
from fill_char_array import char_array

class camera:
    def __init__(self, map, height, width, posX, posY, multiplayerResolutionX, multiplayerResolutionY):
        self.map = map
        self.height = height
        self.width = width
        self.posY = posY
        self.posX = posX

        self.resolutionX = multiplayerResolutionX
        self.resolutionY = multiplayerResolutionY
        self.whatCameraSee = []
        self.whatCameraSee = char_array(self, " ")

    def char_array(self):
        char_array(self)

    def fill_the_camera_view(self):

        i = 0
        g = 0
        for y in range(self.posY, self.height + self.posY):
            for x in range(self.posX, self.width + self.posX):
                for z in range(self.resolutionY):
                    for c in range(self.resolutionX):
                        try:
                            self.whatCameraSee[i + z][g + c] = self.map[y][x]
                        except:
                            break
                g += self.resolutionX
            g = 0
            i += self.resolutionY
        
        i = 0
        g = 0

    # rendering functions
    def draw_map(self):
        for y in range(self.posY, self.height + self.posY):
            for x in range(self.posX, self.width + self.posX):
                try:
                    print(self.map[y][x], end='')
                except:
                    return
            print("")
    #draw_with_resolution is not working btw
    def draw_with_resolution(self):
        self.fill_the_camera_view()
        for y in range(len(self.whatCameraSee)):
            for x in range(len(self.whatCameraSee[0])):
                try:
                    print(self.whatCameraSee[y][x], end='')
                except:
                    return
            print("")
