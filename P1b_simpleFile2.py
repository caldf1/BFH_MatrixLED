#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "wVj" # Change XYZ to the UID of your LED Strip Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_led_strip import BrickletLEDStrip


def clearAll():

    r = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    g = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    i = 0
    a = 0
    while i < 20:
        ls.set_rgb_values(a, 10, r, g, b)
        a += 10;
        i += 1


def createAll():
    # Set first 10 LEDs to green
    r = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    g = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    b = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0]

    i = 0
    a = 1
    while i < 20:
        ls.set_rgb_values(a, 10, r, b, r)
        a += 10;
        i += 1

j = 0
c = 0
def createAll2():
    # Set first 10 LEDs to green
    r = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    g = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    b = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0]

    global c
    c += 10;
    global j
    j += 1
    
    ls.set_rgb_values(c, 10, b, g, b)
 

#Testanfang====================================
NUM_LEDS = 16

r = [0]*NUM_LEDS
g = [0]*NUM_LEDS
b = [0]*NUM_LEDS
r_index = 0

def cb_frame_rendered(length, ls):
    global r_index

    b[r_index] = 0
    if r_index == NUM_LEDS-1:
        r_index = 0
    else:
        r_index += 1
    b[r_index] = 255

    # Set new data for next render cycle
    ls.set_rgb_values(0, NUM_LEDS, r, r, r)
#Testende=======================================


if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    ls = BrickletLEDStrip(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

 #   createAll()

    # Set frame duration to 50ms (20 frames per second)
    ls.set_frame_duration(50)

    # Register frame rendered callback to function cb_frame_rendered
 #   ls.register_callback(ls.CALLBACK_FRAME_RENDERED,
                         #lambda x: clearAll())
#                         lambda x: cb_frame_rendered(x, ls))

    ls.register_callback(ls.CALLBACK_FRAME_RENDERED, createAll())

    # Set initial rgb values to get started
   # ls.set_rgb_values(0, NUM_LEDS, r, g, b)

    input("Press key to exit\n") # Use input() in Python 3
    ipcon.disconnect()

    
