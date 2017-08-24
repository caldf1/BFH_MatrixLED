from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_led_strip import BrickletLEDStrip
import matrixProperties
import imageProperties

class LEDmatrix:


    """
    init() wird automatisch nach der Erzeugung der Instanz aufgerufen. (-> magische Methode)
    Erstellt ein device Objekt und baut die Verbindung zu brickd auf.
    """
    def __init__(self): #(self, var)
        print("Instanz LEDmatrix wurde erstellt.")
        self.__ipcon = IPConnection()                                               # Create IP connection
        self.__deviceObject = BrickletLEDStrip(matrixProperties.UID, self.__ipcon)  # Create device object
        self.__ipcon.connect(matrixProperties.HOST, matrixProperties.PORT)          # Connect to brickd
        print("Verbindung zu brickd hergestellt.")
        self.__deviceObject.set_frame_duration(20)                                 # Default-Geschwindigkeit setzen

        self.__image = imageProperties.defaultImage                                 # Default-Bild setzen
        self.__rgb = matrixProperties.colorRowsRGB()                                # leerer RGB-Array setzen

        self.__deviceObject.register_callback(self.__deviceObject.CALLBACK_FRAME_RENDERED,
                                              lambda x: self.__loadPicture__())

        print("Callback aktiviert.")


#======= private Methoden ==========================================================================
# fillRGBs(), fillAsc(), fillDesc(), loadPicture()


    """ Private Methode: Füllt die Farbinformationen für einen Pixel in die einzelnen RGB-Arrays ab. """
    def __fillRGBs__(self, yMatrix, xImage, yImage):        
        self.__rgb[matrixProperties.IndexRed][yMatrix]   = self.__image[xImage][yImage][imageProperties.IndexRed]
        self.__rgb[matrixProperties.IndexGreen][yMatrix] = self.__image[xImage][yImage][imageProperties.IndexGreen]
        self.__rgb[matrixProperties.IndexBlue][yMatrix]  = self.__image[xImage][yImage][imageProperties.IndexBlue]

        
    """ Private Methode: Füllt eine Spalte für die LED-Matrix aus (von unten nach oben) """ # 0 bis 9
    def __fillAsc__(self, xImage, yMatrix):
        yImage = 0
        i = 0
        while i < matrixProperties.ROWS: # i < 10
            self.__fillRGBs__(yMatrix, xImage, yImage)
            i += 1
            yImage += 1
            yMatrix += 1
            if yMatrix >= matrixProperties.ROWS:
                yMatrix = 0



    """ Private Methode: Füllt eine Spalte für die LED-Matrix aus (von oben nach unten) """ # 9 bis 0
    def __fillDesc__(self, xImage, yMatrix):
        yImage = 0
        i = 0
        while i < matrixProperties.ROWS: # i < 10
            self.__fillRGBs__(yMatrix, xImage, yImage)
            i += 1
            yImage += 1
            yMatrix -= 1
            if yMatrix < 0:
                yMatrix = matrixProperties.ROWS - 1


    def __loadPicture__(self):
        xMatrix = 0
        yMatrix = 0
        xImage = 0 #self.__xImage
        columns = matrixProperties.COLUMNS
        while columns > 0:
            if xMatrix %2 == 0:
                y = 0 #0
                self.__fillAsc__(xImage, yMatrix) # Farbwerte von image-array nach rgb-array bei ungerader Spalte
            else:
                y = matrixProperties.ROWS - 1
                self.__fillDesc__(xImage, matrixProperties.ROWS - (yMatrix + 1)) # Farbwerte von image-array nach rgb-array bei gerader Spalte

            # Aufrufen der Methode set_rgb_values(index, length, r, g, b), bei unserer Matrix ist das r und b vertauscht. (r, g, b, verlangen 16er-Array's)
            self.__deviceObject.set_rgb_values(matrixProperties.LEDnr[xMatrix][y], matrixProperties.ROWS, self.__rgb[matrixProperties.IndexBlue], self.__rgb[matrixProperties.IndexGreen], self.__rgb[matrixProperties.IndexRed])                   

            columns -= 1
            xImage += 1
            xMatrix += 1
            if xMatrix >= matrixProperties.COLUMNS:
                xMatrix = 0
                xImage = 0


#======= public Methoden ==================================================
# connect(), finish(), setVelocity(), lightOff(), setImage(), getImage()


    def connect(self):
        self.__ipcon.connect(matrixProperties.HOST, matrixProperties.PORT)
        print("Verbindung zu brickd hergestellt.")
     

    def finish(self):
        input("Press key to exit\n")
        self.__ipcon.disconnect()
        print("Verbindung beendet.")
        

    def setVelocity(self, frequenz):
        # Set frame duration to 50ms (20 frames per second)
        self.__deviceObject.set_frame_duration(frequenz)

    """ alle LED-Farbwerte löschen (ohne das Bild zu löschen) 
    def lightOff(self):
        i = 0
        while i < 20: # hier 20
            self.__deviceObject.set_rgb_values(i*10, 10, [0]*matrixProperties.NUM_LEDS, [0]*matrixProperties.NUM_LEDS, [0]*matrixProperties.NUM_LEDS)
            i += 1
    """

    """ Methoden: Bild ändern und als Array zurückgeben"""

    def setImage(self, image):
        self.__image = image        

               
    def getImage(self):
        return self.__image # Array



    
