from MoveableLEDMatrix_2308 import *
import imageProperties
import images

if __name__ == "__main__":

    
    moveMatrix = MoveableLEDMatrix(0.25, imageProperties.hello, 'normal')

    time.sleep(1)
    moveMatrix.moveRight()
    time.sleep(2)
 #   moveMatrix.moveDown()
#    time.sleep(3)
#    moveMatrix.moveRight()
#    time.sleep(3)
#    moveMatrix.moveUp()
#    time.sleep(3)
 #   moveMatrix.reset()
#    moveMatrix.lightOff()
    moveMatrix.finish()

    

   
   
