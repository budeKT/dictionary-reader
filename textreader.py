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

    # GUI loop
    root.mainloop() 


# openWindow() Creates a new window based on which button is pressed on the main menu. See main() for which buttons are being made.
# Checks to see if the button pressed contains a specific name ('Word search' or 'Import File') and launches a new window based on that info.
# Each window has different features. Word search is to define a single word only, while Import File will be used as a PDF reader.
def openWindow(root, windowGeo, name):
    if name == "Word Search":
        wordInstance = tkt.Tk()
        searchWindow = Window(root, wordInstance, windowGeo, name)
        searchWindow.createWindow()
        
        tkt.Label(wordInstance, text = "Enter a word to define.").grid(column = 1, row = 0)
        wordLabel = tkt.Label(wordInstance, text = " ")
        wordLabel.grid(column = 1, row = 1)

        wordInput = tkt.Text(wordInstance,
                            height = 1,
                            width = 25)
        wordInput.grid(column = 1, row = 2)

        enterButton = tkt.Button(wordInstance, text = "Enter", command = lambda:enterWord(wordInstance, wordInput, wordLabel))
        enterButton.grid(column = 1, row = 3)

        backButton = tkt.Button(wordInstance, text = "Go Back", command = lambda:goBack(root, wordInstance))
        backButton.grid(column = 1, row = 4)

    # Creates a new window for the PDF reader 
    elif name == "Import file":
        readerInstance = tkt.Tk()
        readerWindow = Window(root, readerInstance, windowGeo, name)
        readerWindow.createWindow()
        tkt.Label(readerInstance, text = "Enter directory of file: ").grid(column = 1, row = 1)
        

        dirInput = tkt.Text(readerInstance,
                                  height = 1,
                                  width = 30)
        dirInput.grid(column = 1, row =2)
        directory = dirInput.get(1.0, "end-1c")
        importButton = tkt.Button(readerInstance, text = "Import File", command = lambda:importFile(directory))
        importButton.grid(column = 1, row = 3)
        

        fileText = tkt.Text(readerInstance,
                            height = 30,
                            width = 35)
        fileText.grid(column = 1, row = 4)
        fileText.insert("1.0", "Please enter directory of a text file in order to read.")

        enterButton = tkt.Button(readerInstance, text = "Enter", command = lambda:enterWord(readerInstance, wordInput, wordLabel))
        enterButton.grid(column = 1, row = 5)
        
        backButton = tkt.Button(readerInstance, text = "Go Back", command = lambda:goBack(root, readerInstance))
        backButton.grid(column = 1, row = 6)

        
def goBack(root, new_Window):
    new_Window.withdraw()
    root.deiconify()
    
# enterWord() will take the word that the user inputs into the textbox and stores it in a variable.
# It will then send the word to definitionretriever.py so it can be requested from the Dictionary API.
def enterWord(windowInstance, wordInput, wordLabel):
    # Stores user input
    userWord = wordInput.get(1.0, "end-1c")
    wordLabel.config(text = " ")

    # Retrieve definition
    if " " in userWord:
        wordLabel = tkt.config(text = "Invalid word! Please enter a single word to define.")
        
    else:
        # Displays user input
        wordDefinition = define.main(userWord)
        wordLabel.config(text = f"Definition of {userWord}: {wordDefinition}")


# importFile() Will import the file and checks if file exists (w/ exception handler)
def importFile(fileIn):
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




