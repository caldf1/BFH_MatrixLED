#!/usr/bin/env python
# -*- coding: utf-8 -*-

matrix = [[0 for i in range(20)] for i in range(10)]
matrix2 = [[[0 for i in range(3)] for i in range(20)] for i in range(10)]
rgb = [[0 for i in range(16)] for i in range(20)]
red = [[0 for i in range(16)] for i in range(20)]
green = [[0 for i in range(16)] for i in range(20)]
blue = [[0 for i in range(16)] for i in range(20)]

# Eingabematrix drucken
def printMatrix():
    for x in matrix:
        print(x)

def printMatrix2():
    for x in matrix2:
        print(x)

# Matrix-Farbwerte drucken
def printRGB():
    for x in rgb:
        print(x)

# Matrix initialisieren, Werte von 199 bis 0, oben links nach unten rechts
def initMatrix():
    x = 0
    y = 0 
    value = 199
    while x < 20:
        if x %2 == 1:   # wenn x ungerade, dann y von 0 bis 9 abfüllen
            y = 0
            while y < 10:
                matrix[y][x] = value
                y += 1
                value -= 1           

        else:          # (x %2 == 0) wenn x gerade, dann y von 9 bis 0 abfüllen
            y = 9
            while y > -1:
                matrix [y][x] = value
                y -= 1
                value -= 1
        x += 1


def initRGB():
    x = 0
    y = 0
    value = 0
    while y < 20:
        while x < 10:
            rgb[y][x] = value
            x += 1
            value += 1
        x = 0
        y += 1


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
                rgb[yRGB][xRGB] = matrix[yMatrix][xMatrix]
                xRGB += 1
                yMatrix -= 1
            xRGB = 0

        else:            # wenn x der Matrix gerade, dann y von 0 bis 9 herausholen
            yMatrix = 0
            while yMatrix < 10:
                rgb[yRGB][xRGB] = matrix[yMatrix][xMatrix]
                xRGB += 1
                yMatrix += 1
            xRGB = 0
        xMatrix -= 1
        yRGB += 1




    
# Ausgabe Wert der Position x,y
def getIndex(x,y): # x: 0-19 | y: 0-9
    return matrix[x][y]


initMatrix()
#printMatrix()
#print(getIndex(0,0))
#initRGB()
mapping()
#printMatrix()
printRGB()
#printMatrix2()

