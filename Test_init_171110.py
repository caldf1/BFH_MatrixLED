from LEDmatrix_init_171110 import *
import imageProperties
import time


if __name__ == "__main__":
    matrix = LEDmatrixConnect()
    
    print(matrix.getFrameDuration())            # 4
    matrix.setFrameDuration(50)                 # 3
    print(matrix.getFrameDuration())            # 4
    time.sleep(3)
    matrix.setImage(imageProperties.hearts1)    # 6
    time.sleep(1.5)
    matrix.setImageRGBindex(2, 2, 2)            # 7
    time.sleep(2)
    matrix.setImageRGBindex(1, 1, 1)            # 7
    time.sleep(2)
    matrix.setImageRGBindex(0, 0, 0)            # 7
    time.sleep(2)
    matrix.setImageRGBindex(0, 1, 2)            # 7
    time.sleep(2)

    matrix.light(False)                         # 5
    time.sleep(1.5)
    matrix.light(True)                          # 5
    time.sleep(1.5)
    matrix.finish()                             # 2
    time.sleep(1.5)
    matrix.connect()                            # 1
    matrix.setImage(imageProperties.forms1)     # 6
    time.sleep(1.5)
    matrix.light(False)                         # 5
    time.sleep(1)
    matrix.finish()                             # 2
