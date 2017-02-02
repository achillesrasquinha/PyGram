import os

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

from pygram.config import PyGramConfig
from pygram.filters import grayscale

class PyGram(object):
    SIZE_WINDOW           = (320, 480)
    SIZE_IMAGE_PANEL      = (320, 320)
    SIZE_BUTTON_GRID      = (1, 3)
    ACCEPTED_FILE_TYPES   = [ ]
    FILTERS               = [
        {
            'name': 'normal',
            'command': lambda image: image
        },
        {
            'name': 'grayscale',
            'command': grayscale
        },
        {
            'name': 'inkwell',
            'command': lambda image: image
        }
    ]
    # inheritance from tk.Frame object
    # descendent class of PyGram
    class Frame(tk.Frame):
        '''
            Creates a new PyGram.Frame object

            Parameters:
                root (tk.Tk) - the root frame of the app
        '''
        def __init__(self, master = None):
            self.master = master

            # calls inherited class's constructor
            tk.Frame.__init__(self, self.master)
            self.createFrame()

        def createFrame(self):
            self.menu       = tk.Menu(self.master)
            self.master.config(menu = self.menu)

            self.filemenu   = tk.Menu(self.menu,
                                      tearoff = False)
            self.menu.add_cascade(label = 'File',
                                  menu  = self.filemenu)

            width, height   = PyGram.SIZE_IMAGE_PANEL
            self.imagePanel = tk.Label(self.master,
                                       width  = width,
                                       height = height)
            rows, cols      = PyGram.SIZE_BUTTON_GRID
            self.imagePanel.grid(row        = 0,
                                 column     = 0,
                                 columnspan = cols)

            self.buttons    = list()
            k               = 0
            for i in range(rows):
                self.buttons.append(list())
                for j in range(cols):
                    f      = PyGram.FILTERS[k]
                    name   = f['name'].capitalize()
                    button = tk.Button(self.master,
                                       text = name)
                    button.grid(row    = i + 1,
                                column = j,
                                sticky = tk.N + tk.E + tk.W + tk.S)

                    self.buttons[i].append(button)

                    k      = k + 1

    def __init__(self):
        # creates a Tk object, instantized only once
        width, height = PyGram.SIZE_WINDOW

        self.root     = tk.Tk()
        self.root.title(PyGramConfig.NAME)
        self.root.geometry('{width}x{height}'.format(
            width  = width,
            height = height
        ))
        self.root.resizable(width  = False,
                            height = False)

        self.frame = PyGram.Frame(self.root)
        self.frame.filemenu.add_command(label = 'Open File', command = self.onOpenFile)

    def onOpenFile(self):
        filetypes = PyGram.ACCEPTED_FILE_TYPES

        dialog    = filedialog.Open(self.frame, filetypes = filetypes)
        filename  = dialog.show()

        if filename:
            self.image   = Image.open(filename)
            self.image   = PyGram.resize(self.image, PyGram.SIZE_IMAGE_PANEL)
            self.imagetk = ImageTk.PhotoImage(self.image)

            self.frame.imagePanel.configure(image = self.imagetk)

            rows, cols   = PyGram.SIZE_BUTTON_GRID
            k            = 0
            for i in range(rows):
                for j in range(cols):
                    f       = PyGram.FILTERS[k]
                    command = f['command']
                    self.frame.buttons[i][j].config(command = lambda command = command: self.onClick(command))
                    k    = k + 1

            self.convert  = self.image

    def resize(image, size):
        w, h    = image.size
        ratio   = w / h
        maximum = max(w, h)

        if maximum is w:
            width  = size[0]
            height = width / ratio
        else:
            height = size[1]
            width  = height * ratio

        image.thumbnail((width, height), Image.ANTIALIAS)

        return image

    def onClick(self, filter):
        self.convert = filter(self.image)
        self.imagetk = ImageTk.PhotoImage(self.convert)
        self.frame.imagePanel.configure(image = self.imagetk)

    def run(self):
        # starts Tkinter's main thread
        self.root.mainloop()
