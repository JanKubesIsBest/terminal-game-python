from figure import figure
import keyboard
from camera import camera
from window import window

class player(figure):

    def __init__(self, _map, posX, posY, speed, skin, height, width):
        super().__init__(_map, posX, posY, speed, skin)
        self.camera = camera(self.map, height, width, round(self.posX - width / 2), round(self.posY - height / 2), 3, 3)
        self.jump = 10
        self.points = 0

        self.window = window(5, 10)
        self.window.add_text("points:" + str(self.points), 0, 2)

    def exist(self):
        
        if self.is_on_floor == True:
            if keyboard.is_pressed('d') and self.posX < len(self.map[0]):  # if key 'q' is pressed 
                self.moveX(1)
            if (keyboard.is_pressed('a') and self.posX > 0):
                self.moveX(-1)
            if keyboard.is_pressed('w'):
                self.moveY(-3)
    
        if self.pastObstacleOnTheMap == "*":
            self.points += 1
            self.window.add_text("points:" + str(self.points), 0, 2)
            self.pastObstacleOnTheMap = " "

        super().exist()

        self.camera.map = self.map
        self.camera.draw_map()

        self.window.draw_map(self.window.map)
    def moveX(self, direction):
        super().moveX(direction)
        self.camera.posX = round(self.posX - self.camera.width / 2)

    def moveY(self, direction):
        super().moveY(direction)
        self.camera.posY = round(self.posY - self.camera.height / 2)
        
    