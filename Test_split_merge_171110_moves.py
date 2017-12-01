from LEDmatrix_split_merge_171110 import *
import imageProperties
import time

if __name__ == "__main__":
    
    
    print("\nBewegungs-Test: Case 'square'\n")  # ===================================================================
    matrix = LEDmatrix('square')
    images = matrix.getObjects()
    imageObj = images[0]

    time.sleep(2)

    imageObj.setInputImage(imageProperties.bild11Zeilen) # auch schön mit imageProperties.hearts1
    time.sleep(2)

    imageObj.setMoveTime(0.1)
    imageObj.setRate(10)

    imageObj.moveRight()
    time.sleep(2)

    imageObj.startBlink()
    time.sleep(2)
    imageObj.stopBlink()
    time.sleep(2)
    
    imageObj.moveLeft()
    time.sleep(2)
    imageObj.stopMoveHorizontal()
    time.sleep(2)
    
    imageObj.moveUp()
    time.sleep(2)
    imageObj.moveDown()
    time.sleep(2)
    imageObj.stopMoveVertical()
    time.sleep(2)

    imageObj.moveRight()
    imageObj.moveUp()
    time.sleep(3)

    imageObj.moveDown()
    time.sleep(3)
    
    imageObj.moveLeft()
    time.sleep(3)
    
    imageObj.moveUp()
    time.sleep(3)
    
    imageObj.resetMove()


    matrix.getMatrix().light(False)
    time.sleep(3)

    matrix.finish()
    print('\nBewegungs-Test erfolgreich.\n')
    time.sleep(5)



