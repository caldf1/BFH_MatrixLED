from LEDmatrix_split_merge_171110 import *
import time

if __name__ == "__main__":

    print("\nTest: Case 0 'default'\n")  # ===================================================================
    matrix0 = LEDmatrix()
    images0 = matrix0.getObjects()                  # 42

    i = 0
    while (i < len(images0)):
        print('\n%s-index-Nr. %d, Name: %s, Position: ' % (matrix0.getCase(), i, images0[i].getName()),
              images0[i].getMatrixPosition())       # 45, 39, 9
        i += 1

    time.sleep(2)

    matrix0.getMatrix().light(False)                # 43
    time.sleep(3)
    matrix0.getMatrix().light(True)                 # 43
    time.sleep(3)
    matrix0.getMatrix().light(False)                # 43
    time.sleep(3)

    matrix0.finish()                                # 44
    print('\nCase 0 Default(=single)-Test erfolgreich.\n')
    time.sleep(5)

    print("\nTest: Case 1 'square'\n")  # ============================================================================
    matrix1 = LEDmatrix('square')
    images1 = matrix1.getObjects()                  # 42

    i = 0
    while (i < len(images1)):
        print('\n%s-index-Nr. %d, Name: %s, Position: ' % (matrix1.getCase(), i, images1[i].getName()),
              images1[i].getMatrixPosition())       # 45, 39, 9
        i += 1

    time.sleep(2)
    matrix1.setBGcolor(255, 0, 255)                 # 41
    time.sleep(2)
    matrix1.setBGcolor(255, 255, 0)                 # 41
    time.sleep(2)
    matrix1.setBGcolor(0, 255, 255)                 # 41
    time.sleep(2)
    matrix1.setBGcolor(255, 255, 255)               # 41
    time.sleep(2)

    matrix1.getMatrix().light(False)                # 43
    time.sleep(3)

    matrix1.finish()                                # 44
    print('\nCase 1 square-Test erfolgreich.\n')
    time.sleep(5)

    print("Test: Case 2 'colorHeartrate'\n")  # ===================================================================
    matrix2 = LEDmatrix('colorHeartrate')
    images2 = matrix2.getObjects()                           # 42

    i = 0
    while (i < len(images2)):
        print('\n%s-index-Nr. %d, Name: %s, Position: ' % (matrix2.getCase(), i, images2[i].getName()),
              images2[i].getMatrixPosition())                # 45, 39, 9
        i += 1

    time.sleep(2)

    i = 0
    while (i < len(images2)):
        if (images2[i].getName() == 'bottomLeftImage'):      # 39
            images2[i].setPuls(30)                           # 36

        if (images2[i].getName() == 'bottom2ndLeftImage'):   # 39
            images2[i].setPuls(60)                           # 36

        if (images2[i].getName() == 'bottom3rdLeftImage'):   # 39
            images2[i].setPuls(120)                          # 36

        if (images2[i].getName() == 'bottom4thLeftImage'):   # 39
            images2[i].setPuls(180)                          # 36

        i += 1
        time.sleep(2)

    time.sleep(2)

    i = 0
    while (i < len(images2)):
        if (images2[i].getName() == 'bottomLeftImage'):      # 39
            images2[i].setLightOffImageColor(0, 255, 255)    # 15

        if (images2[i].getName() == 'bottom2ndLeftImage'):   # 39
            images2[i].setLightOffImageColor(255, 0, 255)    # 15

        if (images2[i].getName() == 'bottom3rdLeftImage'):   # 39
            images2[i].setLightOffImageColor(0, 100, 0)      # 15

        if (images2[i].getName() == 'bottom4thLeftImage'):   # 39
            images2[i].setLightOffImageColor(255, 255, 255)  # 15

        i += 1
        time.sleep(2)

    time.sleep(2)

    matrix2.getMatrix().light(False)                         # 43
    time.sleep(3)

    matrix2.finish()                                         # 44
    print('\nCase 2 colorHeartrate-Test erfolgreich.\n')
    time.sleep(5)

    print("\nTest: Case 3 'quarters4'\n")  # ===================================================================
    matrix3 = LEDmatrix('quarters4')
    images3 = matrix3.getObjects()                  # 42

    i = 0
    while (i < len(images3)):
        print('\n%s-index-Nr. %d, Name: %s, Position: ' % (matrix3.getCase(), i, images3[i].getName()),
              images3[i].getMatrixPosition())       # 45, 39, 9
        i += 1

    time.sleep(2)

    matrix3.getMatrix().light(False)                # 43
    time.sleep(3)

    matrix3.finish()                                # 44
    print('\nCase 3 quarters4-Test erfolgreich.\n')
    time.sleep(3)

    print("\nTest: Case 4 'row2'\n")  # ===================================================================
    matrix4 = LEDmatrix('row2')
    images4 = matrix4.getObjects()                  # 42

    i = 0
    while (i < len(images4)):
        print('\n%s-index-Nr. %d, Name: %s, Position: ' % (matrix4.getCase(), i, images4[i].getName()),
              images4[i].getMatrixPosition())       # 45, 39, 9
        i += 1

    time.sleep(2)

    matrix4.getMatrix().light(False)                # 43
    time.sleep(3)

    matrix4.finish()                                # 44
    print('\nCase 4 row2-Test erfolgreich.\n')
    time.sleep(5)

    print("\nTest: Case 5 'col2'\n")  # ===================================================================
    matrix5 = LEDmatrix('col2')
    images5 = matrix5.getObjects()                  # 42

    i = 0
    while (i < len(images5)):
        print('\n%s-index-Nr. %d, Name: %s, Position: ' % (matrix5.getCase(), i, images5[i].getName()),
              images5[i].getMatrixPosition())       # 45, 39, 9
        i += 1

    time.sleep(2)

    matrix5.getMatrix().light(False)                # 43
    time.sleep(3)

    matrix5.finish()                                # 44
    print('\nCase 5 col2-Test erfolgreich.\n')
    time.sleep(5)

    print("\nTest: Case 6 'single'\n")  # ===================================================================
    matrix6 = LEDmatrix('single')
    images6 = matrix6.getObjects()                  # 42

    i = 0
    while (i < len(images6)):
        print('\n%s-index-Nr. %d, Name: %s, Position: ' % (matrix6.getCase(), i, images6[i].getName()),
              images6[i].getMatrixPosition())       # 45, 39, 9
        i += 1

    time.sleep(2)

    matrix6.getMatrix().light(False)                # 43
    time.sleep(3)

    matrix6.finish()                                # 44
    print('\nCase 6 single-Test erfolgreich.\n')
    time.sleep(5)
