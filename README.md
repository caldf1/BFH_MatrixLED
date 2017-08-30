# BFH_MatrixLED

Files mit den Eigenschaften der Matrix und der Bilder:
* _matrixProperties.py_
* _imageProperties.py_

Für die Initialisierung der LED-Matrix wird _LEDmatrix_2308_init.py_ benötigt.

Dieses File enthält die Klasse __LEDmatrix__, damit wird die Verbindung Matrix hergestellt, 
in der Sekunde werden 50 Bilder an die Matrix übermittelt (Frame duration = 20 ms).

Für die Manipulation der Bilder dient das File _MoveableLEDMatrix_2308.py_.

Dieses enthält die Klasse __MoveableLEDMatrix__, welche eine Instanz von __LEDmatrix__ erstellt.
Für die Bildbewegung stehen folgende Methoden zur Verfügung:
* startMove()
* waiting()
* stopMove()
* moveRight()
* moveLeft()
* stopMovingHorizontal()
* moveUp()
* moveDown()
* stopMovingVertical

Weitere Methoden:
* reset()
* connect()
* finish()
* lightOff()
* lightOn()


Für den farbigen Puls gibt es die _heartrate4_LEDmatrix_2908.py_ mit einem Schriftzug und 4 Herzen.
Folgende Methoden stehen zur Verfügung:
* finish()
* setHeartrate(heartNumber, rate)  -> heartNumber von 1 bis 4
* getHeartrate()
