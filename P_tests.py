
HOST = "localhost"
PORT = 4223
UID = "wVj" # Change XYZ to the UID of your LED Strip Bricklet

def clearAll():

    r = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    g = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    i = 0
    a = 0
    while i < 20:
        ls.set_rgb_values(a, 10, r, g, b)
        a += 10;
        i += 1



        
#r = RepeatingTimer(0.5, myFunction, "hello").
#r.start();
#sleep(2);
#r.interval = 0.05;
#sleep(2);
#r.stop(). """ def __init__(self,interval, function, *args, **kwargs):

res = [170, 190, 199, 200] # 198 199 200  1  -> 0 = 200
res[0] =  ((res[0] +10 ) % 200) # 2       2 / 4 0 r2 5   0, 2
res[1] =  ((res[1] +10 ) % 200) # 3       3 / 4 0 r3 5   0, 3
res[2] =  ((res[2] +10 ) % 200) # 4       4 / 4 1 r0 5   0, 4
res[3] =  ((res[3] +10 ) % 200) # 5 -> 1  5 / 4 1 r1 5   1, 0
#print(res)


res = [1, 2, 199, 200] # 198 199 200  1  -> 0 = 200
res[0] =  ((res[0] -10 ) % 200) # 2       2 / 4 0 r2 5   0, 2
res[1] =  ((res[1] -10 ) % 200) # 3       3 / 4 0 r3 5   0, 3
res[2] =  ((res[2] -10 ) % 200) # 4       4 / 4 1 r0 5   0, 4
res[3] =  ((res[3] -10 ) % 200) # 5 -> 1  5 / 4 1 r1 5   1, 0
#print(res)

x = 0
if x == 0:
    x = 200

def calculate(arr, move)
    res = arr
    z = move
    i = 0
    while i < len(res):
        k = ((res[i] + z) % 200)
        if k == 0:
            res[i] = 200
        else:
            res[i] = k


xMatrix = 19 # 0-19
yMatrix = 9  # 0-9
xRGB = 0     # 0-9
yRGB = 0     # 0-19

    # Iteration Matrix von [9][19] (unten rechts) nach [0][0] (oben links)
    # Iteration RGB von [0][0] (oben links) nach [19][9] (unten rechts)

while xMatrix > -1:
    print("rgb[yRGB][xRGB], matrix[yMatrix][xMatrix]")
    if xMatrix %2 == 1: # wenn x der Matrix ungerade, dann y von 9 bis 0 herausholen
        yMatrix = 9
        while yMatrix > -1:
            #print("rgb[yRGB][xRGB], matrix[yMatrix][xMatrix]")
            yMatrix -= 1
            xRGB += 1
        xRGB = 0
        xMatrix += 1
        yRGB += 1

    else:            # wenn x der Matrix gerade, dann y von 0 bis 9 herausholen
        yMatrix = 0
        while yMatrix < 10:
            #print("rgb[yRGB][xRGB], matrix[yMatrix][xMatrix]")
            yMatrix += 1
            xRGB += 1
        xRGB = 0
        xMatrix += 1
        yRGB += 1

        
    
    
