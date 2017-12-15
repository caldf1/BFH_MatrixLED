import imageProperties
import threading
import time


# noinspection PyDefaultArgument,PyPep8Naming,PyRedundantParentheses,PyUnresolvedReferences
class MoveableImage(object):
    """ für Bildinstanzen
        Mit der Bild-Instanz werden zwei separate Threads erstellt:
        - "moveImage": in welchem das Bild verändert wird
        - "blink": in welchem das Licht ein- und ausgeschalten wird, gemäss einer bestimmten Frequenz
    """
    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/<str:name>/<list:myImage>/<list:matrix_xValues>/<list:matrix_yValues>[POST])
    def __init__(self, name: str, myImage: list = imageProperties.forms1, matrix_xValues: list = [0, 20],
                 matrix_yValues: list = [0, 10]):
        """ Matrix x- und y-Werte = [Startwert, Anzahl Spalten bzw. Zeilen], Startwert von 0 aus gezählt.
            Ranges Blinkenlights-Display: 20x auf 10y (0-19x von links nach rechts / 0-9y von oben nach unten)
        """

        self.__objectName = name

        self.__matrix_xValues = matrix_xValues
        self.__matrix_yValues = matrix_yValues

        self.__inputImage = myImage
        self.__outputImage = [[[] for i in range(self.__matrix_yValues[1])] for i in range(self.__matrix_xValues[1])]
        self.__lightOffImage = [[[0 for i in range(3)] for i in range(self.__matrix_yValues[1])] for i in
                                range(self.__matrix_xValues[1])]
        self.__imageFormat = None  # 'portrait', 'landscape'

        self.__startX = 0
        self.__startY = 0
        self.__move = False  # Boolean: False / True
        self.__moveHorizontal = None  # 'right', 'left', 'false'
        self.__moveVertical = None  # 'up', 'down', 'false'
        self.__moveTime = 1.0  # Angaben in Sekunden, Bild wird alle x Sekunden bewegt

        self.__blinken = False  # Boolean: False / True
        self.__Hz = 1.0  # Frequenz: Hertz = Vorgänge pro Sekunde 1
        self.__timingRatio = [1, 1]  # Bild gleich lange an wie aus  1,1
        self.__on_off = [0.5, 0.5]  # [Bild an, Bild aus] Angaben in Sekunden 0.5 0.5
        self.__light = True  # Boolean: False / True
        self.__heartrate = False  # Boolean: False / True
        self._heartrateOff = 0.5  # Licht aus für 200ms (protected)

        self.__stopped = False  # Boolean: False / True (um die Threads zu stoppen)
        self.__strMove = "Thread move " + self.__objectName + " stopped.\n"
        self.__strBlink = "Thread blink " + self.__objectName + " stopped.\n"

        self.__loadImage__()

        """ Thread für das Blinken """
        self.__threadBlink = threading.Thread(target=self.__blink__, args=())
        self.__threadBlink.daemon = True
        self.__threadBlink.start()

        """ Thread für Bildbewegung """
        self.__threadMove = threading.Thread(target=self.__moveImage__, args=())
        self.__threadMove.daemon = True
        self.__threadMove.start()

    def __loadImage__(self):
        """ Lädt das outputImage einmalig bei der Initialisierung. """
        x = 0
        xMove = 0
        yMove = 0
        while x < len(self.__outputImage):
            y = 0
            while y < len(self.__outputImage[x]):
                self.__outputImage[x][y] = self.__inputImage[xMove][yMove]
                y += 1
                yMove = (yMove + 1) % len(self.__inputImage[xMove])
            x += 1
            xMove = (xMove + 1) % len(self.__inputImage)
            yMove = 0



    def __moveImage__(self):
        """ Methode in separatem Thread, welche für die Bildbewegung zuständig ist.
            inputImage bleibt unverändert, das outputImage wird bei jedem Durchgang angepasst.
            Mögliche Bewegungen: Oben, unten, links, rechts und Kombinationen davon.
        """
        while True:
            if (self.__stopped is True):
                print(self.__strMove)
                break

            if (self.__move is True):
                xMove = 0
                yMove = 0
                if (self.__moveHorizontal is not None and self.__imageFormat != 'portrait'):
                    if (self.__moveHorizontal == 'right'):
                        xMove = (self.__startX + 1) % len(self.__inputImage)
                    if (self.__moveHorizontal == 'left'):
                        xMove = (self.__startX - 1) % len(self.__inputImage)
                    self.__startX = xMove

                if (self.__moveVertical is not None and self.__imageFormat != 'landscape'):
                    if (self.__moveVertical == 'up'):
                        yMove = (self.__startY + 1) % len(self.__inputImage[xMove])
                    if (self.__moveVertical == 'down'):
                        yMove = (self.__startY - 1) % len(self.__inputImage[xMove])
                    self.__startY = yMove

                x = 0
                while x < len(self.__outputImage):
                    y = 0
                    while y < len(self.__outputImage[x]):
                        self.__outputImage[x][y] = self.__inputImage[xMove][yMove]
                        y += 1
                        yMove = (yMove + 1) % len(self.__inputImage[xMove])
                    x += 1
                    xMove = (xMove + 1) % len(self.__inputImage)
                    yMove = self.__startY

            time.sleep(self.__moveTime)

    def __blink__(self):
        """ Methode in separatem Thread, welche für das Blinken zuständig ist.
            Blinken erfolgt durch das 'ein und ausschalten' des Lichts.
        """
        while True:
            if (self.__stopped is True):
                print(self.__strBlink)
                break

            if (self.__blinken is True):
                self.__light = True
                time.sleep(self.__on_off[0])  # für 'on'
                self.__light = False
                time.sleep(self.__on_off[1])  # für 'off'





    # ===========================================================================================
    # public Methoden
    # ===========================================================================================

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/finish[PUT])
    def finish(self):
        """ Stoppt die Threads "moveImage" und "blink". """
        # input("\nPress key to finish Thread\n")
        self.__stopped = True

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/getMatrixPosition[GET])
    def getMatrixPosition(self) -> list:
        """ Gibt die Position zurück, wo das Bild auf dem LED-Display abgebildet werden soll.
            [[Startwert x, Anzahl Spalten], [Startwert y, Anzahl Zeilen]]
            :return lsMatrixValue: list
        """
        lsMatrixValue = [self.__matrix_xValues, self.__matrix_yValues]
        return lsMatrixValue

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/getXvalues[GET])
    def getXvalues(self) -> list:
        """ [Startwert x, Anzahl Spalten]
            :return matrix_xValues: list
        """
        return self.__matrix_xValues

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/getYvalues[GET])
    def getYvalues(self) -> list:
        """ [Startwert y, Anzahl Zeilen]
            :return matrix_yValues: list
        """
        return self.__matrix_yValues

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/getName[GET])
    def getName(self) -> str:
        """ Gibt den Namen der Instanz zurück.
            :return: objectName: str
        """
        return self.__objectName

    # ===== Image-Methoden =====

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/getImage[GET])
    def getImage(self) -> list:
        """ Gibt das aktuelle Bild zurück (outputImage)
            oder ein leeres Bild (lightOffImage)
            wenn das Licht ausgeschalten ist.
            :returns outputImage or lightOffImage: list
        """
        if (self.__light is True):
            return self.__outputImage
        else:
            return self.__lightOffImage

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/getLightOffImage[GET])
    def getLightOffImage(self) -> list:
        """ Gibt ein leeres Bild zurück, Farbwerte [0,0,0].
            :return lightOffImage: list
        """
        return self.__lightOffImage

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/setLightOffImage/<list:image>[PUT])
    def setLightOffImage(self, image: list):
        """ Definiert ein "Licht aus Bild".
            :param image: list
        """
        x = 0
        xImage = 0
        yImage = 0
        while x < len(self.__lightOffImage):
            y = 0
            while y < len(self.__lightOffImage[x]):
                self.__lightOffImage[x][y] = image[xImage][yImage]
                y += 1
                yImage = (yImage + 1) % len(image[xImage])
            x += 1
            xImage = (xImage + 1) % len(image)
            yImage = 0


    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/setLightOffImageColor/<int:red> /<int:green>/<int:blue>[PUT])
    def setLightOffImageColor(self, red: int, green: int, blue: int):
        """ Aendert die Farbe des "Licht aus Bildes". Int-Wertebereich von 0 bis 255.
            :param red: int
            :param green: int
            :param blue: int
        """
        self.__lightOffImage = [[[red, green, blue] for i in range(self.__matrix_yValues[1])] for i in
                                range(self.__matrix_xValues[1])]

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/resetLightOffImage[PUT])
    def resetLightOffImage(self):
        """ Zurücksetzen des "Licht aus Bildes", mit den Farbwerten [0,0,0]. """
        self.__lightOffImage = [[[0 for i in range(3)] for i in range(self.__matrix_yValues[1])] for i in
                                range(self.__matrix_xValues[1])]

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/setImageFormat/<str:imageFormat>[PUT])
    def setImageFormat(self, imageFormat: 'portrait' 'landscape' = None):
        """ Mögliche Auswahl: 'default', 'portrait' (= hochformat), 'landscape' (= querformat)
            Portrait-Bilder lassen sich nur nach oben/unten bewegen.
            Landscape-Bilder lassen sich nur nach links/rechts bewegen
            :param imageFormat: str
        """
        self.__imageFormat = imageFormat

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/setInputImage/<list:image>/<str:imageFormat>[PUT])
    def setInputImage(self, image: list, imageFormat: 'portrait' 'landscape' = None):
        """ Aendert das input-Bild.
            Die Bildgrösse sollte der Grösse des instanzierten Objektes MoveableImage() entsprechen.
            Die optimale Bildgrösse kann mit getImageSizeAsText() bzw. mit getImageSize() abgefragt werden.
            Ausserdem kann das Bildformat gewählt werden: default, portrait = hochformat, landscape = querformat.
            Portrait-Bilder lassen sich nur nach oben/unten bewegen.
            Landscape-Bilder lassen sich nur nach links/rechts bewegen
            :param image: list
            :param imageFormat: str
        """
        self.__startX = 0
        self.__startY = 0
        self.__inputImage = image
        self.__loadImage__()
        self.__imageFormat = imageFormat

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/getImageSizeAsText[GET])
    def getImageSizeAsText(self) -> str:
        """ :return  image-size: str
        """
        size = self.getImageSize()
        return "Optimale Bildgrösse: x = %d, y = %d." % (size[0], size[1])

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/getImageSize[GET])
    def getImageSize(self) -> list:
        """ [x, y] | x = Anzahl Spalten / y = Anzahl Zeilen
            :return image-size: list
        """
        return [self.__matrix_xValues[1], self.__matrix_yValues[1]]

    # ===== Move-Methoden =====

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/startBlink[PUT])
    def startBlink(self):
        """ Blink-Flag wird auf True gesetzt. """
        self.__blinken = True

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/stopBlink[PUT])
    def stopBlink(self):
        """ Blink-Flag wird auf False gesetzt. """
        self.__blinken = False
        time.sleep(1)
        self.__light = True

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/startMove[PUT])
    def startMove(self):
        """ Move-Flag wird auf True gesetzt. """
        self.__move = True

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/waiting[PUT])
    def waiting(self):
        """ Move-Flag wird auf False gesetzt. """
        self.__move = False

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/stopMove[PUT])
    def stopMove(self):
        """ Move-Flag wird auf False gesetzt.
            moveHorizontal, moveVertical werden auf 'false' gesetzt.
        """
        self.__move = False
        self.__moveHorizontal = None
        self.__moveVertical = None

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/resetMove[PUT])
    def resetMove(self):
        """ Ruft die Methoden stopMove() und stopBlink() auf.
            startX und startY werden auf 0 gesetzt.
        """
        self.stopMove()
        self.stopBlink()
        self.__startX = 0
        self.__startY = 0
        self.__loadImage__()

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/moveRight[PUT])
    def moveRight(self):
        """ Ruft startMove() auf, moveHorizontal wird auf 'right' gesetzt. """
        self.startMove()
        self.__moveHorizontal = 'right'

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/moveLeft[PUT])
    def moveLeft(self):
        """ Ruft startMove() auf, moveHorizontal wird auf 'left' gesetzt. """
        self.startMove()
        self.__moveHorizontal = 'left'

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/stopMoveHorizontal[PUT])
    def stopMoveHorizontal(self):
        """ moveHorizontal wird auf 'false' gesetzt. """
        self.__moveHorizontal = None

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/moveUp[PUT])
    def moveUp(self):
        """ Ruft startMove() auf, moveVertical wird auf 'up' gesetzt. """
        self.startMove()
        self.__moveVertical = 'up'

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/moveDown[PUT])
    def moveDown(self):
        """ Ruft startMove() auf, moveVertical wird auf 'down' gesetzt. """
        self.startMove()
        self.__moveVertical = 'down'

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/stopMoveVertical[PUT])
    def stopMoveVertical(self):
        """ moveVertical wird auf 'false' gesetzt. """
        self.__moveVertical = None

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/getMove[GET])
    def getMoveInfo(self) -> list:
        """ Gibt die Bewegungsinformationen zurück:
            move, moveHorizontal, moveVertical, moveTime,
            blinken, heartrate, Hz, timingRatio, on_off
            :return lsMove: list
        """
        lsMove = [['move', self.__move],
                  ['horizontal', self.__moveHorizontal],
                  ['vertical', self.__moveVertical],
                  ['moveTime', self.__moveTime],
                  ['blinken', self.__blinken],
                  ['heartrate', self.__heartrate],
                  ['rate', self.__Hz],
                  ['timingRatio', self.__timingRatio],
                  ['light on/light off', self.__on_off]]
        return lsMove

    # ===== Geschwindigkeiten, Frequenzen =====

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/setMoveTime/<float:second>[PUT])
    def setMoveTime(self, second: float = 1.0):
        """ Beeinflusst die time.sleep() beim moveImage-Thread.
            Default: 1 Sekunde.
            :param second: float
        """
        self.__moveTime = second

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/setRate/<float:hertz>[PUT])
    def setRate(self, hertz: float = 1.0):
        """ Anzahl Vorgänge pro Sekunde, diese Methode nicht für Puls-Frequenzen aufrufen!
            Berechnet die Light-on/off-Zeit unter Berücksichtigung des Heartrate-Flags.
            :param hertz: float
        """
        self.__Hz = hertz
        if (self.__heartrate is False):
            self.__on_off[0] = (1 / (hertz * (self.__timingRatio[0] + self.__timingRatio[1]))) * self.__timingRatio[
                0]  # on
            self.__on_off[1] = (1 / (hertz * (self.__timingRatio[0] + self.__timingRatio[1]))) * self.__timingRatio[
                1]  # off
        else:
            if ((1 / self.__Hz) - self._heartrateOff > 0):
                self.__on_off[0] = (1 / self.__Hz) - self._heartrateOff
                self.__on_off[1] = self._heartrateOff
            else:
                x = 1 / (self.__Hz * 2)
                self.__on_off[0] = x
                self.__on_off[1] = x

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/setPuls/<int:puls>[PUT])
    def setPuls(self, puls: int):
        """ Puls übergeben. Methode setzt den Heartrate-Flag auf True (default-Wert).
            Ruft setRate() und startBlink() auf.
            :param puls: int
        """
        self.setRate(puls / 60)
        self.setHeartrateFlag()
        self.startBlink()

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/setTimingRatio/<int:ratioOn>/<int:ratioOff>[PUT])
    def setTimingRatio(self, ratioOn: int = 1, ratioOff: int = 1):
        """ Aendert das Taktverhältnis der Blink-Frequenz.
            Defaultmässig ist [1,1] definiert, also gleich lange Licht ein wie aus.
            :param ratioOn:
            :param ratioOff:
        """
        self.__timingRatio[0] = ratioOn
        self.__timingRatio[1] = ratioOff
        if (self.__heartrate is False):
            self.__on_off[0] = (1 / (self.__Hz * (ratioOn + ratioOff))) * ratioOn  # on
            self.__on_off[1] = (1 / (self.__Hz * (ratioOn + ratioOff))) * ratioOff  # off

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/setHeartrate/<bool:boolean>[PUT])
    def setHeartrateFlag(self, boolean: bool = True):
        """ wird der Flag auf true gesetzt,
            wird der timme.sleep-Wert (self.__on_off) mit setRate() anders berechnet
            :param boolean: bool
        """
        if (boolean is True):
            self.__heartrate = True
        else:
            self.__heartrate = False
            self.setRate(self.__Hz)

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/MoveableImage/light/<bool:state>[PUT])
    def light(self, state: bool = True):
        """ Um das Licht ein- und auszuschalten.
            :param state: bool
        """
        self.__blinken = False
        time.sleep(1)
        self.__light = state
