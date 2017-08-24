from MoveableLEDMatrix_2308 import *
import imageProperties

if __name__ == "__main__":

    
    moveMatrix = MoveableLEDMatrix(0.1, imageProperties.hiOli)

    time.sleep(2)
    moveMatrix.moveRight()
    time.sleep(3)
 #   moveMatrix.moveDown()
#    time.sleep(3)
#    moveMatrix.moveRight()
#    time.sleep(3)
#    moveMatrix.moveUp()
#    time.sleep(3)
    moveMatrix.reset()

    

   
   
