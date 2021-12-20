import os
from time import sleep
from camera import camera
from map import map
from player import player



def main():
    game_map = map()
    my_player = player(game_map.map, 6, 5, 1, "+", 7, 7)

    while (True):
        my_player.exist()

        #game_map.draw_map(game_map.map)
        sleep(1 % 240)
        os.system("cls")



main()
