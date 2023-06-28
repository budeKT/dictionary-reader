import definitionretriever as define
import keyboard as kbd
import tkinter as tkt
 
def main():
    # Loads in main menu for input selection
    chosen = False
    while chosen == False:
        print(" [1] Define a word \n", 
              "[2] Import a text file \n",
              "[0] Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            sendWord()
            chosen = True    

        elif choice == "2":
            fileIn = input("Enter file name: ") + ".txt"
            importFile(fileIn)
            chosen = True

        elif choice == "0":
            break

        else:
            print("Invalid input.")

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




