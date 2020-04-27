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
    triangle(pierwszalitera[0]-50, pierwszalitera[1]+d, pierwszalitera[0]+200, drugalitera[1]+d, (pierwszalitera[0]+pierwszalitera[0]+150)/2, pierwszalitera[1]-100) # trójkąt nie jest kształtem nie standardowym, ale zaliczę, bo go nie mieliśmy
   
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
    if keyCode == LEFT:
        shift = 1
    elif keyCode == RIGHT:
        shift = 1
    if key == litery[1].lower():
        pressedKey = 1  
def keyemitted():
    global shift
    global pressedKey
    if keycode == LEFT:
        shift = 0
    elif keycode == RIGHT:
        shift = 0
    if key == litery[1].lower():
        pressedKey = 0
 
 # ciekawe, oryginalne rozwiązanie; dało się znacznie prościej
 # chyba coś domieszałeś z referencji javy, zwróć uwagę, żeby były pythonowe i włączony mode do pythona w processingu
 # niestety się miesza, bo jest nie do końca przemyślane i przy przeskoczeniu na literę nie ma możliwości 'odznaczenia' i co więcej wtedy za najechanie na jedną podświetla się ta druga - też zamienia
 # 1,5p
 # po za nazwamizmiennych nawet kolory z Kockomacie identyczne, jeśli to się powtórzy nie zaliczę zadania
