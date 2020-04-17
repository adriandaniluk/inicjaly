def setup():
    global pierwszalitera
    global drugalitera
    global d
    global shift
    global litery
    global kolory
    global pressedKey
    size(500,600)
    pierwszalitera = [width/2, height/2]
    drugalitera = [width/2 + 30, height/2]
    d = 100
    shift = 0
    litery = ["A", "D"]
    kolory = ["#423C40", "#79BFA1"]
    pressedKey = 0
    textSize(d)
    noFill()
    stroke("#79BFA1")
    triangle(pierwszalitera[0]-50, pierwszalitera[1]+d, pierwszalitera[0]+200, drugalitera[1]+d, (pierwszalitera[0]+pierwszalitera[0]+150)/2, pierwszalitera[1]-100)
   
def draw():
    x = mouseLetter(pierwszalitera[0], pierwszalitera[1])
    y = pressedKey
    if shift == 1:
        a = x
        x = y
        y = a
    fill(kolory[x])
    text(litery[0], pierwszalitera[0], pierwszalitera[1] + 90)
    fill(kolory[y])
    text(litery[1], drugalitera[0] + 45, drugalitera[1] + 90)
   
def mouseLetter(xPos, yPos):
    if mouseX >= xPos:
        if mouseX <= xPos + d/2:
            if mouseY >= yPos:
                if mouseY <= yPos + d:
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    else:
        return 0
 
def keyPressed():
    global shift
    global pressedKey
    if keycore == LEFT:
        shift = 1
    elif keycore == RIGHT:
        shift = 1
    if key == słowa[1].lower():
        pressedKey = 1  
def keyemitted():
    global shift
    global pressedKey
    if keycore == LEFT:
        shift = 0
    elif keycore == RIGHT:
        shift = 0
    if key == słowa[1].lower():
        pressedKey = 0
 
