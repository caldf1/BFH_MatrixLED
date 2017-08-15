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
z = 0

if d == 1:
    a = 190




from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_led_strip import BrickletLEDStrip

# Use frame rendered callback to move the active LED every frame

def test():
    global a
    global b
    global c
    global d
    global l
    global s
    global z
    
    while z == 0:
        #print("a: ", a, " s: ", s, " c: ", c)                         
        if s < 20:
            print("a: ", a, " s: ", s, " c: ", c)  
            if c == 2:
                 c = 0
                 z = 1
             
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


#test()

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    ls = BrickletLEDStrip(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    l = [255,255,255,255,255,255,255,255,255,255,0,0,0,0,0,0]
    b = [0]*16

    i = 0
    a = 0
    while i < 20:
        ls.set_rgb_values(a, 10, b, b, b)
        a += 10;
        i += 1
        

    ls.set_rgb_values(199, 1, l, l, b) 
    
    input("Press key to exit\n") # Use input() in Python 3
    ipcon.disconnect()
    
