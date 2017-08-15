
xMatrix = 19 # 0-19
yMatrix = 0  # 0-9
xRGB = 0     # 0-9
yRGB = 0     # 0-19

# Iteration Matrix von [9][19] (unten rechts) nach [0][0] (oben links)
# Iteration RGB von [0][0] (oben links) nach [19][9] (unten rechts)

while xMatrix > -1:
    if xMatrix %2 == 1:
        yMatrix = 9
        while yMatrix > -1:
            print("rgb[",yRGB ,"][",xRGB,"], matrix[",yMatrix,"][",xMatrix,"]")
            xRGB += 1
            yMatrix -= 1
        xRGB = 0

    else:
        yMatrix = 0
        #if x %2 == 1: # wenn x der Matrix ungerade, dann y von 9 bis 0 herausholen
        while yMatrix < 10:
            print("rgb[",yRGB ,"][",xRGB,"], matrix[",yMatrix,"][",xMatrix,"]")
            xRGB += 1
            yMatrix += 1
        xRGB = 0
    xMatrix -= 1
    yRGB += 1
        

        
    
    
