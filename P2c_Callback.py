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



from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_led_strip import BrickletLEDStrip

# Use frame rendered callback to move the active LED every frame
def cb_frame_rendered(length, ls):
    global a
    global b
    global c
    global l
    global r_index
    global s


    if s == 20: # Light off
        a = 0
        c += 1 
        s = 0
        
        i = 0
        x = 0
        while i < 20:
           ls.set_rgb_values(x, NUM_LEDS, b, b, b)
           x += 10
           i += 1


    else: # Light on
        ls.set_rgb_values(a, NUM_LEDS, l, l, l)
        a += 10
        s += 1


    # Set new data for next render cycle
 #   ls.set_rgb_values(s, NUM_LEDS, r, b, b)
 #   s += 10

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
