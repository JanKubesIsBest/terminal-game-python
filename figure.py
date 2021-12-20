class figure:
    def __init__(self, _map, posX, posY, speed, skin):
        self.map = _map
        self.posX = posX
        self.posY = posY
        
        self.speed = speed
        self.skin = skin
        self.gravity = 1

        self.pastObstacleOnTheMap = " "

        self.is_on_floor = False
        self.alive = True
    def exist(self):
        if (self.pastObstacleOnTheMap == "_"):
            self.is_on_floor = True
        else:
            self.is_on_floor = False
        if self.is_on_floor == False:
            self.fall()
        
        self.draw_on_map()

    def fall(self):
        self.moveY(1)

    def moveX(self, direction):
        self.map[self.posY][self.posX] = self.pastObstacleOnTheMap
        self.posX += 1 * self.speed * direction
        self.pastObstacleOnTheMap = self.map[self.posY][self.posX]


    def moveY(self, direction):
        self.map[self.posY][self.posX] = self.pastObstacleOnTheMap
        self.posY += 1 * self.speed * direction
        self.pastObstacleOnTheMap = self.map[self.posY][self.posX]

    def draw_on_map(self):
        self.map[self.posY][self.posX] = self.skin
    