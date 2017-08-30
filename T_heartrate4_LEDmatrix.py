from heartrate4_LEDmatrix_2908 import *
import imageProperties
import matrixProperties

if __name__ == "__main__":

    
  
    heartrateMatrix = heartrate4_LEDmatrix()
    time.sleep(5)
    heartrateMatrix.finish()

"""

    # textfield in matrixImage: x: 0 - 19 und y: 0 - 4 (Grösse: 20x, 5y)
    x = 0
    while x < 20:
        print(x)
        x += 1

    # heart1 in matrixImage: x: 0 - 4 und y: 5 - 9 (Grösse: 5x, 5y)
    # heart2 in matrixImage: x: 5 - 9 und y: 5 - 9 (Grösse: 5x, 5y)
    # heart3 in matrixImage: x: 10 - 14 und y: 5 - 9 (Grösse: 5x, 5y)
    # heart4 in matrixImage: x: 15 - 19 und y: 5 - 9 (Grösse: 5x, 5y)
    x = 0
    y = 0
    while x < 5:
        while y < 5:
            print("Heart[", x,",", y,"]")
            print("MatrixImage[", x,",",y+5,"]")
            print("MatrixImage[", x+5,",",y+5,"]")
            print("MatrixImage[", x+10,",",y+5,"]")
            print("MatrixImage[", x+15,",",y+5,"]")
            y += 1
        x += 1
        y = 0
        
    matrix = [[0 for i in range(matrixProperties.ROWS)] for i in range(matrixProperties.COLUMNS)]
    for x in matrix:
        print(x)
"""
    

   
   
