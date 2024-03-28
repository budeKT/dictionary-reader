import tkinter as tkt

class Window:
    def __init__(self, root, instance, geometry, name):
        self.root = root
        self.instance = instance
        self.geometry = geometry
        self.name = name

    def createWindow(self):
        self.root.withdraw()
        self.instance.title(self.name)
        self.instance.geometry(self.geometry)

