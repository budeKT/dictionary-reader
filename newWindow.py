import tkinter as tkt

class Window:
    def __init__(self, root, geometry, name):
        self.root = root
        self.geometry = geometry
        self.name = name
    
    def createWindow(self):
        self.root.withdraw()
        self.instance = tkt.Tk()
        self.instance.title(self.name)
        self.instance.geometry(self.geometry)
    
