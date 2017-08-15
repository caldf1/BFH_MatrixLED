#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "wVj" # Change XYZ to the UID of your LED Strip Bricklet


positionA = [
#col  19,  18,  17,  16,  15,  14,  13,  12,  11,  10,  9,  8,  7,  6,  5,  4,  3,  2,  1,  0
#      0    1    2    3    4    5    6    7    8    9  10  11  12  13  14  15  16  17  18  19    
    [190, 189, 170, 169, 150, 149, 130, 129, 110, 109, 90, 89, 70, 69, 50, 49, 30, 29, 10,  9], # 0 | 9 
    [191, 188, 171, 168, 151, 148, 131, 128, 111, 108, 91, 88, 71, 68, 51, 48, 31, 28, 11,  8], # 1 | 8
    [192, 187, 172, 167, 152, 147, 132, 127, 112, 107, 92, 87, 72, 67, 52, 47, 32, 27, 12,  7], # 2 | 7
    [193, 186, 173, 166, 153, 146, 133, 126, 113, 106, 93, 86, 73, 66, 53, 46, 33, 26, 13,  6], # 3 | 6
    [194, 185, 174, 165, 154, 145, 134, 125, 114, 105, 94, 85, 74, 65, 54, 45, 34, 25, 14,  5], # 4 | 5
    [195, 184, 175, 164, 155, 144, 135, 124, 115, 104, 95, 84, 75, 64, 55, 44, 35, 24, 15,  4], # 5 | 4
    [196, 183, 176, 163, 156, 143, 136, 123, 116, 103, 96, 83, 76, 63, 56, 43, 36, 23, 16,  3], # 6 | 3
    [197, 182, 177, 162, 157, 142, 137, 122, 117, 102, 97, 82, 77, 62, 57, 42, 37, 22, 17,  2], # 7 | 2
    [198, 181, 178, 161, 158, 141, 138, 121, 118, 101, 98, 81, 78, 61, 58, 41, 38, 21, 18,  1], # 8 | 1
    [199, 180, 179, 160, 159, 140, 139, 120, 119, 100, 99, 80, 79, 60, 59, 40, 39, 20, 19,  0], # 9 | 0 [9][19]
]

manuell = [
    #0, 1, 2, 3, 4, 5, 6, 7, 8, 9,|10,11,12,13,14,15
    [L, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #0
    [0, 0, 0, 0, 0, 0, 0, 0, 0, L, 0, 0, 0, 0, 0, 0], #1
    [0, 0, L, L, L, L, L, L, 0, 0, 0, 0, 0, 0, 0, 0], #2
    [0, 0, 0, L, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #3
    [0, 0, 0, 0, 0, L, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #4
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #5
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #6
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #7
    [0, 0, 0, L, L, L, L, 0, 0, 0, 0, 0, 0, 0, 0, 0], #8
    [0, 0, 0, L, 0, 0, L, 0, 0, 0, 0, 0, 0, 0, 0, 0], #9
    [0, 0, 0, L, 0, 0, L, 0, 0, 0, 0, 0, 0, 0, 0, 0], #10
    [0, 0, 0, L, L, L, L, 0, 0, 0, 0, 0, 0, 0, 0, 0], #11
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #12
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #13
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #14
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #15
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #16
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #17
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #18
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #19
    ]



# COLORS
# L = 255
W = [ 255, 255, 255]    # white
D = [ 255,   0,   0]    # dark
B = [ 255,   0,   0]    # blue
G = [   0, 255,   0]    # green
R = [   0,   0, 255]    # green
C = [ 255, 255,   0]    # cyan
Y = [   0, 255, 255]    # yellow
M = [ 255,   0, 255]    # magenta

r_index = 0


matrix = [
#col 19, 18, 17, 16, 15, 14, 13, 12, 11, 10,  9,  8,  7,  6,  5,  4,  3,  2,  1,  0
#     0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19    
    [ D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  D], # 0 | 9 
    [ D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  D], # 1 | 8
    [ D,  D,  D,  R,  D,  R,  D,  D,  D,  D,  D,  D,  D,  D,  W,  D,  W,  D,  D,  D], # 2 | 7
    [ D,  D,  R,  R,  R,  R,  R,  D,  D,  D,  D,  D,  D,  W,  W,  W,  W,  W,  D,  D], # 3 | 6
    [ D,  D,  D,  R,  R,  R,  D,  D,  D,  D,  D,  D,  D,  D,  W,  W,  W,  D,  D,  D], # 4 | 5
    [ D,  D,  D,  D,  R,  D,  D,  D,  D,  M,  D,  M,  D,  D,  D,  W,  D,  D,  D,  D], # 5 | 4
    [ D,  D,  D,  D,  D,  D,  D,  D,  M,  M,  M,  M,  M,  D,  D,  D,  D,  D,  D,  D], # 6 | 3
    [ D,  D,  D,  D,  D,  D,  D,  D,  D,  M,  M,  M,  D,  D,  D,  D,  D,  D,  D,  D], # 7 | 2
    [ D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  M,  D,  D,  D,  D,  D,  D,  D,  D,  D], # 8 | 1
    [ D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  D,  D], # 9 | 0 [9][19]
]

values = [[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,
          [0]*16,[0]*16,[0]*16,[0]*16,[0]*16,
          [0]*16,[0]*16,[0]*16,[0]*16,[0]*16,
          [0]*16,[0]*16,[0]*16,[0]*16,[0]*16]#*20

#bgr
vB = [[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,
      [0]*16,[0]*16,[0]*16,[0]*16,[0]*16,
      [0]*16,[0]*16,[0]*16,[0]*16,[0]*16,
      [0]*16,[0]*16,[0]*16,[0]*16,[0]*16]#*20 values blau

#bgr
vG = [[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,
      [0]*16,[0]*16,[0]*16,[0]*16,[0]*16,
      [0]*16,[0]*16,[0]*16,[0]*16,[0]*16,
      [0]*16,[0]*16,[0]*16,[0]*16,[0]*16]#*20 values grün

#bgr
vR = [[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,
      [0]*16,[0]*16,[0]*16,[0]*16,[0]*16,
      [0]*16,[0]*16,[0]*16,[0]*16,[0]*16,
      [0]*16,[0]*16,[0]*16,[0]*16,[0]*16]#*20 values rot


def setValues():
        global values
        global matrix
        ma = 9
        mb = 19
        va = 0 # max. 19
        vb = 0 # max. 9
        while ma >= 0:
            
            while mb >= 0:
                if va % 2 == 1:
                    values[va][ma] = matrix [ma][mb]
                else:
                   values[va][vb] = matrix [ma][mb]
                #print("va: ", va, " vb: ", vb, " ma: ", ma, " mb: ", mb)
                mb -= 1
                va += 1
                               
            ma -= 1
            mb = 19
            va = 0
            vb += 1
            
    
             




#print("L: ", matrix[9][19])
#matrix[9][19] = 100
#print(matrix)
#print("neuer Wert: ", matrix[9][19])
setValues()
#values[18][9] = 100
#print(values)

NUM_LEDS = 10
r = [0]*16
on = 0
#b = [0]*16

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_led_strip import BrickletLEDStrip

# Use frame rendered callback to move the active LED every frame
def cb_frame_rendered(length, ls):    
    global on
    global r

    if on == 1:
        i = 0
        a = 0
        on = 0
        while i < 20:
           ls.set_rgb_values(a, NUM_LEDS, r, r, r)
           a += 10
           i += 1
                
    else:
        i = 0
        while i < 20:
#               ls.set_rgb_values(i*10, NUM_LEDS, r, r, values[i])
               ls.set_rgb_values(i*10, NUM_LEDS, r, values[i], r)
#              ls.set_rgb_values(i*10, NUM_LEDS, values[i], r, r)
#              ls.set_rgb_values(i*10, NUM_LEDS, values[i], values[i], values[i])
               i += 1
               on = 1

    

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    ls = BrickletLEDStrip(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Set frame duration to 50ms (20 frames per second)
    ls.set_frame_duration(500)

    # Register frame rendered callback to function cb_frame_rendered
    ls.register_callback(ls.CALLBACK_FRAME_RENDERED,
                         lambda x: cb_frame_rendered(x, ls))

    # Set initial rgb values to get started
 #   ls.set_rgb_values(0, 0, r, g, b)

    input("Press key to exit\n") # Use input() in Python 3
    ipcon.disconnect()
