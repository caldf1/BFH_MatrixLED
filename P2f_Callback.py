#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "wVj" # Change XYZ to the UID of your LED Strip Bricklet

TEN = 10
a = 0
b = [0]*16          # light
c = 0               # cycle number
l = [255]*16        # light
r_index = 0
s = 0               # Anzahl frames 0-19
d = 0               # Richtung: 0 = re -> li | 1 = li -> re

if d == 1:
    a = 190

array = [
    [a, l, l, l, 0],
    [a, l, l, b, 1],
    [a, l, b, b, 0],
    [a, b, b, b, 1],
 #   [a, l, l, l, 0],
#    [a, l, l, l, 0],
#    [a, l, l, l, 0],
    ]

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_led_strip import BrickletLEDStrip

# Use frame rendered callback to move the active LED every frame
def cb_frame_rendered(length, ls):
    
    global a
    global b
    global c
    global d
    global l
    global r_index
    global s
    global array
    r = 0
    arr = array[r_index]

                      
    if s < 20: # durchläufe
        ls.set_rgb_values(a, TEN, arr[1], arr[2] , arr[3])

        s += 1
        
        if d == 0:
            a += 10
        else:
            a -= 10

    

    else:   # zurücksetzen
        s = 0
        
        
        if d == 0:
            a = 0       
        else:
            a = 190





if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    ls = BrickletLEDStrip(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Set frame duration to 50ms (20 frames per second)
    ls.set_frame_duration(150)

    # Register frame rendered callback to function cb_frame_rendered
    ls.register_callback(ls.CALLBACK_FRAME_RENDERED,
                         lambda x: cb_frame_rendered(x, ls))

    # Set initial rgb values to get started
   #ls.set_rgb_values(0, 0, r, g, b)

    input("Press key to exit\n") # Use input() in Python 3
    ipcon.disconnect()
