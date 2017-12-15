from LEDmatrix_init_171110 import *
from LEDmatrix_moveableImage_171110 import *
import imageProperties
import matrixProperties
import threading
import time


# noinspection PyRedundantParentheses,PyUnresolvedReferences
class LEDmatrix:
    """ Mögliche Argumente (arg): 'single'(=default-Wert), 'square', 'colorHeartrate', 'quarters4', 'row2', 'col2' """

    #  @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/LEDmatrix[POST])
    def __init__(self, usecase: 'single' 'square' 'colorHeartrate' 'quarters4' 'row2' 'col2' = 'single'):

        self.__ledMatrix = LEDmatrixConnect()  # Matrix: 20x 10y
        self.__bgRed = 0
        self.__bgGreen = 0
        self.__bgBlue = 0

        self.__case = usecase
        self.__objectlist = []  # list(MoveableImage)
        self.__stopped = False
        self._sleepTime = 0.01

        if (self.__case == 'square'):
            # Eine quadratische Bildinstanz in der Mitte.
            squareImage = MoveableImage('square', [[[255, 255, 255] for i in range(10)] for i in range(10)], [5, 10],
                                        [0, 10])
            self.__objectlist.append(squareImage)

        if (self.__case == 'colorHeartrate'):
            # Es werden 5 bewegbare Bildinstanzen erstellt.
            # (oben = "Puls", unten-links = gelb, unten-2.v.links = blau, unten-3.v.Links = weiss, unten-4.v.Links = ).

            # Default-Bilder importieren
            text = imageProperties.pulstext
            heart1 = imageProperties.heartblue
            heart2 = imageProperties.heartred
            heart3 = imageProperties.heartgreen
            heart4 = imageProperties.heartyellow

            # Matrix splitten
            topImage = MoveableImage("topImage", text, [0, 20], [0, 5])
            bottomLeftImage = MoveableImage("bottomLeftImage", heart1, [0, 5], [5, 5])
            bottom2ndLeftImage = MoveableImage("bottom2ndLeftImage", heart2, [5, 5], [5, 5])
            bottom3rdLeftImage = MoveableImage("bottom3rdLeftImage", heart3, [10, 5], [5, 5])
            bottom4thLeftImage = MoveableImage("bottom4thLeftImage", heart4, [15, 5], [5, 5])
            self.__objectlist.extend(
                (topImage, bottomLeftImage, bottom2ndLeftImage, bottom3rdLeftImage, bottom4thLeftImage))

            # Definieren, dass der Puls dargestellt werden soll.
            bottomLeftImage.setHeartrateFlag(True)
            bottom2ndLeftImage.setHeartrateFlag(True)
            bottom3rdLeftImage.setHeartrateFlag(True)
            bottom4thLeftImage.setHeartrateFlag(True)

        if (self.__case == 'quarters4'):
            # Es werden 4 bewegbare Bildinstanzen erstellt.
            # (oben-links = rot, oben-rechts = gelb, unten-links = blau, unten-rechts = weiss).
            topLeftImage = MoveableImage("topLeftImage", [[[255, 0, 0] for i in range(5)] for i in range(10)], [0, 10],
                                         [0, 5])
            topRightImage = MoveableImage("topRightImage", [[[255, 255, 0] for i in range(5)] for i in range(10)],
                                          [10, 10], [0, 5])
            bottomLeftImage = MoveableImage("bottomLeftImage", [[[0, 0, 255] for i in range(5)] for i in range(10)],
                                            [0, 10], [5, 5])
            bottomRightImage = MoveableImage("bottomRightImage",
                                             [[[255, 255, 255] for i in range(5)] for i in range(10)], [10, 10], [5, 5])
            self.__objectlist.extend((topLeftImage, topRightImage, bottomLeftImage, bottomRightImage))

        if (self.__case == 'row2'):
            # Es werden 2 bewegbare Bildinstanzen erstellt.
            # (obere und untere Bildinstanz). Farbe oben = rot, Farbe unten = blau.
            topImage = MoveableImage("topImage", [[[255, 0, 0] for i in range(5)] for i in range(20)], [0, 20], [0, 5])
            bottomImage = MoveableImage("bottomImage", [[[0, 0, 255] for i in range(5)] for i in range(20)], [0, 20],
                                        [5, 5])
            self.__objectlist.extend((topImage, bottomImage))

        if (self.__case == 'col2'):
            # Es werden 2 bewegbare Bildinstanzen erstellt.
            # (linke und rechte Bildinstanz). Farbe links = rot, Farbe rechts = blau.
            leftImage = MoveableImage("leftImage", [[[255, 0, 0] for i in range(10)] for i in range(10)], [0, 10],
                                      [0, 10])
            rightImage = MoveableImage("rightImage", [[[0, 0, 255] for i in range(10)] for i in range(10)], [10, 10],
                                       [0, 10])
            self.__objectlist.extend((leftImage, rightImage))

        if (self.__case == 'single'):
            # Die Matrix wird nicht geteilt, es wird nur 1 bewegbare Bildinstanz erstellt.
            singleImage = MoveableImage("singleImage")
            self.__objectlist.append(singleImage)

        """ Thread für das Mergen der Bildteile. """
        self.__threadMerge = threading.Thread(target=self.__runMerge__, args=())
        self.__threadMerge.daemon = True
        self.__threadMerge.start()

    def __runMerge__(self):
        """ Thread, welcher die Bildteile zusammenfügt und an die LEDmatrix_init weiterleitet. """
        while True:
            if (self.__stopped is True):
                print("Merge-Thread stopped\n")
                break

            mergeImage = []
            # image = [[[self.__bgRed, self.__bgGreen, self.__bgBlue] for i in range(10)] for i in range(20)]
            image = [[[self.__bgRed, self.__bgGreen, self.__bgBlue] for i in range(mergeProperties.ROWS)] for i in
                     range(mergeProperties.COLUMNS)]

            # alle aktuellen Bilder der Bildinstanzen "abholen"
            j = 0
            while j < len(self.__objectlist):
                mergeImage.append(self.__objectlist[j].getImage())
                j += 1

            # einzelne Bildteile zu einem Gesamtbild (20x/10y) zusammenfügen
            i = 0
            while i < len(self.__objectlist):
                xValues = self.__objectlist[i].getXvalues()
                yValues = self.__objectlist[i].getYvalues()

                x = 0
                y = 0
                while x < xValues[1]:
                    while y < yValues[1]:
                        image[xValues[0] + x][yValues[0] + y] = mergeImage[i][x][y]
                        y += 1
                    x += 1
                    y = 0
                i += 1

            self.__ledMatrix.setImage(image)  # Gesamtbild an LEDmatrixConnect-Instanz
            time.sleep(self._sleepTime)

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/LEDmatrix/setBGcolor/<int:red>/<int:green>/<int:blue>[PUT])
    def setBGcolor(self, red: int, green: int, blue: int):
        """ Definiert die Hintergrundfarbe, wo kein Bild ist.
            Wertebereich von 0 bis 255.
            :param red: int
            :param green: int
            :param blue: int
        """
        self.__bgRed = red
        self.__bgGreen = green
        self.__bgBlue = blue

    #  @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/LEDmatrix/getObjects[GET])
    def getObjects(self) -> list:
        """ Gibt eine Liste mit den Bildobjekten (MoveableImage) zurück.
            :return: objectList: list
        """
        return self.__objectlist

    #  @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/LEDmatrix/getMatrix[GET])
    def getMatrix(self) -> LEDmatrixConnect:
        """ Gibt das Matrix-Objekt (LEDmatrixConnect) zurück.
            :return: ledMatrix: LEDmatrixConnect
        """
        return self.__ledMatrix

    #  @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/LEDmatrix/getCase[GET])
    def getCase(self) -> str:
        """ Gibt den Namen des Use-Cases zurück.
            :return: case: str
        """
        return self.__case

    #  @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/LEDmatrix/finish[PUT])
    def finish(self):
        """ Programm beenden.
            Beendet alle Threads und die Verbindung zum LED-Display.
        """
        objectlist = self.__objectlist

        input("\nPress key to finish Thread\n")
        self.__stopped = True

        i = 0
        while i < len(objectlist):
            objectlist[i].finish()
            i += 1

        time.sleep(2)
        input("\nPress key to exit\n")
        self.__ledMatrix.finish()
