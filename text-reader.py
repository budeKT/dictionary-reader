import definitionretriever as define
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

    # initialize window. We create root as the "root" application/gui where we will do stuff in.
    rootHeight = int(screenH * heightPercent / 100)
    rootWidth = int(screenW * widthPercent / 100)
    root.geometry(str(rootWidth)+"x"+str(rootHeight))
    root.resizable(True, True)

    # Dictionary button
    searchButton = tkt.Button(root, text = "Test next window", command = lambda:openWindow(root, "Word Search"))
    searchButton.pack()

    # PDF reader button
    readerButton = tkt.Button(root, text = "PDF/Text Reader", command = lambda:openWindow(root, "Import file"))
    readerButton.pack()

    # Main menu logic for input
    # chosen = False
    # while chosen == False:
    #     print(" [1] Define a word \n", 
    #           "[2] Import a text file \n",
    #           "[0] Exit")
    #     choice = input("Enter your choice: ")

    #     if choice == "1":
    #         sendWord()
    #         chosen = True    

    #     elif choice == "2":
    #         fileIn = input("Enter file name: ") + ".txt"
    #         importFile(fileIn)
    #         chosen = True

    #     elif choice == "0":
    #         break

    #     else:
    #         print("Invalid input.")

    # gui loop
    root.mainloop() 


def openWindow(root, funcName):
    # Hides main GUI and creates new one
    root.withdraw()
    new_Window = tkt.Tk()
    new_Window.title("funcName")

    # Return back to main menu
    backButton = tkt.Button(new_Window, text = "Go Back", command = lambda:main())
    backButton.pack()
    
    # Need to figure out how to close this window if go back is pressed.

def sendWord():
    # Sends a given word to definitionretriever.py
    word = input("Enter a Word: ")
    define.main(word)

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


main()




