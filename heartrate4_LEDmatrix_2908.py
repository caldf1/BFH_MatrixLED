from LEDmatrix_2308_init import *
#from MoveableLEDMatrix_2308 import *
import imageProperties
import matrixProperties
import threading
import time
import copy

class heartrate4_LEDmatrix(object):

    def __init__(self, text=imageProperties.pulstext, heart1=imageProperties.heartred, heart2=imageProperties.heartyellow, heart3=imageProperties.heartgreen, heart4=imageProperties.heartblue):

        self.__blinkInterval = 0.2
        self.__matrix = LEDmatrix()
               

        self.__textfield = text     # x: 0 - 19 und y: 0 - 4 (Grösse: 20x, 5y)
        self.__matrixTextfield = [[[] for i in range(5)] for i in range(matrixProperties.COLUMNS)]
        self.__rateTextfield = 0.5
        self.__stopThreadTextfield = 'false'
        threadTextfield = threading.Thread(target=self.__runTextfield__, args=())
        threadTextfield.daemon = True
        threadTextfield.start()
        
        
        self.__heart1 = heart1        # x: 0 - 4 und y: 5 - 9 (Grösse: 5x, 5y)
        self.__matrixHeart1 = [[[] for i in range(5)] for i in range(5)]
        self.__heartrate1 = 0.33
        self.__stopThreadHeart1 = 'false'
        threadHeart1 = threading.Thread(target=self.__runHeart1__, args=())
        threadHeart1.daemon = True
        threadHeart1.start()
        
        
        self.__heart2 = heart2        # x: 5 - 9 und y: 5 - 9 (Grösse: 5x, 5y)
        self.__matrixHeart2 = [[[] for i in range(5)] for i in range(5)]
        self.__heartrate2 = 1.25
        self.__stopThreadHeart2 = 'false'
        threadHeart2 = threading.Thread(target=self.__runHeart2__, args=())
        threadHeart2.daemon = True
        threadHeart2.start()
        

        self.__heart3 = heart3        # x: 10 - 14 und y: 5 - 9 (Grösse: 5x, 5y)
        self.__matrixHeart3 = [[[] for i in range(5)] for i in range(5)]
        self.__heartrate3 = 0.5
        self.__stopThreadHeart3 = 'false'
        threadHeart3 = threading.Thread(target=self.__runHeart3__, args=())
        threadHeart3.daemon = True
        threadHeart3.start()
        

        self.__heart4 = heart4        # x: 15 - 19 und y: 5 - 9 (Grösse: 5x, 5y)
        self.__matrixHeart4 = [[[] for i in range(5)] for i in range(5)]
        self.__heartrate4 = 1
        self.__stopThreadHeart4 = 'false'
        threadHeart4 = threading.Thread(target=self.__runHeart4__, args=())
        threadHeart4.daemon = True
        threadHeart4.start()

        
        self.__matrixImage = [[0 for i in range(matrixProperties.ROWS)] for i in range(matrixProperties.COLUMNS)]
        self.__stopThreadMerge = 'false'
        threadMerge = threading.Thread(target=self.__runMerge__, args=())
        threadMerge.daemon = True
        threadMerge.start()
        
        
        
        

 


    def __mergeMatrixImage__(self):

        # textfield in matrixImage: x: 0 - 19 und y: 0 - 4 (Grösse: 20x, 5y)
        x = 0
        y = 0
        while x < 20:
            while y < 5:
                self.__matrixImage[x][y] = self.__matrixTextfield[x][y]
                y += 1
            x += 1
            y = 0

        # heart1 in matrixImage: x: 0 - 4 und y: 5 - 9 (Grösse: 5x, 5y)
        # heart2 in matrixImage: x: 5 - 9 und y: 5 - 9 (Grösse: 5x, 5y)
        # heart3 in matrixImage: x: 10 - 14 und y: 5 - 9 (Grösse: 5x, 5y)
        # heart4 in matrixImage: x: 15 - 19 und y: 5 - 9 (Grösse: 5x, 5y)
        x = 0
        y = 0
        while x < 5:
            while y < 5:
                self.__matrixImage[x][y+5] = self.__matrixHeart1[x][y]
                self.__matrixImage[x+5][y+5] = self.__matrixHeart2[x][y]
                self.__matrixImage[x+10][y+5] = self.__matrixHeart3[x][y]
                self.__matrixImage[x+15][y+5] = self.__matrixHeart4[x][y]
                y += 1
            x += 1
            y = 0


        self.__matrix.setImage(self.__matrixImage)
            

#======= run Methoden (eigene Threads) ================================================== 

    
    def __runTextfield__(self):
        """ Method that runs forever """
        while True:
            # print("thread textfield runs") # zum testen
            if self.__stopThreadTextfield == 'true':
                print("Textfield Thread stopped")
                break

            self.__matrixTextfield = copy.deepcopy(self.__textfield)
            time.sleep(1)
            


    def __runHeart1__(self):
        """ Method that runs forever """
        while True:
            # print("thread heart1 runs") # zum testen
            if self.__stopThreadHeart1 == 'true':
                print("Heart 1 Thread stopped")
                break
        
            self.__matrixHeart1 = copy.deepcopy(self.__heart1)
            if (self.__heartrate1 - self.__blinkInterval) <= 0:
                time.sleep(self.__heartrate1)
            else:
                time.sleep(self.__heartrate1 - self.__blinkInterval) # Variante 1
            self.__matrixHeart1 = [[[0 for i in range (3)] for i in range(matrixProperties.ROWS)] for i in range(matrixProperties.COLUMNS)]
            time.sleep(self.__blinkInterval) # Variante 1 

 

    def __runHeart2__(self):
        """ Method that runs forever """        
        while True:
            # print("thread heart2 runs") # zum testen
            if self.__stopThreadHeart2 == 'true':
                print("Heart 2 Thread stopped")
                break
        
            self.__matrixHeart2 = copy.deepcopy(self.__heart2)
            if (self.__heartrate2 - self.__blinkInterval) <= 0:
                time.sleep(self.__heartrate2)
            else:
                time.sleep(self.__heartrate2 - self.__blinkInterval) # Variante 1
            self.__matrixHeart2 = [[[0 for i in range (3)] for i in range(matrixProperties.ROWS)] for i in range(matrixProperties.COLUMNS)]
            time.sleep(self.__blinkInterval) # Variante 1 


    def __runHeart3__(self):
        """ Method that runs forever """
        while True:
            # print("thread heart3 runs") # zum testen
            if self.__stopThreadHeart3 == 'true':
                print("Heart 3 Thread stopped")
                break

            self.__matrixHeart3 = copy.deepcopy(self.__heart3)
            if (self.__heartrate3 - self.__blinkInterval) <= 0:
                time.sleep(self.__heartrate3)
            else:
                time.sleep(self.__heartrate3 - self.__blinkInterval) # Variante 1
            self.__matrixHeart3 = [[[0 for i in range (3)] for i in range(matrixProperties.ROWS)] for i in range(matrixProperties.COLUMNS)]
            time.sleep(self.__blinkInterval) # Variante 1 

            

    def __runHeart4__(self):
        """ Method that runs forever """
        while True:
            # print("thread heart4 runs") # zum testen
            if self.__stopThreadHeart4 == 'true':
                print("Heart 4 Thread stopped")
                break
        
            self.__matrixHeart4 = copy.deepcopy(self.__heart4)
            if (self.__heartrate4 - self.__blinkInterval) <= 0:
                time.sleep(self.__heartrate4)
            else:
                time.sleep(self.__heartrate4 - self.__blinkInterval) # Variante 1
            self.__matrixHeart4 = [[[0 for i in range (3)] for i in range(matrixProperties.ROWS)] for i in range(matrixProperties.COLUMNS)]
            time.sleep(self.__blinkInterval) # Variante 1 


    def __runMerge__(self):
        """ Method that runs forever """
        while True:
            #print("thread merge runs") # zum testen
            if self.__stopThreadMerge == 'true':
                print("Merge Thread stopped")
                break
        
            self.__mergeMatrixImage__()
            time.sleep(0.02)
            
        
 #======= public Methoden ==================================================       


    def finish(self):
        self.__matrix.finish()
        input("\nPress key to finish Thread\n")
        self.__stopThreadMerge = 'true'
        self.__stopThreadTextfield = 'true'
        self.__stopThreadHeart1 = 'true'
        self.__stopThreadHeart2 = 'true'
        self.__stopThreadHeart3 = 'true'
        self.__stopThreadHeart4 = 'true'



        

    def setHeartrate(self, heartNumber, rate):
        if heartNumber == 1:
            self.__heartrate1 = rate

        if heartNumber == 2:
            self.__heartrate2 = rate

        if heartNumber == 3:
            self.__heartrate3 = rate

        if heartNumber == 4:
            self.__heartrate4 = rate

        else:
            return "invalid heart number, take a number from 1 to 4"



    def getHeartrate(self):
        heartrate = "Puls 1: ", self.__heartrate1, "\nPuls 2: ", self.__heartrate2, "\nPuls 3: ", self.__heartrate3, "\nPuls 4: ", self.__heartrate4
        return heartrate
