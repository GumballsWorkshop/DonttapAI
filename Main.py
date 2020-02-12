import numpy as np
from PIL import ImageGrab
from directKeys import click
import time

gameCoords = [454, 182, 889, 617]
gameWidth = gameCoords[2] - gameCoords[0]
gameHeight = gameCoords[3] - gameCoords[1]
stepX = gameWidth // 8
stepY = gameHeight // 8

time.sleep(7)

def clickSquare (screen):
    global stepX, stepY, gameWidth, gameHeight, gameCoords
    for x in range(stepX, gameWidth, stepX * 2):
        for y in range(stepY, gameHeight, stepY * 2):
            if (screen[y][x]) < 10:
                actualX = x + gameCoords[0]
                actualY = y + gameCoords[1]
                click(actualX, actualY)
                # print("looking at x: {}, y: {}".format(x, y))
                # print("pixel value: {}".format(screen[x][y]))
                # print("clicked at x: {}, y: {}".format(actualX, actualY))
    time.sleep(0.05)



for i in range(1000):
    startTime = time.time()
    screen = np.array(ImageGrab.grab(bbox=gameCoords).convert("L"))
    clickSquare(screen)
    # if i == 0:
    #     np.savetxt('values.csv', screen, fmt="%d", delimiter=",")
    print("Frame took {} seconds. Up to frame no {}".format((time.time() - startTime), i))
