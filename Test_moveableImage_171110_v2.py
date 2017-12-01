from LEDmatrix_init_171110 import *
from LEDmatrix_moveableImage_171110 import *
import imageProperties
import time
import threading


# noinspection PyRedundantParentheses
class TestThread:
    """ Klasse für die automatische Bildübermittlung. """
    
    def __init__(self, matrixObject: LEDmatrixConnect, imageObject: MoveableImage):
        self.matrix = matrixObject
        self.image = imageObject
        self.xValues = self.image.getXvalues()
        self.yValues = self.image.getYvalues()

        # Thread
        self.stopped = False
        self.sleepTime = 0.01

        self.threadTest = threading.Thread(target=self.__run__, args=())
        self.threadTest.daemon = True
        self.threadTest.start()

    def __run__(self):
        """ Thread, welcher die Bildteile zusammenfügt und an die LEDmatrix_init weiterleitet. """
        while True:
            if (self.stopped is True):
                print("Test-Thread stopped\n")
                break

            mergeImage = self.image.getImage()
            matrixImage = [[[0, 0, 0] for i in range(10)] for i in range(20)]

            xVal = self.xValues
            yVal = self.yValues

            x = 0
            y = 0
            while x < xVal[1]:
                while y < yVal[1]:
                    matrixImage[xVal[0] + x][yVal[0] + y] = mergeImage[x][y]
                    y += 1
                x += 1
                y = 0

            self.matrix.setImage(matrixImage)
            time.sleep(self.sleepTime)


class Merge:
    """ Klasse um die Bildübermittlung manuell aufzurufen. """
    
    def __init__(self, matrixObject: LEDmatrixConnect, imageObject: MoveableImage):
        self.matrix = matrixObject
        self.image = imageObject
        self.xValues = self.image.getXvalues()
        self.yValues = self.image.getYvalues()

        
    def run(self, image: list):
        """ Bildübergabe an LEDmatrixConnect-Objekt. """
        mergeImage = image
        matrixImage = [[[0, 0, 0] for i in range(10)] for i in range(20)]

        xVal = self.xValues
        yVal = self.yValues

        x = 0
        y = 0
        while x < xVal[1]:
            while y < yVal[1]:
                matrixImage[xVal[0] + x][yVal[0] + y] = mergeImage[x][y]
                y += 1
            x += 1
            y = 0

        self.matrix.setImage(matrixImage)
        time.sleep(1.5)       




if __name__ == "__main__":
    # LED-Display-Verbindung und Bildinstanz erstellen
    matrix = LEDmatrixConnect()
    # Erwartung: ein 10x mal 6y grosses Bild in der Mitte des Displays
    image = MoveableImage('test', imageProperties.forms1, [0, 20], [0, 10])

    # Um die Bilder zu übermitteln
    send = Merge(matrix, image)

    # Abfragen
    print('\ngetName: ' + image.getName())                                                  # 39
    print('\ngetMatrixPosition (Expected: [[0, 20][0, 10]]): ', image.getMatrixPosition())  # 9
    print('\ngetXvalues (Expected: [0, 20]): ', image.getXvalues())                         # 10
    print('\ngetYvalues (Expected: [0, 10]): ', image.getYvalues())                         # 11
    print('\ngetImageSizeAsText: ' + image.getImageSizeAsText())                            # 19
    print('\ngetImageSize: ', image.getImageSize())                                         # 20
    print('\ngetMoveInfo (1): \n', image.getMoveInfo())                                     # 33

        
    print('\nBild-Tests: Image ändern, "Licht aus"-Image ändern')
    send.run(image.getImage())                                          # 12
    time.sleep(2)
    send.run(image.getLightOffImage())                                  # 13
    image.setLightOffImageColor(0, 255, 0)                              # 15
    time.sleep(2)
    send.run(image.getLightOffImage())                                  # 13
    image.setLightOffImage(imageProperties.legoface)                    # 14
    time.sleep(2)
    send.run(image.getLightOffImage())                                  # 13
    image.resetLightOffImage()                                          # 16
    time.sleep(2)
    send.run(image.getLightOffImage())                                  # 13
    image.setInputImage(imageProperties.hearts1, 'landscape')           # 18
    time.sleep(2)
    send.run(image.getImage())                                          # 12
    time.sleep(1)

    # Thread starten, um die Bildbewegungen zu testen
    TestThread(matrix, image)

    print("\nBild: Blink- und Move-tests")
    image.startBlink()                                              # 21 blinken
    time.sleep(2)
    image.setRate(4)                                                # 35 4x/Sekunde blinken
    image.setTimingRatio(3, 1)                                      # 37 im Verhältnis 3:1
    print('\ngetMoveInfo (2): \n', image.getMoveInfo())             # 33
    image.setHeartrateFlag()                                        # 38 Heartrate: True
    print('\ngetMoveInfo (3): \n', image.getMoveInfo())             # 33
    image.setPuls(120)                                              # 36 Puls: 120
    print('\ngetMoveInfo (4): \n', image.getMoveInfo())             # 33
    image.setHeartrateFlag(False)                                   # 38 Heartrate: False
    print('\ngetMoveInfo (5): \n', image.getMoveInfo())             # 33
    image.stopBlink()                                               # 22 blinken stoppen
    time.sleep(2)

    print("\nimageFormat-Tests")
    image.setImageFormat()                                          # 17 Bildformat 'default'
    image.moveRight()                                               # 27 nach rechts
    time.sleep(5)
    image.setMoveTime(0.1)                                          # 34 schneller
    time.sleep(2)
    image.setMoveTime(0.5)                                          # 34 langsamer
    time.sleep(2)
    image.setMoveTime(0.1)                                          # 34 schneller
    time.sleep(2)
    image.moveLeft()                                                # 28 nach links
    print('\ngetMoveInfo (6): \n', image.getMoveInfo())             # 33
    time.sleep(2)
    image.setImageFormat('portrait')                                # 17 Bildformat: hoch (stop)
    time.sleep(2)
    image.setImageFormat('landscape')                               # 17 Bildformat: quer
    time.sleep(2)
    image.setImageFormat('default')                                 # 17 Bildformat: default
    time.sleep(2)
    image.stopMoveHorizontal()                                      # 29 links/rechts stoppen
    print('\ngetMoveInfo (7): \n', image.getMoveInfo())             # 33
    time.sleep(2)
    image.moveUp()                                                  # 30 nach oben
    time.sleep(2)
    image.moveDown()                                                # 31 nach unten
    time.sleep(2)
    image.setImageFormat('landscape')                               # 17 Bildformat: quer (stop)
    time.sleep(2)
    image.setImageFormat('portrait')                                # 17 Bildformat: hoch
    time.sleep(2)
    image.setImageFormat('default')                                 # 17 Bildformat: default
    time.sleep(2)
    image.stopMoveVertical()                                        # 32 oben/unten stoppen
    time.sleep(2)

    print("\nstop and go")
    image.moveRight()                                               # 27 nach rechts
    image.moveUp()                                                  # 30 nach oben
    time.sleep(3)
    image.waiting()                                                 # 24 warten
    time.sleep(2)
    image.startMove()                                               # 23 Bewergung starten
    time.sleep(2)
    image.stopMove()                                                # 25 Bewegung stoppen
    time.sleep(2)
    image.startMove()                                               # 23 "no effect"
    print('\ngetMoveInfo (8): \n', image.getMoveInfo())             # 33
    time.sleep(2)
    image.resetMove()                                               # 26 Bildposition zurück
    time.sleep(2)

    print("\nmove in alle Richtungen")
    image.moveRight()                                               # 27 rechts
    time.sleep(1)
    image.moveDown()                                                # 31 unten (rechts + unten)
    time.sleep(1)
    image.moveLeft()                                                # 28 links (links + unten)
    time.sleep(1)
    image.moveUp()                                                  # 30 oben (links + oben)
    time.sleep(1)
    image.resetMove()                                               # 26 Bildposition zurück
    time.sleep(2)

    print("Light on / off")
    image.startBlink()                                              # 21 blinken
    time.sleep(2)
    image.light(False)                                              # 40 Licht aus
    time.sleep(2)
    image.light()                                                   # 40 Licht ein
    time.sleep(2)

    # Alle Threads beenden, Verbindungsabbau
    TestThread.stopped = True
    image.finish()                                                  # 8
    matrix.light(False)                                             # 43
    time.sleep(3)
    matrix.finish()                                                 # 2
