from LEDmatrix_2308_init import *
import matrixProperties
import imageProperties
import threading
import time

"""
Threading: The run() method will be started and it will run in the background until the application exits.

"""
class MoveableLEDmatrix(object):


    def __init__(self, interval=0.1, myImage=imageProperties.forms1, imageFormat='normal'):
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
        self.__lightOff = 'false'                                                   # 'false' or 'true'
        
        # zum ablesen des inputImage
#        self.__cycleX = 0                                                           # für die Bewegung nach links und rechts
#        self.__cycleY = 0                                                           # für die Bewegung nach oben und unten
        self.__startX = 0 
        self.__startY = 0
        self.__format = imageFormat                                                 # 'normal', 'column', 'row'


        # Thread erstellen und starten, läuft dann im Hintergrund
        self.__stopped = 'false'
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
            if (self.__moveHorizontal != 'false' and self.__format != 'column'):
                if self.__moveHorizontal == 'right':
                    xMove = (self.__startX + 1) % len(self.__inputImage)

                if self.__moveHorizontal == 'left':
                    xMove = (self.__startX - 1) % len(self.__inputImage)

                self.__startX = xMove

                        
            # oben-unten-Bewegung
            if self.__moveVertical != 'false' and self.__format != 'row':
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

        self.__matrix.setImage(self.__matrixImage)

     




    def run(self):
        """ Method that runs forever """
        while True:            
            # print("thread runs") # zum testen
            if self.__stopped== 'true':
                print("Thread stopped")
                break

            # Bild ändern und an Matrix "senden"
            if self.__lightOff is 'false':
                
                self.__loadImage__()
#                self.__matrix.setImage(self.__matrixImage)
                time.sleep(self.interval - 0.2) # Variante 1 (Variante 2 -> time.sleep(0.2)

#                self.__matrix.setImage([[[0 for i in range (3)] for i in range(matrixProperties.ROWS)] for i in range(matrixProperties.COLUMNS)]) 
#                time.sleep(0.2) # Variante 1 (Variante 2 -> time.sleep(self.interval - 0.2)

            else:
                self.__matrix.setImage([[[0 for i in range (3)] for i in range(matrixProperties.ROWS)] for i in range(matrixProperties.COLUMNS)])   




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

    def setFormat(self, imageFormat):
        self.__format = imageFormat

    def getFormat(self):
        return self.__format


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
    

# connect(), finish(), setVelocity(), lightOff()

    def connect(self):
        self.__matrix.connect()

    def finish(self):
        self.__matrix.finish()
        input("\nPress key to finish Thread\n")
        self.__stopped = 'true'
        


    def setVelocity(self, frequenz):
        self.__matrix.setVelocity(self, frequenz)

            
    def lightOff(self):
        self.__lightOff = 'true'

    def lightOn(self):
        self.__lightOff = 'false'


