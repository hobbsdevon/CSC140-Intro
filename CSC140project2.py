import cImage

img = cImage.Image("elliot.gif")
win = cImage.ImageWin("Elliot", img.getWidth(), img.getHeight())
img.draw(win)
isRunning = True



def red():
    img = cImage.Image("elliot.gif")

    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)
            newRed = 255 - p.getRed()
            newPixel = cImage.Pixel(newRed, p.getGreen(), p.getBlue())
            img.setPixel(col, row, newPixel)
    img.draw(win)

def green():
    img = cImage.Image("elliot.gif")

    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)
            newGreen = 255 - p.getGreen()
            newPixel = cImage.Pixel(p.getRed(), newGreen, p.getBlue())
            img.setPixel(col, row, newPixel)
    img.draw(win)

def blue():
    img = cImage.Image("elliot.gif")

    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)
            newBlue = 255 - p.getBlue()
            newPixel = cImage.Pixel(p.getRed(), p.getGreen(), newBlue)
            img.setPixel(col, row, newPixel)
    img.draw(win)

def negative():
    img = cImage.Image("elliot.gif")

    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)
            newRed = 255 - p.getRed()
            newGreen = 255 - p.getGreen()
            newBlue = 255 - p.getBlue()
            newPixel = cImage.Pixel(newRed, newGreen, newBlue)
            img.setPixel(col, row, newPixel)
    img.draw(win)


def gScale():
    img = cImage.Image("elliot.gif")

    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)
            newCol = int((p.getRed() + p.getGreen() + p.getBlue())/3)
            newPixel = cImage.Pixel(newCol, newCol, newCol)
            img.setPixel(col, row, newPixel)
    img.draw(win)
    

def sepia():
    img = cImage.Image("elliot.gif")

    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)
            newRed = int((.393*p.getRed()) + (.769*p.getGreen()) + (.189*p.getBlue()))
            newGreen = int((.349*p.getRed()) + (.686*p.getGreen()) + (.168*p.getBlue()))
            newBlue = int((.272*p.getRed()) + (.534*p.getGreen()) + (.131*p.getBlue()))
            if newRed > 255:
                newRed = 255
            elif newRed < 0:
                newRed = 0
            if newGreen > 255:
                newGreen = 255
            elif newGreen < 0:
                newGreen = 0
            if newBlue > 255:
                newBlue = 255
            elif newBlue < 0:
                newBlue = 0
            newPixel = cImage.Pixel(newRed, newGreen, newBlue)
            img.setPixel(col, row, newPixel)
    img.draw(win)

def select():
    function = input("What would you like to apply to your picture? 'r' for redwash, 'g' for greenwash,'b' for bluewash, 's' for sepia, 'n' for negative, or 'gs' for greyscale. Click to quit: ")
    if function == "r":
        red()
    elif function == "g":
        green()
    elif function == "b":
        blue()
    elif function == "s":
        sepia()
    elif function == "gs":
        gScale()
    elif function == "n":
        negative()
    elif function == "q":
        quit()


while isRunning:
    select()
    





    
