#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "wVj" # Change XYZ to the UID of your LED Strip Bricklet

NUM_LEDS = 10
a = 0
b = [0]*16 # light
c = 0   # cycle number
l = [255]*16 # light
r_index = 0
s = 0   # Anzahl frames 0-19
d = 1   # Richtung: 0 = re -> li | 1 = li -> re

if d == 1:
    a = 190


print("a: ", a, " s: ", s, " c: ", c)

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
                      
    if s < 20:
        if c == 0:
            ls.set_rgb_values(a, NUM_LEDS, l, l, l) # 1. Zyklus: weiss

        if c == 1:
            ls.set_rgb_values(a, NUM_LEDS, l, b, b) # 1. Zyklus: blau

        if c == 2:
            ls.set_rgb_values(a, NUM_LEDS, b, l, b) # 1. Zyklus: grün

        if c == 3:
            ls.set_rgb_values(a, NUM_LEDS, b, b, l) # 1. Zyklus: rot

        if c == 4:
            ls.set_rgb_values(a, NUM_LEDS, b, b, b) # 1. Zyklus: dunkel

        if c == 5:
             c = 0 
        s += 1

        if d == 0:
            a += 10
        else:
            a -= 10

    else:
        s = 0
        c += 1
        if d == 0:
            a = 0
        else:
            a = 190


#        if d == 0:
#            a += 10
#        elif d == 1:
#            a -= 10
   
    
#        if d == 0:
#            a = 0
#        elif d == 1:
#            a = 190

 

    # Set new data for next render cycle
 #   ls.set_rgb_values(s, NUM_LEDS, r, b, b)
 #   s += 10

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
 #   ls.set_rgb_values(0, 0, r, g, b)

    input("Press key to exit\n") # Use input() in Python 3
    ipcon.disconnect()
