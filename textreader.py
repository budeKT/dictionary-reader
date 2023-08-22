import definitionretriever as define
from newWindow import Window
import keyboard as kbd
import tkinter as tkt
from tkinter import messagebox
 
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

        exampleLabel = tkt.Label(wordInstance, text = "Example: ")
        exampleLabel.grid(column = 1, row = 2)

        wordInput = tkt.Text(wordInstance,
                            height = 1,
                            width = 25)
        wordInput.grid(column = 1, row = 3)

        enterButton = tkt.Button(wordInstance, text = "Enter", command = lambda:getWord(wordInput, wordLabel, exampleLabel))
        enterButton.grid(column = 1, row = 4)

        backButton = tkt.Button(wordInstance, text = "Go Back", command = lambda:goBack(root, wordInstance))
        backButton.grid(column = 1, row = 5)

    # Creates a new window for the PDF reader 
    elif name == "Import file":
        # Create the window
        readerInstance = tkt.Tk()
        readerWindow = Window(root, readerInstance, windowGeo, name)
        readerWindow.createWindow()
        tkt.Label(readerInstance, text = "Enter directory of file: ").grid(column = 1, row = 1)

        # create a label with left alignment
        wordLabel = tkt.Label(readerInstance, text = "Definitions listed here")
        wordLabel.grid(column = 1, row = 4)

        exampleLabel = tkt.Label(readerInstance, text = "Example: ")
        exampleLabel.grid(column = 1, row = 5)

        # Create textboxes in the window
        fileIn = tkt.Text(readerInstance,
                                  height = 1,
                                  width = 30)
        fileIn.grid(column = 1, row =2)
        directory = fileIn.get(1.0, "end-1c")

        fileText = tkt.Text(readerInstance,
                            height = 30,
                            width = 70,
                            wrap = tkt.WORD,
                            undo = True)
            
        fileText.grid(column = 1, row = 8)
        fileText.insert("1.0", "Please enter directory of a text file in order to read.")
        fileText.bind("<<Selection>>",lambda selectedTest: fileSelectedText(fileText))

        index = 0
         # Create buttons in the window
        importButton = tkt.Button(readerInstance, text = "Import File", command = lambda:importFile(readerInstance, fileIn, fileText))
        importButton.grid(column = 1, row = 3)

        nextButton = tkt.Button(readerInstance, text = "Next Definition", command = lambda:defFind(wordInput = fileSelectedText(fileText), wordLabel = wordLabel, exampleLabel = exampleLabel, name = "Next", index = index))
        nextButton.grid(column = 1, row = 6)

        prevButton = tkt.Button(readerInstance, text = "Prev Definition", command = lambda:defFind(wordInput = fileSelectedText(fileText), wordLabel = wordLabel, exampleLabel = exampleLabel, name = "Prev", index = index))
        prevButton.grid(column = 1, row = 7)

        searchButton = tkt.Button(readerInstance, text = "Search", command = lambda:defFind(wordInput = fileSelectedText(fileText), wordLabel = wordLabel, exampleLabel = exampleLabel, name = "Search", index = index))
        searchButton.grid(column = 1, row = 9)
        
        backButton = tkt.Button(readerInstance, text = "Go Back", command = lambda:goBack(root, readerInstance))
        backButton.grid(column = 1, row = 10)

        
def goBack(root, new_Window):
    new_Window.withdraw()
    root.deiconify()
    
# enterWord() will take the word that the user inputs into the textbox and stores it in a variable.
# It will then send the word to definitionretriever.py so it can be requested from the Dictionary API.
def getWord(wordInput, wordLabel, exampleLabel):
    # Stores user input
    userWord = wordInput.get(1.0, "end-1c")
    wordLabel.config(text = " ")
    if " " in userWord.strip():
        wordLabel.config(text = "Invalid word. Please enter a single word to define.")
    
    else:
        defFind(userWord, wordLabel, exampleLabel)


# importFile() Will import the file and checks if file exists (w/ exception handler)
def importFile(Instance, fileIn, fileText):
    
    try:
        fileText.delete("1.0", tkt.END)
        fileIn = open(fileIn.get(1.0, "end-1c"), "r")
        line = list(fileIn.readlines())
        for i in range(len(line)):
            # Fixes unicode errors (e.g, â€™ instead of ')
            textEncode = line[i].encode('cp1252')
            textDecode = textEncode.decode('utf-8')
            line.pop(i)
            line.insert(i, textDecode)
            fileText.insert(tkt.END, line[i])
        fileIn.close()
        
        
    except FileNotFoundError:
       message = "File could not be found. Please check for spelling."
       return message

    
def fileSelectedText(textbox):
    #if there is any text
    if textbox.tag_ranges("sel"):
        selectedText = textbox.get("sel.first", "sel.last")
        if selectedText:
            return selectedText
def defFind(wordInput, wordLabel, exampleLabel, name, index):
    if " " in wordInput.strip():
        wordLabel.config(text = "Invalid word! Please enter a single word to define.")
    elif name == "Next":
        index += 1
        partOfSpeech, definitions, example = define.main(wordInput)
        wordLabel.config(text = f"Definition of {wordInput}, {partOfSpeech[index]}: {definitions[index]}")
        exampleLabel.config(text = f"Example: {example[index]}")
        return index
    elif name == "Prev":
        index -= 1
        partOfSpeech, definitions, example = define.main(wordInput)
        wordLabel.config(text = f"Definition of {wordInput}, {partOfSpeech[index]}: {definitions[index]}")
        exampleLabel.config(text = f"Example: {example[index]}")
        return index
    else:
        partOfSpeech, definitions, example = define.main(wordInput)
        wordLabel.config(text = f"Definition of {wordInput}, {partOfSpeech[index]}: {definitions[index]}")
        exampleLabel.config(text = f"Example: {example[index]}")

def winClose(root):
    root.Destroy()

main()




