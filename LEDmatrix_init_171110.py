from tinkerforge.brick_master import BrickMaster
from tinkerforge.bricklet_led_strip import BrickletLEDStrip
from tinkerforge.ip_connection import IPConnection
import matrixProperties
import time


# LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/LEDmatrixConnect)
# noinspection PyPep8Naming,PyRedundantParentheses
class LEDmatrixConnect(object):
    """
    init() wird automatisch nach der Erzeugung der Instanz aufgerufen. (-> magische Methode)
    Erstellt ein device Objekt und baut die Verbindung zu brickd auf. (Verbindung zu Master Brick????)
    """
    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/LEDmatrixConnect[POST])
    def __init__(self):

        # Attribute importiert
        self.__UIDmaster = matrixProperties.UIDmaster  # "6et15y"
        self.__UIDbricklet = matrixProperties.UIDbricklet  # "wVj"
        self.__HOST = matrixProperties.HOST  # "localhost"
        self.__PORT = matrixProperties.PORT  # 4223
        self.__matrixIndexRed = matrixProperties.IndexRed  # 0
        self.__matrixIndexGreen = matrixProperties.IndexGreen  # 1
        self.__matrixIndexBlue = matrixProperties.IndexBlue  # 2
        self.__rows = matrixProperties.ROWS  # 10
        self.__columns = matrixProperties.COLUMNS  # 20
        self.__LEDnr = matrixProperties.LEDnr  # Liste LED-Nummern 0 bis 199
        self.__numLEDS = matrixProperties.NUM_LEDS  # 16
        self.__rgb = [[0 for i in range(self.__numLEDS)] for i in range(3)]  # RGB-Array

        self.__image = matrixProperties.defaultImage  # Default-Bild setzen
        self.__imageIndexRed = 0
        self.__imageIndexGreen = 1
        self.__imageIndexBlue = 2

        # Instanzvariablen
        self.__light = True  # Boolean: True / False

        # Objekte 
        print("Instanz LEDmatrix wurde erstellt.")
        self.__ipcon = IPConnection()  # Create IP connection
        self.__masterBrick = BrickMaster(self.__UIDmaster, self.__ipcon)
        self.__brickletLEDstrip = BrickletLEDStrip(self.__UIDbricklet, self.__ipcon)  # Create device object
        # Connect to brickd --> Verbindung Masterbrick? richtiger RGB-Kanal einstellen?
        self.__ipcon.connect(self.__HOST,
                             self.__PORT)
        print("Verbindung zu brickd hergestellt.")
        self.__brickletLEDstrip.set_frame_duration(20)  # Anzeigedauer Bild: 20ms ergibt 20 Bilder pro Sekunde
        self.__brickletLEDstrip.set_channel_mapping(self.__brickletLEDstrip.CHANNEL_MAPPING_RGB)  # CHANNEL_MAPPING_RGB = 6 -> Farbkanal definieren (RGB statt BGR)

        # Callback starten
        self.__brickletLEDstrip.register_callback(self.__brickletLEDstrip.CALLBACK_FRAME_RENDERED,
                                                  lambda x: self.__loadPicture__())

        print("Callback aktiviert.")

    # ======= private Methoden ==========================================================================
    # fillRGBs(), fillAsc(), fillDesc(), loadPicture()



    def __fillRGBs__(self, yMatrix, xImage, yImage):
        """ Private Methode: Füllt die Farbinformationen für einen Pixel in die einzelnen RGB-Arrays ab. """
        self.__rgb[self.__matrixIndexRed][yMatrix] = self.__image[xImage][yImage][self.__imageIndexRed]
        self.__rgb[self.__matrixIndexGreen][yMatrix] = self.__image[xImage][yImage][self.__imageIndexGreen]
        self.__rgb[self.__matrixIndexBlue][yMatrix] = self.__image[xImage][yImage][self.__imageIndexBlue]

    def __fillAsc__(self, xImage, yMatrix):
        """ Private Methode: Füllt eine Spalte für die LED-Matrix aus (von unten nach oben) """  # 0 bis 9
        yImage = 0
        i = 0
        while (i < self.__rows):  # i < 10
            self.__fillRGBs__(yMatrix, xImage, yImage)
            i += 1
            yImage += 1
            yMatrix += 1
            if (yMatrix >= self.__rows):
                yMatrix = 0

    def __fillDesc__(self, xImage, yMatrix):
        """ Private Methode: Füllt eine Spalte für die LED-Matrix aus (von oben nach unten) """  # 9 bis 0
        yImage = 0
        i = 0
        while (i < self.__rows):  # i < 10
            self.__fillRGBs__(yMatrix, xImage, yImage)
            i += 1
            yImage += 1
            yMatrix -= 1
            if (yMatrix < 0):
                yMatrix = self.__rows - 1

    def __loadPicture__(self):
        """ Methode lädt ein ganzes Bild, sofern self.__light auf True gesetzt ist => Licht an. """

        if (self.__light is True):

            xMatrix = 0
            yMatrix = 0
            xImage = 0
            columns = self.__columns  # 20
            while (columns > 0):
                if (xMatrix % 2 == 0):  # Farbwerte von image-array nach rgb-array bei gerader Spalte
                    y = 0
                    self.__fillAsc__(xImage, yMatrix)
                else:  # Farbwerte von image-array nach rgb-array bei ungerader Spalte
                    y = self.__rows - 1
                    self.__fillDesc__(xImage, self.__rows - (yMatrix + 1))

                # Aufrufen der Methode set_rgb_values(index, length, r, g, b). (r, g, b, verlangen 16er-Array's)
                self.__brickletLEDstrip.set_rgb_values(self.__LEDnr[xMatrix][y], self.__rows,  # self.__rows = 10
                                                       self.__rgb[self.__matrixIndexRed],
                                                       self.__rgb[self.__matrixIndexGreen],
                                                       self.__rgb[self.__matrixIndexBlue])

                columns -= 1
                xImage += 1
                xMatrix += 1
                if xMatrix >= self.__columns:
                    xMatrix = 0
                    xImage = 0

    # ======= public Methoden ==================================================
    # connect(), finish(), setVelocity(), lightOff(), setImage(), getImage()

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/LEDmatrixConnect/connect[PUT])
    def connect(self):
        """ Verbindungsaufbau """
        self.__ipcon.connect(self.__HOST, self.__PORT)
        print("Verbindung zu brickd hergestellt.")

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/LEDmatrixConnect/finish[PUT])
    def finish(self):
        """ Beendet die Verbindung. """
        # input("Press key to exit\n")
        self.__ipcon.disconnect()
        print("Verbindung beendet.")

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/LEDmatrixConnect/setVelocity/<int:frequenz>[PUT])
    def setFrameDuration(self, millisec: int = 20):
        """ Set frame duration to 50ms (20 frames per second).
        Verändert die Anzeigedauer eines Frames.
        :param millisec: int
        """
        self.__brickletLEDstrip.set_frame_duration(millisec)

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/LEDmatrixConnect/getFrameDuration[GET])
    def getFrameDuration(self) -> int:
        """ Gibt einen int-Wert zurück. Anzeigedauer der Frames auf dem LED-Display.
        (20ms entspricht 50 Bilder/Sekunde)
        :return frame duration: int
        """
        return self.__brickletLEDstrip.get_frame_duration()

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/LEDmatrixConnect/light/<boolean:status>[PUT])
    def light(self, status: bool = True):  # status = boolean True / False
        """ Licht-Regelung auf 'unterster' Stufe, wirkt sich auf den gesamten LED-Display.
        True = 'Licht an', False = 'Licht aus'
        :param status: boolean
        """
        self.__light = status

        time.sleep(1)

        if (status is False):
            i = 0
            while i < self.__columns:  # hier 20
                self.__brickletLEDstrip.set_rgb_values(i * 10, 10, [0] * self.__numLEDS, [0] * self.__numLEDS,
                                                       [0] * self.__numLEDS)
                i += 1

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/LEDmatrixConnect/setImage/<list:image>[PUT])
    def setImage(self, image: list):
        """ Liste mit den RGB-Werten der
        Form [[[red, green, blue] for i in range(x columns)] for i in range(y rows)]
        :param image: list
        """
        self.__image = image

    # @LEDmatrix.route('ledmatrix.bfh.ch/api/v1.0/LEDmatrixConnect/setImageRGBindex/<int:red>/<int:green>/<int:blue>[PUT])
    def setImageRGBindex(self, red: int, green: int, blue: int):
        """ Werte: 0 bis 2, Default: red = 0, green = 1, blue = 2
        :param red: int
        :param green: int
        :param blue: int
        """
        self.__imageIndexRed = red
        self.__imageIndexGreen = green
        self.__imageIndexBlue = blue
