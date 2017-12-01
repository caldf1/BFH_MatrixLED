from LEDmatrix_split_merge_171110 import *
import imageProperties
import time


if __name__ == "__main__":

    print("\nBildtests: Images von imageProperties  \n")  # ===========================================================
    matrix = LEDmatrix()
    images = matrix.getObjects()
    imageObj = images[0]
    
    print('defaultImage: Spalten (x) = %d | Zeilen (y) = %d\n' % (
        len(imageProperties.defaultImage), len(imageProperties.defaultImage[0])))
    imageObj.setInputImage(imageProperties.defaultImage)
    time.sleep(2)

    print(
        'hello: Spalten (x) = %d | Zeilen (y) = %d\n' % (len(imageProperties.hello), len(imageProperties.hello[0])))
    imageObj.setInputImage(imageProperties.hello)
    time.sleep(2)

    print(
        'hearts1: Spalten (x) = %d | Zeilen (y) = %d\n' % (
            len(imageProperties.hearts1), len(imageProperties.hearts1[0])))
    imageObj.setInputImage(imageProperties.hearts1)
    time.sleep(2)

    print(
        'forms1: Spalten (x) = %d | Zeilen (y) = %d\n' % (len(imageProperties.forms1), len(imageProperties.forms1[0])))
    imageObj.setInputImage(imageProperties.forms1)
    time.sleep(2)

    print(
        'legoface: Spalten (x) = %d | Zeilen (y) = %d\n' % (
            len(imageProperties.legoface), len(imageProperties.legoface[0])))
    imageObj.setInputImage(imageProperties.legoface)
    time.sleep(2)

    print(
        'hiOli: Spalten (x) = %d | Zeilen (y) = %d\n' % (len(imageProperties.hiOli), len(imageProperties.hiOli[0])))
    imageObj.setInputImage(imageProperties.hiOli)
    time.sleep(2)

    print(
        'subsets: Spalten (x) = %d | Zeilen (y) = %d\n' % (
            len(imageProperties.subsets), len(imageProperties.subsets[0])))
    imageObj.setInputImage(imageProperties.subsets)
    time.sleep(2)

    print(
        'heartblue: Spalten (x) = %d | Zeilen (y) = %d\n' % (
            len(imageProperties.heartblue), len(imageProperties.heartblue[0])))
    imageObj.setInputImage(imageProperties.heartblue)
    time.sleep(2)

    print(
        'heartred: Spalten (x) = %d | Zeilen (y) = %d\n' % (
            len(imageProperties.heartred), len(imageProperties.heartred[0])))
    imageObj.setInputImage(imageProperties.heartred)
    time.sleep(2)

    print(
        'heartgreen: Spalten (x) = %d | Zeilen (y) = %d\n' % (
            len(imageProperties.heartgreen), len(imageProperties.heartgreen[0])))
    imageObj.setInputImage(imageProperties.heartgreen)
    time.sleep(2)

    print(
        'heartyellow: Spalten (x) = %d | Zeilen (y) = %d\n' % (
            len(imageProperties.heartyellow), len(imageProperties.heartyellow[0])))
    imageObj.setInputImage(imageProperties.heartyellow)
    time.sleep(2)

    print(
        'pulstext: Spalten (x) = %d | Zeilen (y) = %d\n' % (
            len(imageProperties.pulstext), len(imageProperties.pulstext[0])))
    imageObj.setInputImage(imageProperties.pulstext)
    time.sleep(2)

    print(
        'hochformat: Spalten (x) = %d | Zeilen (y) = %d\n' % (
            len(imageProperties.hochformat), len(imageProperties.hochformat[0])))
    imageObj.setInputImage(imageProperties.hochformat)
    time.sleep(2)

    print(
        'querformat: Spalten (x) = %d | Zeilen (y) = %d\n' % (
            len(imageProperties.querformat), len(imageProperties.querformat[0])))
    imageObj.setInputImage(imageProperties.querformat)
    time.sleep(2)

    print(
        'bild11Zeilen: Spalten (x) = %d | Zeilen (y) = %d\n' % (
            len(imageProperties.bild11Zeilen), len(imageProperties.bild11Zeilen[0])))
    imageObj.setInputImage(imageProperties.bild11Zeilen)
    time.sleep(2)

    print(
        'b11z: Spalten (x) = %d | Zeilen (y) = %d\n' % (len(imageProperties.b11z), len(imageProperties.b11z[0])))
    imageObj.setInputImage(imageProperties.b11z)
    time.sleep(2)

    print(
        'whiteLine: Spalten (x) = %d | Zeilen (y) = %d\n' % (
            len(imageProperties.whiteLine), len(imageProperties.whiteLine[0])))
    imageObj.setInputImage(imageProperties.whiteLine)
    time.sleep(2)

    print(
        'testImage: Spalten (x) = %d | Zeilen (y) = %d\n' % (
            len(imageProperties.testImage), len(imageProperties.testImage[0])))
    imageObj.setInputImage(imageProperties.testImage)
    time.sleep(2)

    matrix.getMatrix().light(False)
    time.sleep(3)
    matrix.finish()
    print('\nBildtests-Test erfolgreich.\n')
    time.sleep(5)
