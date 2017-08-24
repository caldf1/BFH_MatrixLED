from LEDmatrix_2308_init import *
import matrixProperties
import imageProperties
import threading
import time

"""
Threading: The run() method will be started and it will run in the background until the application exits.

"""
class MoveableLEDMatrix(object):


    def __init__(self, interval=1, myImage=imageProperties.forms1, imageFormat='normal'):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval

        self.__matrix = LEDmatrix()
        self.__inputImage = myImage
        self.__matrixImage = [[0 for i in range(matrixProperties.ROWS)] for i in range(matrixProperties.COLUMNS)]
 #       self.__matrix.finish()
        

        # für das matrixImage
        self.__numberOfColumns = matrixProperties.COLUMNS                           # hier 20 Spalten
        self.__numberOfRows = matrixProperties.ROWS                                 # hier 10 Zeilen
        self.__startColumn = 0                                                      # Start-Spalte
        self.__startRow = 0                                                         # Start-Zeile

        # Bewegung merken
        self.__move = 'false'                                                       # 'false' oder 'true'
        self.__moveHorizontal = 'false'                                             # 'right' oder 'left' oder 'false'
        self.__moveVertical = 'false'                                               # 'up' oder 'down' oder 'false'

        # zum ablesen des inputImage
#        self.__cycleX = 0                                                           # für die Bewegung nach links und rechts
#        self.__cycleY = 0                                                           # für die Bewegung nach oben und unten
        self.__startX = 0 
        self.__startY = 0
        self.__format = imageFormat # 'normal', 'column', 'row'


        # Thread erstellen und starten, läuft dann im Hintergrund
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution




    """
    Bild bewegen
    """            
    def __loadImage__(self): # Werte für StartColumn und numberOfColumn jeweils von 1 bis 20.

        # Ausgangswerte setzen (x, y) in Abhängigkeit einer Bildbewegung
        xMove = 0
        yMove = 0
        if self.__move != 'false': # y = (x + 1) %(maxX + 1)
            # links-rechts-Bewegung
            if self.__moveHorizontal != 'false':
                if self.__moveHorizontal == 'right':
                    xMove = (self.__startX + 1) % len(self.__inputImage)

                if self.__moveHorizontal == 'left':
                    xMove = (self.__startX - 1) % len(self.__inputImage)

                self.__startX = xMove

                        
            # oben-unten-Bewegung
            if self.__moveVertical != 'false':
                if self.__moveVertical == 'up':
                    yMove = (self.__startY + 1) % len(self.__inputImage[xMove])

                if self.__moveVertical == 'down':
                    yMove = (self.__startY - 1) % len(self.__inputImage[xMove])

                self.__startY = yMove


        # Keine Bewegung
        else: 
            xMove = self.__startX
            yMove = self.__startY


        x = 0
        while x < len(self.__matrixImage):
            y = 0
            while y < len(self.__matrixImage[x]):
                self.__matrixImage[x][y] = self.__inputImage[xMove][yMove]
                y += 1
                yMove = (yMove + 1) % len(self.__inputImage[xMove])
            x += 1
            xMove = (xMove + 1) % len(self.__inputImage)






    def run(self):
        """ Method that runs forever """
        while True:
            time.sleep(self.interval)

            # Bild ändern und an Matrix "senden"
            self.__loadImage__()
            self.__matrix.setImage(self.__matrixImage)



#======= public Methoden ==================================================
# startMove(), waiting(), stopMovingHorizontal(), stopMovingVertical(), stopMove(),
# moveRight(), moveLeft(), moveUp(), moveDown(), reset()


    """ Bewegungen starten, unterbrechen, stoppen. Bewegungsrichtung einstellen (rechts, links, oben, unten)"""

    def startMove(self):
        self.__move = 'true'

    def waiting(self):
        self.__move = 'false'
                
    def stopMove(self):
        self.__move = 'false'
        self.__moveHorizontal = 'false'
        self.__moveVertical = 'false'
        self.__startX = 0
        self.__startY = 0



    def moveRight(self): 
        self.startMove()
        self.__moveHorizontal = 'right'

    def moveLeft(self): 
        self.startMove()
        self.__moveHorizontal = 'left'

    def stopMovingHorziontal(self):
        self.__moveHorizontal = 'false'

        

    def moveUp(self): 
        self.startMove()
        self.__moveVertical = 'up'

    def moveDown(self): 
        self.startMove()
        self.__moveVertical = 'down'

    def stopMovingVertical(self):
        self.__moveVertical = 'false'



    # nur zu Testzwecke
    def getMove(self):
        string = 'Bewegung:', self.__move, "\nlinks/rechts: ", self.__moveHorizontal, "\nauf/ab: ", self.__moveVertical 
        return string



    def reset(self):
        self.__numberOfColumns = matrixProperties.COLUMNS
        self.__numberOfRows = matrixProperties.ROWS
        self.__startColumn = 0
        self.__startRow = 0
        self.stopMove()



# setNumberOfColumns(), getNumberOfColumns(), setNumberOfRows, getNumberOfRows(), setStartColumnAndRow()


    """ Anzahl Spalten (x): hier von 1 bis 20 """

    def setNumberOfColumns(self, columns):
        self.__numberOfColumns = columns

    def getNumberOfColumns(self):
        return self.__numberOfColumns



    """ Anzahl Zeilen (y): hier von 1 bis 10 """

    def setNumberOfRows(self, rows):
        self.__numberOfRows = rows

    def getNumberOfRows(self):
        return self.__numberOfRows



    """ Startwert x, y ändern (Column, Row) """
    def setStartColumnAndRow(self, startColumn, startRow):
        self.__startColumn = startColumn - 1
        self.__startRow = startRow -1
    


