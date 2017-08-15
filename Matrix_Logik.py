from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_led_strip import BrickletLEDStrip

allPixelDefault = [
     [1,9,19,0,0,0,0,0,0,1,0,1,198,19,8,199,19,9,190,19,0,9,0,9,10,1,0,19,1,9,18,1,8],
     [2,8,19,0,0,0,1,0,1,2,0,2,197,19,7,198,19,8,199,19,9,0,0,0,19,1,9,18,1,8,17,1,7],
     [3,7,19,0,0,0,2,0,2,3,0,3,196,19,6,197,19,7,198,19,8,1,0,1,18,1,8,17,1,7,16,1,6],
     [4,6,19,0,0,0,3,0,3,4,0,4,195,19,5,196,19,6,197,19,7,2,0,2,17,1,7,16,1,6,15,1,5],
     [5,5,19,0,0,0,4,0,4,5,0,5,194,19,4,195,19,5,196,19,6,3,0,3,16,1,6,15,1,5,14,1,4],
     [6,4,19,0,0,0,5,0,5,6,0,6,193,19,3,194,19,4,195,19,5,4,0,4,15,1,5,14,1,4,13,1,3],
     [7,3,19,0,0,0,6,0,6,7,0,7,192,19,2,193,19,3,194,19,4,5,0,5,14,1,4,13,1,3,12,1,2],
     [8,2,19,0,0,0,7,0,7,8,0,8,191,19,1,192,19,2,193,19,3,6,0,6,13,1,3,12,1,2,11,1,1],
     [9,1,19,0,0,0,8,0,8,9,0,9,190,19,0,191,19,1,192,19,2,7,0,7,12,1,2,11,1,1,10,1,0],
     [10,0,19,0,0,0,9,0,9,0,0,0,199,19,9,190,19,0,191,19,1,8,0,8,11,1,1,10,1,0,19,1,9],
     ]

allPixel = []

# Default-Werte in allPixel kopieren
def copyDefaultWerte():
     i = 0
     while i < len(allPixelDefault):
          allPixel.append(allPixelDefault[i].copy())
          i += 1

copyDefaultWerte()
#print(allPixel)


ID   = 0    # Index = ID-1
ID_Y = 1    # für 10 x 20 Matrix [Y][X]
ID_X = 2    # für 10 x 20 Matrix [Y][X]
R    = 3    # Werte von 0 - 319 für rot
G    = 4    # Werte von 0 - 319 für grün
B    = 5    # Werte von 0 - 319 für blau
A    = 6    # effektive Position des Lämpchens, leuchtet weiss wenn als "a" in «ls.set_rgb_values(a, 1, [255]*16,[255]*16,[255]*16)» als "a" eingefügt 
A_Y  = 7    # für 20 x 10 Matrix [Y][X]
A_X  = 8    # für 20 x 10 Matrix [Y][X]
D_O  = 9    # Position oben (Verschiebung)
O_Y  = 10   # oben in 20 x 10 Matrix [Y][X]
O_X  = 11   # oben in 20 x 10 Matrix [Y][X]
D_OR  = 12  # Position oben-rechts (Verschiebung)
OR_Y  = 13  # oben-rechts in 20 x 10 Matrix [Y][X]
OR_X  = 14  # oben-rechts in 20 x 10 Matrix [Y][X]
D_R  = 15   # Position rechts (Verschiebung)
R_Y  = 16   # rechts in 20 x 10 Matrix [Y][X]
R_X  = 17   # rechts in 20 x 10 Matrix [Y][X]
D_UR  = 18  # Position unten-rechts (Verschiebung)
UR_Y  = 19  # unten-rechts in 20 x 10 Matrix [Y][X]
UR_X  = 20  # unten-rechts in 20 x 10 Matrix [Y][X]
D_U  = 21   # Position unten (Verschiebung)
U_Y  = 22   # unten in 20 x 10 Matrix [Y][X]
U_X  = 23   # unten in 20 x 10 Matrix [Y][X]
D_UL  = 24  # Position unten-links (Verschiebung)
UL_Y  = 25  # unten-links in 20 x 10 Matrix [Y][X]
UL_X  = 26  # unten-links in 20 x 10 Matrix [Y][X]
D_L  = 27   # Position links (Verschiebung)
L_Y  = 28   # links in 20 x 10 Matrix [Y][X]
L_X  = 29   # links in 20 x 10 Matrix [Y][X]
D_OL  = 30  # Position oben-links (Verschiebung)
OL_y  = 31  # oben-links in 20 x 10 Matrix [Y][X]
OL_X  = 32  # oben-links in 20 x 10 Matrix [Y][X]

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
         
     
# Pixelwerte in die Arrays von red, green, blue laden
def loadMatrix():
     global allPixel
     global red
     global green
     global blue

     i = 0
     while i < len(allPixel):
          if i+1 == allPixel[i][0]:
               red[A_Y][A_X] = allPixel[i][R]
               green[A_Y][A_X] = allPixel[i][G]
               blue[A_Y][A_X] = allPixel[i][B]
               i += 1
          else:
               print("Fehler")

def showPicture():
     i = 0
     while i < 20:
          ls.set_rgb_values(i*10, 10, blue[i], green[i], red[i])
          i += 1

cycle = 0 # Anzahl Durchläufe
frameIndex = 0 # 0-19 (20 Frames = 1 Durchlauf)

def movePicture(direction):
     global allPixel
     firstPixel = [allPixel[0][R], allPixel[0][G], allPixel[0][B]]
     p1 = allPixel[0]
     p2 = allPixel[allPixel[][]]
     i = 2
     while i <= 199
          changeSinglePixel(i-1, allPixel[i][R])
               red[L_Y][L_X] = allPixel[i][R]
               green[L_Y][L_X] = allPixel[i][G]
               blue[L_Y][L_X] = allPixel[i][B]

     changeSinglePixel(200, firstPixel[0], firstPixel[1], firstPixel[2])
     

     loadMatrix()

# einzelner Pixel ändern: id-Nummer, r-Wert, g-Wert, b-Wert (jeweils von 0-319)
def changeSinglePixel(idNr, r, g, b):
     global allPixel

     if idNr >= 1 & idNr <= 10:
        if idNr == allPixel[idNr-1][0]:
            allPixel[idNr-1][R] = r
            allPixel[idNr-1][G] = g
            allPixel[idNr-1][B] = b

        else:
            print("Mappingfehler: idNr und allPixel-Array")

     else:
         print("ungültige idNr, Wähle eine Nummer von 1 bis 10")
         



loadMatrix()
changeSinglePixel(2, 255, 244, 233)
print(allPixel[2-1])
print(allPixelDefault[2-1])
