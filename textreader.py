import definitionretriever as define
from newWindow import Window
import keyboard as kbd
import tkinter as tkt
 
def main():
    root = tkt.Tk()
    root.title("PDF Dictionary Main Menu")

    # Calculate the aspect ratio of any given screen dimensions.
    # winfo_screenwidth obtains the width of the user's screen.
    screenW = root.winfo_screenwidth()
    screenH = root.winfo_screenheight()
    
    # Rescales the root window to take up a percentage of the user's screen.
    widthPercent = 20
    heightPercent = 15

    # Root GUI data
    rootHeight = int(screenH * heightPercent / 100)
    rootWidth = int(screenW * widthPercent / 100)
    xPos = int((screenW/2) - (rootWidth/2))
    yPos = int((screenH/2) - (rootHeight/2))
    windowGeo = f"+{xPos}+{yPos}"
    root.geometry(windowGeo)
    root.resizable(True, True)

    buttonHeight = 1
    buttonWidth = 12

    tkt.Label(text = "Welcome to PDF Dictionary!").grid(column = 1, row = 0)

    # Empty space so it looks better
    tkt.Label(text = " ").grid(column = 1, row = 2)
    tkt.Label(text = " ").grid(column = 1, row = 4)

    # Dictionary button
    searchButton = tkt.Button(root, height = buttonHeight, width = buttonWidth, 
                              text = "Define a word", 
                              command = lambda:openWindow(root, windowGeo, "Word Search"))
    searchButton.grid(column = 0, row = 3)

    # PDF reader button
    readerButton = tkt.Button(root, height = buttonHeight, width = buttonWidth, 
                              text = "PDF/Text Reader", 
                              command = lambda:openWindow(root, windowGeo, "Import file"))
    readerButton.grid(column = 1, row = 3)

    # Quit app button
    quitButton = tkt.Button(root, height = buttonHeight, width = buttonWidth, 
                            text = "Quit", 
                            command = root.quit)
    quitButton.grid(column = 2, row = 3)

    # gui loop
    root.mainloop() 


def openWindow(root, windowGeo, name):
    if name == "Word Search":
        wordInstance = tkt.Tk()
        searchWindow = Window(root, wordInstance, windowGeo, name)
        searchWindow.createWindow()

        backButton = tkt.Button(wordInstance, text = "Go Back", command = lambda:goBack(root, wordInstance))
        backButton.grid(column = 0, row = 0)

       
    elif name == "Import file":
        readerInstance = tkt.Tk()
        readerWindow = Window(root, readerInstance, windowGeo, name)
        readerWindow.createWindow()
        
        backButton = tkt.Button(readerInstance, text = "Go Back", command = lambda:goBack(root, readerInstance))
        backButton.grid(column = 0, row = 0)


def goBack(root, new_Window):
    new_Window.withdraw()
    root.deiconify()
    

def importFile(fileIn):
    # Checks if file exists (w/ exception handler)
    try:
        fileIn = open(fileIn, "r")
        line = list(fileIn.readlines())
        for i in range(len(line)):
            print(line[i])
        fileIn.close()
        loadFile(line)
    
    except FileNotFoundError:
       print("File does not exist. Please check for spelling and if it's in the working directory.")


def loadFile(line):
    # Loads up file into a tkinter label so user can highlight words.
    pass


def winClose(root):
    root.Destroy()

main()




