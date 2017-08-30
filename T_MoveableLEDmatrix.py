from MoveableLEDmatrix_2308 import *
import imageProperties


if __name__ == "__main__":

    
    moveMatrix = MoveableLEDmatrix( 1, imageProperties.hello, 'normal')

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
 #   moveMatrix.lightOff()
    moveMatrix.finish()

    

   
   
