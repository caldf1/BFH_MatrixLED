#!/usr/bin/env python
# -*- coding: utf-8 -*-

#======= Simpel RGB nur 1 Wert =============================================================

matrix2 = [[0 for i in range(20)] for i in range(10)]
rgb2    = [[0 for i in range(16)] for i in range(20)]


# Matrix initialisieren, Werte von 199 bis 0, oben links nach unten rechts
def initMatrix2():
    x = 0
    y = 0 
    value = 199
    while x < 20:
        if x %2 == 1:   # wenn x ungerade, dann y von 0 bis 9 abfüllen
            y = 0
            while y < 10:
                matrix2[y][x] = value
                y += 1
                value -= 1           

        else:          # (x %2 == 0) wenn x gerade, dann y von 9 bis 0 abfüllen
            y = 9
            while y > -1:
                matrix2[y][x] = value
                y -= 1
                value -= 1
        x += 1

# rgb-Tabelle initialisieren für Tests
def initRGB2():
    x = 0
    y = 0
    value = 0
    while y < 20:
        while x < 10:
            rgb2[y][x] = value
            x += 1
            value += 1
        x = 0
        y += 1

# Überführen der Werte von der Matrix in die rgb-Tabelle
def mapping2():
    xMatrix = 19 # 0-19
    yMatrix = 9  # 0-9
    xRGB = 0     # 0-9
    yRGB = 0     # 0-19

    # Iteration Matrix von [9][19] (unten rechts) nach [0][0] (oben links)
    # Iteration RGB von [0][0] (oben links) nach [19][9] (unten rechts)
    while xMatrix > -1:
        if xMatrix %2 == 1: # wenn x der Matrix ungerade, dann y von 9 bis 0 herausholen
            yMatrix = 9
            while yMatrix > -1:
                rgb2[yRGB][xRGB] = matrix2[yMatrix][xMatrix]
                xRGB += 1
                yMatrix -= 1
            xRGB = 0

        else:            # wenn x der Matrix gerade, dann y von 0 bis 9 herausholen
            yMatrix = 0
            while yMatrix < 10:
                rgb2[yRGB][xRGB] = matrix2[yMatrix][xMatrix]
                xRGB += 1
                yMatrix += 1
            xRGB = 0
        xMatrix -= 1
        yRGB += 1

# Ausgabe Wert der Position x,y
def getIndex2(x,y): # x: 0-19 | y: 0-9
    return matrix2[x][y]

def printMatrix():
    for x in matrix:
        print(x)

def printRGB2():
    for x in rgb2:
        print(x)

#======= Mit RGB [r, g, b] ===============================================================

matrix = [[[0 for i in range(3)] for i in range(20)] for i in range(10)]
rgb    = [[[0 for i in range(3)] for i in range(16)] for i in range(20)]
red    = [[0 for i in range(16)] for i in range(20)]
green  = [[0 for i in range(16)] for i in range(20)]
blue   = [[0 for i in range(16)] for i in range(20)]

R = 0
G = 1
B = 2
INDEX = 4 #?



# Matrix initialisieren, Werte von 199 bis 0, oben links nach unten rechts
def initMatrix():
    x = 0
    y = 0 
    value = 255

    while x < 20:
        if x %2 == 1:   # wenn x ungerade, dann y von 0 bis 9 abfüllen
            y = 0
            while y < 10:
                matrix[y][x][R] = value
                matrix[y][x][G] = value
                matrix[y][x][B] = value
                y += 1
                value -= 1           

        else:          # (x %2 == 0) wenn x gerade, dann y von 9 bis 0 abfüllen
            y = 9
            while y > -1:
                matrix[y][x][R] = value
                matrix[y][x][G] = value
                matrix[y][x][B] = value
                y -= 1
                value -= 1
        x += 1
 
# Überführen der Werte von der Matrix in die rgb-Tabelle
def mapping():
    xMatrix = 19 # 0-19
    yMatrix = 9  # 0-9
    xRGB = 0     # 0-9
    yRGB = 0     # 0-19

    # Iteration Matrix von [9][19] (unten rechts) nach [0][0] (oben links)
    # Iteration RGB von [0][0] (oben links) nach [19][9] (unten rechts)
    while xMatrix > -1:
        if xMatrix %2 == 1: # wenn x der Matrix ungerade, dann y von 9 bis 0 herausholen
            yMatrix = 9
            while yMatrix > -1:
                rgb[yRGB][xRGB][R] = matrix[yMatrix][xMatrix][R]
                rgb[yRGB][xRGB][G] = matrix[yMatrix][xMatrix][G]
                rgb[yRGB][xRGB][B] = matrix[yMatrix][xMatrix][B]
                red[yRGB][xRGB] = matrix[yMatrix][xMatrix][R]
                green[yRGB][xRGB] = matrix[yMatrix][xMatrix][G]
                blue[yRGB][xRGB] = matrix[yMatrix][xMatrix][B]               
                xRGB += 1
                yMatrix -= 1
            xRGB = 0

        else:            # wenn x der Matrix gerade, dann y von 0 bis 9 herausholen
            yMatrix = 0
            while yMatrix < 10:
                rgb[yRGB][xRGB][R] = matrix[yMatrix][xMatrix][R]
                rgb[yRGB][xRGB][G] = matrix[yMatrix][xMatrix][G]
                rgb[yRGB][xRGB][B] = matrix[yMatrix][xMatrix][B]
                red[yRGB][xRGB] = matrix[yMatrix][xMatrix][R]
                green[yRGB][xRGB] = matrix[yMatrix][xMatrix][G]
                blue[yRGB][xRGB] = matrix[yMatrix][xMatrix][B]
                xRGB += 1
                yMatrix += 1
            xRGB = 0
        xMatrix -= 1
        yRGB += 1



# mit allen Farbwerten RGB
def printMatrix2():
    for x in matrix2:
        print(y)

def printRGB():
    for x in rgb:
        print(x)

def printRed():
    for x in red:
        print(x)

def printGreen():
    for x in green:
        print(x)

def printBlue():
    for x in blue:
        print(x)


#======= Output / Tests =============================================================


initMatrix()

x = 0 # -19
while x < 20:
    matrix[0][x] = [255,0,0]
    x += 1
x = 0
while x < 20:
    matrix[9][x] = [0,255,0]
    x += 1

matrix[2][2] = [0,0,255]
    
mapping()
#printRed()
#printGreen()
#printBlue()
#printRGB()
#initMatrix2()
#printMatrix()
#print(getIndex(0,0))
#initRGB2()
#printRGB2()
#printMatrix2()

# ein einzelnes, statisches Bild anzeigen
def showPicture():
     i = 0
     while i < 20:
          ls.set_rgb_values(i*10, 10, blue[i], green[i], red[i])
          i += 1

#========= Output LED-Wand ============================================================
# Imports:
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_led_strip import BrickletLEDStrip

HOST = "localhost"
PORT = 4223
UID = "wVj" # UID of your LED Strip Bricklet

cycle = 0 # Anzahl Durchläufe
frameIndex = 0 # 0-19 (20 Frames = 1 Durchlauf)

# Use frame rendered callback to move the active LED every frame
def cb_frame_rendered(length, ls):
     global frameIndex
     global cycle

     showPicture()

 #    movePicture(OL) # Fehler bei OL
 #    movePicture(R)
 #    showPicture()
 #    lightOff()
     if frameIndex < 20:
          frameIndex += 1
     else:
          frameIndex = 0
          cycle += 1



if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    ls = BrickletLEDStrip(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Set frame duration to 50ms (20 frames per second)
    ls.set_frame_duration(250)

    # Register frame rendered callback to function cb_frame_rendered
    ls.register_callback(ls.CALLBACK_FRAME_RENDERED,
                         lambda x: cb_frame_rendered(x, ls))

    # Set initial rgb values to get started
 #   ls.set_rgb_values(0, 0, r, g, b)

    input("Press key to exit\n") # Use input() in Python 3
    ipcon.disconnect()

