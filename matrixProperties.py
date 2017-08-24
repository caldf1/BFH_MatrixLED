""" Eigenschaften der LED-Matrix """

HOST = "localhost"
PORT = 4223
UID = "wVj" # Change XYZ to the UID of your LED Strip Bricklet

ROWS = 10
COLUMNS = 20
NUM_LEDS = 16

START_LED = [COLUMNS - 1, 0] # {19x, 0y} im Koordinatensytem
LED_MAX = ROWS * COLUMNS - 1
MATRIX_DEFAULT = [[0 for i in range(ROWS)] for i in range(COLUMNS)] # [[0 for i in range(10)] for i in range(20)]

IndexRed = 0
IndexGreen = 1
IndexBlue = 2

def colorRow():
    return [0 for i in range(NUM_LEDS)] # [0 for i in range(16)]

def colorRowsRGB():
    return [[0 for i in range(NUM_LEDS)] for i in range (3)] # [[0 for i in range(16)] for i in range(3)]


def LEDnr():
    value = 0         
    array = MATRIX_DEFAULT # [[0 for i in range(10)] for i in range(20)]

    x = START_LED[0]        # 19 
    y = START_LED[1]        # 0
    while x > -1:
        if x %2 == 1:       # von y0 nach yMax (=ROWS-1)
            y = 0
            while y < ROWS:
                array[x][y] = value
                y += 1
                value += 1
        else:               # von yMax (=ROWS-1) nach y0
            y = ROWS-1
            while y > -1:
                array[x][y] = value
                y -= 1
                value += 1
        x -= 1

    return array


LEDnr = LEDnr()


def getLEDnr(xMatrix, yMatrix):
    return LEDnr[xMatrix][yMatrix]
  

def printLEDnr():
    for x in LEDnr:
        print(x)

#printLEDnr()



