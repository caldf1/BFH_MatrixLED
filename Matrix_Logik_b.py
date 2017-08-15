#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports:
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_led_strip import BrickletLEDStrip

# Array der 200 Pixel mit ID, IDY, IDX, R, G, B, A, AY, AX
Mapping = [
    [1,9,19,0,0,0,0,0,0],
    [2,8,19,0,0,0,1,0,1],
    [3,7,19,0,0,0,2,0,2],
    [4,6,19,0,0,0,3,0,3],
    [5,5,19,0,0,0,4,0,4],
    [6,4,19,0,0,0,5,0,5],
    [7,3,19,0,0,0,6,0,6],
    [8,2,19,0,0,0,7,0,7],
    [9,1,19,0,0,0,8,0,8],
    [10,0,19,0,0,0,9,0,9],
    [11,9,18,0,0,0,19,1,9],
    [12,8,18,0,0,0,18,1,8],
    [13,7,18,0,0,0,17,1,7],
    [14,6,18,0,0,0,16,1,6],
    [15,5,18,0,0,0,15,1,5],
    [16,4,18,0,0,0,14,1,4],
    [17,3,18,0,0,0,13,1,3],
    [18,2,18,0,0,0,12,1,2],
    [19,1,18,0,0,0,11,1,1],
    [20,0,18,0,0,0,10,1,0],
    [21,9,17,0,0,0,20,2,0],
    [22,8,17,0,0,0,21,2,1],
    [23,7,17,0,0,0,22,2,2],
    [24,6,17,0,0,0,23,2,3],
    [25,5,17,0,0,0,24,2,4],
    [26,4,17,0,0,0,25,2,5],
    [27,3,17,0,0,0,26,2,6],
    [28,2,17,0,0,0,27,2,7],
    [29,1,17,0,0,0,28,2,8],
    [30,0,17,0,0,0,29,2,9],
    [31,9,16,0,0,0,39,3,9],
    [32,8,16,0,0,0,38,3,8],
    [33,7,16,0,0,0,37,3,7],
    [34,6,16,0,0,0,36,3,6],
    [35,5,16,0,0,0,35,3,5],
    [36,4,16,0,0,0,34,3,4],
    [37,3,16,0,0,0,33,3,3],
    [38,2,16,0,0,0,32,3,2],
    [39,1,16,0,0,0,31,3,1],
    [40,0,16,0,0,0,30,3,0],
    [41,9,15,0,0,0,40,4,0],
    [42,8,15,0,0,0,41,4,1],
    [43,7,15,0,0,0,42,4,2],
    [44,6,15,0,0,0,43,4,3],
    [45,5,15,0,0,0,44,4,4],
    [46,4,15,0,0,0,45,4,5],
    [47,3,15,0,0,0,46,4,6],
    [48,2,15,0,0,0,47,4,7],
    [49,1,15,0,0,0,48,4,8],
    [50,0,15,0,0,0,49,4,9],
    [51,9,14,0,0,0,59,5,9],
    [52,8,14,0,0,0,58,5,8],
    [53,7,14,0,0,0,57,5,7],
    [54,6,14,0,0,0,56,5,6],
    [55,5,14,0,0,0,55,5,5],
    [56,4,14,0,0,0,54,5,4],
    [57,3,14,0,0,0,53,5,3],
    [58,2,14,0,0,0,52,5,2],
    [59,1,14,0,0,0,51,5,1],
    [60,0,14,0,0,0,50,5,0],
    [61,9,13,0,0,0,60,6,0],
    [62,8,13,0,0,0,61,6,1],
    [63,7,13,0,0,0,62,6,2],
    [64,6,13,0,0,0,63,6,3],
    [65,5,13,0,0,0,64,6,4],
    [66,4,13,0,0,0,65,6,5],
    [67,3,13,0,0,0,66,6,6],
    [68,2,13,0,0,0,67,6,7],
    [69,1,13,0,0,0,68,6,8],
    [70,0,13,0,0,0,69,6,9],
    [71,9,12,0,0,0,79,7,9],
    [72,8,12,0,0,0,78,7,8],
    [73,7,12,0,0,0,77,7,7],
    [74,6,12,0,0,0,76,7,6],
    [75,5,12,0,0,0,75,7,5],
    [76,4,12,0,0,0,74,7,4],
    [77,3,12,0,0,0,73,7,3],
    [78,2,12,0,0,0,72,7,2],
    [79,1,12,0,0,0,71,7,1],
    [80,0,12,0,0,0,70,7,0],
    [81,9,11,0,0,0,80,8,0],
    [82,8,11,0,0,0,81,8,1],
    [83,7,11,0,0,0,82,8,2],
    [84,6,11,0,0,0,83,8,3],
    [85,5,11,0,0,0,84,8,4],
    [86,4,11,0,0,0,85,8,5],
    [87,3,11,0,0,0,86,8,6],
    [88,2,11,0,0,0,87,8,7],
    [89,1,11,0,0,0,88,8,8],
    [90,0,11,0,0,0,89,8,9],
    [91,9,10,0,0,0,99,9,9],
    [92,8,10,0,0,0,98,9,8],
    [93,7,10,0,0,0,97,9,7],
    [94,6,10,0,0,0,96,9,6],
    [95,5,10,0,0,0,95,9,5],
    [96,4,10,0,0,0,94,9,4],
    [97,3,10,0,0,0,93,9,3],
    [98,2,10,0,0,0,92,9,2],
    [99,1,10,0,0,0,91,9,1],
    [100,0,10,0,0,0,90,9,0],
    [101,9,9,0,0,0,100,10,0],
    [102,8,9,0,0,0,101,10,1],
    [103,7,9,0,0,0,102,10,2],
    [104,6,9,0,0,0,103,10,3],
    [105,5,9,0,0,0,104,10,4],
    [106,4,9,0,0,0,105,10,5],
    [107,3,9,0,0,0,106,10,6],
    [108,2,9,0,0,0,107,10,7],
    [109,1,9,0,0,0,108,10,8],
    [110,0,9,0,0,0,109,10,9],
    [111,9,8,0,0,0,119,11,9],
    [112,8,8,0,0,0,118,11,8],
    [113,7,8,0,0,0,117,11,7],
    [114,6,8,0,0,0,116,11,6],
    [115,5,8,0,0,0,115,11,5],
    [116,4,8,0,0,0,114,11,4],
    [117,3,8,0,0,0,113,11,3],
    [118,2,8,0,0,0,112,11,2],
    [119,1,8,0,0,0,111,11,1],
    [120,0,8,0,0,0,110,11,0],
    [121,9,7,0,0,0,120,12,0],
    [122,8,7,0,0,0,121,12,1],
    [123,7,7,0,0,0,122,12,2],
    [124,6,7,0,0,0,123,12,3],
    [125,5,7,0,0,0,124,12,4],
    [126,4,7,0,0,0,125,12,5],
    [127,3,7,0,0,0,126,12,6],
    [128,2,7,0,0,0,127,12,7],
    [129,1,7,0,0,0,128,12,8],
    [130,0,7,0,0,0,129,12,9],
    [131,9,6,0,0,0,139,13,9],
    [132,8,6,0,0,0,138,13,8],
    [133,7,6,0,0,0,137,13,7],
    [134,6,6,0,0,0,136,13,6],
    [135,5,6,0,0,0,135,13,5],
    [136,4,6,0,0,0,134,13,4],
    [137,3,6,0,0,0,133,13,3],
    [138,2,6,0,0,0,132,13,2],
    [139,1,6,0,0,0,131,13,1],
    [140,0,6,0,0,0,130,13,0],
    [141,9,5,0,0,0,140,14,0],
    [142,8,5,0,0,0,141,14,1],
    [143,7,5,0,0,0,142,14,2],
    [144,6,5,0,0,0,143,14,3],
    [145,5,5,0,0,0,144,14,4],
    [146,4,5,0,0,0,145,14,5],
    [147,3,5,0,0,0,146,14,6],
    [148,2,5,0,0,0,147,14,7],
    [149,1,5,0,0,0,148,14,8],
    [150,0,5,0,0,0,149,14,9],
    [151,9,4,0,0,0,159,15,9],
    [152,8,4,0,0,0,158,15,8],
    [153,7,4,0,0,0,157,15,7],
    [154,6,4,0,0,0,156,15,6],
    [155,5,4,0,0,0,155,15,5],
    [156,4,4,0,0,0,154,15,4],
    [157,3,4,0,0,0,153,15,3],
    [158,2,4,0,0,0,152,15,2],
    [159,1,4,0,0,0,151,15,1],
    [160,0,4,0,0,0,150,15,0],
    [161,9,3,0,0,0,160,16,0],
    [162,8,3,0,0,0,161,16,1],
    [163,7,3,0,0,0,162,16,2],
    [164,6,3,0,0,0,163,16,3],
    [165,5,3,0,0,0,164,16,4],
    [166,4,3,0,0,0,165,16,5],
    [167,3,3,0,0,0,166,16,6],
    [168,2,3,0,0,0,167,16,7],
    [169,1,3,0,0,0,168,16,8],
    [170,0,3,0,0,0,169,16,9],
    [171,9,2,0,0,0,179,17,9],
    [172,8,2,0,0,0,178,17,8],
    [173,7,2,0,0,0,177,17,7],
    [174,6,2,0,0,0,176,17,6],
    [175,5,2,0,0,0,175,17,5],
    [176,4,2,0,0,0,174,17,4],
    [177,3,2,0,0,0,173,17,3],
    [178,2,2,0,0,0,172,17,2],
    [179,1,2,0,0,0,171,17,1],
    [180,0,2,0,0,0,170,17,0],
    [181,9,1,0,0,0,180,18,0],
    [182,8,1,0,0,0,181,18,1],
    [183,7,1,0,0,0,182,18,2],
    [184,6,1,0,0,0,183,18,3],
    [185,5,1,0,0,0,184,18,4],
    [186,4,1,0,0,0,185,18,5],
    [187,3,1,0,0,0,186,18,6],
    [188,2,1,0,0,0,187,18,7],
    [189,1,1,0,0,0,188,18,8],
    [190,0,1,0,0,0,189,18,9],
    [191,9,0,0,0,0,199,19,9],
    [192,8,0,0,0,0,198,19,8],
    [193,7,0,0,0,0,197,19,7],
    [194,6,0,0,0,0,196,19,6],
    [195,5,0,0,0,0,195,19,5],
    [196,4,0,0,0,0,194,19,4],
    [197,3,0,0,0,0,193,19,3],
    [198,2,0,0,0,0,192,19,2],
    [199,1,0,0,0,0,191,19,1],
    [200,0,0,0,0,0,190,19,0],
    ]

# Wertearray A, AY, AX, R, G, B, O, OR, R, UR, U, UL, L, OL
Valueset = [
    [0,0,0,0,0,0,1,198,199,190,9,10,19,18,],
    [1,0,1,0,0,0,2,197,198,199,0,19,18,17,],
    [2,0,2,0,0,0,3,196,197,198,1,18,17,16,],
    [3,0,3,0,0,0,4,195,196,197,2,17,16,15,],
    [4,0,4,0,0,0,5,194,195,196,3,16,15,14,],
    [5,0,5,0,0,0,6,193,194,195,4,15,14,13,],
    [6,0,6,0,0,0,7,192,193,194,5,14,13,12,],
    [7,0,7,0,0,0,8,191,192,193,6,13,12,11,],
    [8,0,8,0,0,0,9,190,191,192,7,12,11,10,],
    [9,0,9,0,0,0,0,199,190,191,8,11,10,19,],
    [10,1,0,0,0,0,19,0,9,8,11,28,29,20,],
    [11,1,1,0,0,0,10,9,8,7,12,27,28,29,],
    [12,1,2,0,0,0,11,8,7,6,13,26,27,28,],
    [13,1,3,0,0,0,12,7,6,5,14,25,26,27,],
    [14,1,4,0,0,0,13,6,5,4,15,24,25,26,],
    [15,1,5,0,0,0,14,5,4,3,16,23,24,25,],
    [16,1,6,0,0,0,15,4,3,2,17,22,23,24,],
    [17,1,7,0,0,0,16,3,2,1,18,21,22,23,],
    [18,1,8,0,0,0,17,2,1,0,19,20,21,22,],
    [19,1,9,0,0,0,18,1,0,9,10,29,20,21,],
    [20,2,0,0,0,0,21,18,19,10,29,30,39,38,],
    [21,2,1,0,0,0,22,17,18,19,20,39,38,37,],
    [22,2,2,0,0,0,23,16,17,18,21,38,37,36,],
    [23,2,3,0,0,0,24,15,16,17,22,37,36,35,],
    [24,2,4,0,0,0,25,14,15,16,23,36,35,34,],
    [25,2,5,0,0,0,26,13,14,15,24,35,34,33,],
    [26,2,6,0,0,0,27,12,13,14,25,34,33,32,],
    [27,2,7,0,0,0,28,11,12,13,26,33,32,31,],
    [28,2,8,0,0,0,29,10,11,12,27,32,31,30,],
    [29,2,9,0,0,0,20,19,10,11,28,31,30,29,],
    [30,3,0,0,0,0,39,20,29,28,31,48,49,40,],
    [31,3,1,0,0,0,30,29,28,27,32,47,48,49,],
    [32,3,2,0,0,0,31,28,27,26,33,46,47,48,],
    [33,3,3,0,0,0,32,27,26,25,34,45,46,47,],
    [34,3,4,0,0,0,33,26,25,24,35,44,45,46,],
    [35,3,5,0,0,0,34,25,24,23,36,43,44,45,],
    [36,3,6,0,0,0,35,24,23,22,37,42,43,44,],
    [37,3,7,0,0,0,36,23,22,21,38,41,42,43,],
    [38,3,8,0,0,0,37,22,21,20,39,40,41,42,],
    [39,3,9,0,0,0,38,21,20,29,30,49,40,41,],
    [40,4,0,0,0,0,41,38,39,30,49,50,59,58,],
    [41,4,1,0,0,0,42,37,38,39,40,59,58,57,],
    [42,4,2,0,0,0,43,36,37,38,41,58,57,56,],
    [43,4,3,0,0,0,44,35,36,37,42,57,56,55,],
    [44,4,4,0,0,0,45,34,35,36,43,56,55,54,],
    [45,4,5,0,0,0,46,33,34,35,44,55,54,53,],
    [46,4,6,0,0,0,47,32,33,34,45,54,53,52,],
    [47,4,7,0,0,0,48,31,32,33,46,53,52,51,],
    [48,4,8,0,0,0,49,30,31,32,47,52,51,50,],
    [49,4,9,0,0,0,40,39,30,31,48,51,50,59,],
    [50,5,0,0,0,0,59,40,49,48,51,68,69,60,],
    [51,5,1,0,0,0,50,49,48,47,52,67,68,69,],
    [52,5,2,0,0,0,51,48,47,46,53,66,67,68,],
    [53,5,3,0,0,0,52,47,46,45,54,65,66,67,],
    [54,5,4,0,0,0,53,46,45,44,55,64,65,66,],
    [55,5,5,0,0,0,54,45,44,43,56,63,64,65,],
    [56,5,6,0,0,0,55,44,43,42,57,62,63,64,],
    [57,5,7,0,0,0,56,43,42,41,58,61,62,63,],
    [58,5,8,0,0,0,57,42,41,40,59,60,61,62,],
    [59,5,9,0,0,0,58,41,40,49,50,69,60,61,],
    [60,6,0,0,0,0,61,58,59,50,69,70,79,78,],
    [61,6,1,0,0,0,62,57,58,59,60,79,78,77,],
    [62,6,2,0,0,0,63,56,57,58,61,78,77,76,],
    [63,6,3,0,0,0,64,55,56,57,62,77,76,75,],
    [64,6,4,0,0,0,65,54,55,56,63,76,75,74,],
    [65,6,5,0,0,0,66,53,54,55,64,75,74,73,],
    [66,6,6,0,0,0,67,52,53,54,65,74,73,72,],
    [67,6,7,0,0,0,68,51,52,53,66,73,72,71,],
    [68,6,8,0,0,0,69,50,51,52,67,72,71,70,],
    [69,6,9,0,0,0,60,59,50,51,68,71,70,79,],
    [70,7,0,0,0,0,79,60,69,68,71,88,89,80,],
    [71,7,1,0,0,0,70,69,68,67,72,87,88,89,],
    [72,7,2,0,0,0,71,68,67,66,73,86,87,88,],
    [73,7,3,0,0,0,72,67,66,65,74,85,86,87,],
    [74,7,4,0,0,0,73,66,65,64,75,84,85,86,],
    [75,7,5,0,0,0,74,65,64,63,76,83,84,85,],
    [76,7,6,0,0,0,75,64,63,62,77,82,83,84,],
    [77,7,7,0,0,0,76,63,62,61,78,81,82,83,],
    [78,7,8,0,0,0,77,62,61,60,79,80,81,82,],
    [79,7,9,0,0,0,78,61,60,69,70,89,80,81,],
    [80,8,0,0,0,0,81,78,79,70,89,90,99,98,],
    [81,8,1,0,0,0,82,77,78,79,80,99,98,97,],
    [82,8,2,0,0,0,83,76,77,78,81,98,97,96,],
    [83,8,3,0,0,0,84,75,76,77,82,97,96,95,],
    [84,8,4,0,0,0,85,74,75,76,83,96,95,94,],
    [85,8,5,0,0,0,86,73,74,75,84,95,94,93,],
    [86,8,6,0,0,0,87,72,73,74,85,94,93,92,],
    [87,8,7,0,0,0,88,71,72,73,86,93,92,91,],
    [88,8,8,0,0,0,89,70,71,72,87,92,91,90,],
    [89,8,9,0,0,0,80,79,70,71,88,91,90,99,],
    [90,9,0,0,0,0,99,80,89,88,91,108,109,100,],
    [91,9,1,0,0,0,90,89,88,87,92,107,108,109,],
    [92,9,2,0,0,0,91,88,87,86,93,106,107,108,],
    [93,9,3,0,0,0,92,87,86,85,94,105,106,107,],
    [94,9,4,0,0,0,93,86,85,84,95,104,105,106,],
    [95,9,5,0,0,0,94,85,84,83,96,103,104,105,],
    [96,9,6,0,0,0,95,84,83,82,97,102,103,104,],
    [97,9,7,0,0,0,96,83,82,81,98,101,102,103,],
    [98,9,8,0,0,0,97,82,81,80,99,100,101,102,],
    [99,9,9,0,0,0,98,81,80,89,90,109,100,101,],
    [100,10,0,0,0,0,101,98,99,90,109,110,119,118,],
    [101,10,1,0,0,0,102,97,98,99,100,119,118,117,],
    [102,10,2,0,0,0,103,96,97,98,101,118,117,116,],
    [103,10,3,0,0,0,104,95,96,97,102,117,116,115,],
    [104,10,4,0,0,0,105,94,95,96,103,116,115,114,],
    [105,10,5,0,0,0,106,93,94,95,104,115,114,113,],
    [106,10,6,0,0,0,107,92,93,94,105,114,113,112,],
    [107,10,7,0,0,0,108,91,92,93,106,113,112,111,],
    [108,10,8,0,0,0,109,90,91,92,107,112,111,110,],
    [109,10,9,0,0,0,100,99,90,91,108,111,110,119,],
    [110,11,0,0,0,0,119,100,109,108,111,128,129,120,],
    [111,11,1,0,0,0,110,109,108,107,112,127,128,129,],
    [112,11,2,0,0,0,111,108,107,106,113,126,127,128,],
    [113,11,3,0,0,0,112,107,106,105,114,125,126,127,],
    [114,11,4,0,0,0,113,106,105,104,115,124,125,126,],
    [115,11,5,0,0,0,114,105,104,103,116,123,124,125,],
    [116,11,6,0,0,0,115,104,103,102,117,122,123,124,],
    [117,11,7,0,0,0,116,103,102,101,118,121,122,123,],
    [118,11,8,0,0,0,117,102,101,100,119,120,121,122,],
    [119,11,9,0,0,0,118,101,100,109,110,129,120,121,],
    [120,12,0,0,0,0,121,118,119,110,129,130,139,138,],
    [121,12,1,0,0,0,122,117,118,119,120,139,138,137,],
    [122,12,2,0,0,0,123,116,117,118,121,138,137,136,],
    [123,12,3,0,0,0,124,115,116,117,122,137,136,135,],
    [124,12,4,0,0,0,125,114,115,116,123,136,135,134,],
    [125,12,5,0,0,0,126,113,114,115,124,135,134,133,],
    [126,12,6,0,0,0,127,112,113,114,125,134,133,132,],
    [127,12,7,0,0,0,128,111,112,113,126,133,132,131,],
    [128,12,8,0,0,0,129,110,111,112,127,132,131,130,],
    [129,12,9,0,0,0,120,119,110,111,128,131,130,139,],
    [130,13,0,0,0,0,139,120,129,128,131,148,149,140,],
    [131,13,1,0,0,0,130,129,128,127,132,147,148,149,],
    [132,13,2,0,0,0,131,128,127,126,133,146,147,148,],
    [133,13,3,0,0,0,132,127,126,125,134,145,146,147,],
    [134,13,4,0,0,0,133,126,125,124,135,144,145,146,],
    [135,13,5,0,0,0,134,125,124,123,136,143,144,145,],
    [136,13,6,0,0,0,135,124,123,122,137,142,143,144,],
    [137,13,7,0,0,0,136,123,122,121,138,141,142,143,],
    [138,13,8,0,0,0,137,122,121,120,139,140,141,142,],
    [139,13,9,0,0,0,138,121,120,129,130,149,140,141,],
    [140,14,0,0,0,0,141,138,139,130,149,150,159,158,],
    [141,14,1,0,0,0,142,137,138,139,140,159,158,157,],
    [142,14,2,0,0,0,143,136,137,138,141,158,157,156,],
    [143,14,3,0,0,0,144,135,136,137,142,157,156,155,],
    [144,14,4,0,0,0,145,134,135,136,143,156,155,154,],
    [145,14,5,0,0,0,146,133,134,135,144,155,154,153,],
    [146,14,6,0,0,0,147,132,133,134,145,154,153,152,],
    [147,14,7,0,0,0,148,131,132,133,146,153,152,151,],
    [148,14,8,0,0,0,149,130,131,132,147,152,151,150,],
    [149,14,9,0,0,0,140,139,130,131,148,151,150,159,],
    [150,15,0,0,0,0,159,140,149,148,151,168,169,160,],
    [151,15,1,0,0,0,150,149,148,147,152,167,168,169,],
    [152,15,2,0,0,0,151,148,147,146,153,166,167,168,],
    [153,15,3,0,0,0,152,147,146,145,154,165,166,167,],
    [154,15,4,0,0,0,153,146,145,144,155,164,165,166,],
    [155,15,5,0,0,0,154,145,144,143,156,163,164,165,],
    [156,15,6,0,0,0,155,144,143,142,157,162,163,164,],
    [157,15,7,0,0,0,156,143,142,141,158,161,162,163,],
    [158,15,8,0,0,0,157,142,141,140,159,160,161,162,],
    [159,15,9,0,0,0,158,141,140,149,150,169,160,161,],
    [160,16,0,0,0,0,161,158,159,150,169,170,179,178,],
    [161,16,1,0,0,0,162,157,158,159,160,179,178,177,],
    [162,16,2,0,0,0,163,156,157,158,161,178,177,176,],
    [163,16,3,0,0,0,164,155,156,157,162,177,176,175,],
    [164,16,4,0,0,0,165,154,155,156,163,176,175,174,],
    [165,16,5,0,0,0,166,153,154,155,164,175,174,173,],
    [166,16,6,0,0,0,167,152,153,154,165,174,173,172,],
    [167,16,7,0,0,0,168,151,152,153,166,173,172,171,],
    [168,16,8,0,0,0,169,150,151,152,167,172,171,170,],
    [169,16,9,0,0,0,160,159,150,151,168,171,170,179,],
    [170,17,0,0,0,0,179,160,169,168,171,188,189,180,],
    [171,17,1,0,0,0,170,169,168,167,172,187,188,189,],
    [172,17,2,0,0,0,171,168,167,166,173,186,187,188,],
    [173,17,3,0,0,0,172,167,166,165,174,185,186,187,],
    [174,17,4,0,0,0,173,166,165,164,175,184,185,186,],
    [175,17,5,0,0,0,174,165,164,163,176,183,184,185,],
    [176,17,6,0,0,0,175,164,163,162,177,182,183,184,],
    [177,17,7,0,0,0,176,163,162,161,178,181,182,183,],
    [178,17,8,0,0,0,177,162,161,160,179,180,181,182,],
    [179,17,9,0,0,0,178,161,160,169,170,189,180,181,],
    [180,18,0,0,0,0,181,178,179,170,189,190,199,198,],
    [181,18,1,0,0,0,182,177,178,179,180,199,198,197,],
    [182,18,2,0,0,0,183,176,177,178,181,198,197,196,],
    [183,18,3,0,0,0,184,175,176,177,182,197,196,195,],
    [184,18,4,0,0,0,185,174,175,176,183,196,195,194,],
    [185,18,5,0,0,0,186,173,174,175,184,195,194,193,],
    [186,18,6,0,0,0,187,172,173,174,185,194,193,192,],
    [187,18,7,0,0,0,188,171,172,173,186,193,192,191,],
    [188,18,8,0,0,0,189,170,171,172,187,192,191,190,],
    [189,18,9,0,0,0,180,179,170,171,188,191,190,199,],
    [190,19,0,0,0,0,199,180,189,188,191,8,9,0,],
    [191,19,1,0,0,0,190,189,188,187,192,7,8,9,],
    [192,19,2,0,0,0,191,188,187,186,193,6,7,8,],
    [193,19,3,0,0,0,192,187,186,185,194,5,6,7,],
    [194,19,4,0,0,0,193,186,185,184,195,4,5,6,],
    [195,19,5,0,0,0,194,185,184,183,196,3,4,5,],
    [196,19,6,0,0,0,195,184,183,182,197,2,3,4,],
    [197,19,7,0,0,0,196,183,182,181,198,1,2,3,],
    [198,19,8,0,0,0,197,182,181,180,199,0,1,2,],
    [199,19,9,0,0,0,198,181,180,189,190,9,0,1,]
    ]


M_ID   = 0    # Index = ID-1
M_IDY  = 1    # für 10 x 20 Matrix [Y][X]
M_IDX  = 2    # für 10 x 20 Matrix [Y][X]
M_R    = 3    # Werte von 0 - 319 für rot
M_G    = 4    # Werte von 0 - 319 für grün
M_B    = 5    # Werte von 0 - 319 für blau
M_A    = 6    # effektive Position des Lämpchens, leuchtet weiss wenn als "a" in «ls.set_rgb_values(a, 1, [255]*16,[255]*16,[255]*16)» als "a" eingefügt 
M_AY   = 7    # für 20 x 10 Matrix [Y][X]
M_AX   = 8    # für 20 x 10 Matrix [Y][X]

VS_A   = 0   # entspricht dem Index
VS_AY   = 1   # für 20 x 10 Matrix [Y][X]
VS_AX  = 2   # für 20 x 10 Matrix [Y][X]
VS_R   = 3   # Werte von 0 - 319 für rot
VS_G   = 4   # Werte von 0 - 319 für grün
VS_B   = 5   # Werte von 0 - 319 für blau
O      = 6   # Position oben (Verschiebung)
OR     = 7   # Position oben-rechts (Verschiebung)
R      = 8   # Position rechts (Verschiebung)
UR     = 9   # Position unten-rechts (Verschiebung)
U      = 10  # Position unten (Verschiebung)
UL     = 11  # Position unten-links (Verschiebung)
L      = 12  # Position links (Verschiebung)
OL = 13  # Position oben-links (Verschiebung)



red = [[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,
       [0]*16,[0]*16,[0]*16,[0]*16,[0]*16,
       [0]*16,[0]*16,[0]*16,[0]*16,[0]*16,
       [0]*16,[0]*16,[0]*16,[0]*16,[0]*16] #*20x10 (16)

green = [[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,
        [0]*16,[0]*16,[0]*16,[0]*16,[0]*16,
        [0]*16,[0]*16,[0]*16,[0]*16,[0]*16,
        [0]*16,[0]*16,[0]*16,[0]*16,[0]*16] #*20x10 (16)

blue = [[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,
        [0]*16,[0]*16,[0]*16,[0]*16,[0]*16,
        [0]*16,[0]*16,[0]*16,[0]*16,[0]*16,
        [0]*16,[0]*16,[0]*16,[0]*16,[0]*16] #*20x10(16)


# alle RGB-Werte auf 0 zurücksetzen
def LightOff():
     i = 0
     a = 0
     while i < 20:
         ls.set_rgb_values(a, 10, [0]*16, [0]*16, [0]*16)
         a += 10
         i += 1
         
     
# Pixelwerte in Valueset laden und RGB initalisieren
def initValueset():
     global Mapping
     global Valueset
     global red
     global green
     global blue

     i = 0
     while i < len(Mapping):
          if i+1 == Mapping[i][0]:
               indexVS = Mapping[i][M_A]
               Valueset[indexVS][VS_R] = Mapping[i][M_R]
               Valueset[indexVS][VS_G] = Mapping[i][M_G]
               Valueset[indexVS][VS_B] = Mapping[i][M_B]
               i += 1
          else:
               print("Fehler Mapping")

     initRGB(Valueset)


# ein einzelnes, statisches Bild anzeigen
def showPicture():
     i = 0
     while i < 20:
          ls.set_rgb_values(i*10, 10, blue[i], green[i], red[i])
          i += 1


def initRGB(Valueset):
     j = 0
     while j < len(Valueset):
          if j == Valueset[j][0]:
               y = Valueset[j][VS_AY]
               x = Valueset[j][VS_AX]
               red[y][x]   = Valueset[j][VS_R]
               green[y][x] = Valueset[j][VS_G]
               blue[y][x]  = Valueset[j][VS_B]
               j += 1
          else:
               print("Fehler Valueset")


# Richtung: O, OR, R, UR, U, UL, L, OL (oben, rechts, links, unten)
def movePicture(direction):
     global Valueset
     global cycle
     global frameIndex

     # Valueset kopieren
     newValueset = []
     i = 0
     while i < len(Valueset):
          newValueset.append(Valueset[i].copy())
          i += 1

     # Pixelwerte verschieben in newValueset und RGB-Arrays
     i = 0
     while i < len(Valueset):
          if i == Valueset[i][0]:
               newIndex = Valueset[i][direction]
               newValueset[newIndex][VS_R] = Valueset[i][VS_R]
               newValueset[newIndex][VS_G] = Valueset[i][VS_G]
               newValueset[newIndex][VS_B] = Valueset[i][VS_B]
              # y = Valueset[newIndex][VS_AY]
              # x = Valueset[newIndex][VS_AX]
              # red[y][x]   = Valueset[i][VS_R]
              # green[y][x] = Valueset[i][VS_G]
              # blue[y][x]  = Valueset[i][VS_B]
              # print(newValueset[newIndex])
               i += 1
          else:
               print("Fehler Valueset")


     Valueset = newValueset
     initRGB(Valueset)


  

# einzelner Pixel ändern: id-Nummer, r-Wert, g-Wert, b-Wert (jeweils von 0-319)
def changeSinglePixel(idNr, r, g, b):
     global Mapping
     global Valueset

     if idNr >= 1 & idNr <= 200:
        if idNr == Mapping[idNr-1][0]:
             indexVS = Mapping[idNr-1][M_A]            
             Valueset[indexVS][VS_R] = r
             Valueset[indexVS][VS_G] = g
             Valueset[indexVS][VS_B] = b
        else:
            print("Mappingfehler: idNr und allPixel-Array")
     else:
         print("ungültige idNr, Wähle eine Nummer von 1 bis 200")
         


initValueset()
changeSinglePixel(177, 255, 0, 0)
changeSinglePixel(176, 255, 0, 0)
changeSinglePixel(168, 255, 0, 0)
changeSinglePixel(167, 255, 0, 0)
changeSinglePixel(166, 255, 0, 0)
changeSinglePixel(165, 255, 0, 0)
changeSinglePixel(157, 255, 0, 0)
changeSinglePixel(156, 255, 0, 0)
changeSinglePixel(155, 255, 0, 0)
changeSinglePixel(154, 255, 0, 0)
changeSinglePixel(148, 255, 0, 0)
changeSinglePixel(147, 255, 0, 0)
changeSinglePixel(146, 255, 0, 0)
changeSinglePixel(145, 255, 0, 0)
changeSinglePixel(104, 255, 0, 255)
changeSinglePixel(95, 255, 0, 255)
changeSinglePixel(94, 255, 0, 255)
changeSinglePixel(93, 255, 0, 255)
changeSinglePixel(84, 255, 0, 255)
changeSinglePixel(83, 255, 0, 255)
changeSinglePixel(82, 255, 0, 255)
changeSinglePixel(75, 255, 0, 255)
changeSinglePixel(74, 255, 0, 255)
changeSinglePixel(73, 255, 0, 255)
changeSinglePixel(64, 255, 0, 255)
initRGB(Valueset)
#print(Mapping[2-1])
#print(Valueset[2-1])
movePicture(L)
#print(Valueset[18])


#=====================================================================

HOST = "localhost"
PORT = 4223
UID = "wVj" # UID of your LED Strip Bricklet

cycle = 0 # Anzahl Durchläufe
frameIndex = 0 # 0-19 (20 Frames = 1 Durchlauf)

# Use frame rendered callback to move the active LED every frame
def cb_frame_rendered(length, ls):

     showPicture()

     #movePicture()

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
    ls.set_frame_duration(500)

    # Register frame rendered callback to function cb_frame_rendered
    ls.register_callback(ls.CALLBACK_FRAME_RENDERED,
                         lambda x: cb_frame_rendered(x, ls))

    # Set initial rgb values to get started
 #   ls.set_rgb_values(0, 0, r, g, b)

    input("Press key to exit\n") # Use input() in Python 3
    ipcon.disconnect()
