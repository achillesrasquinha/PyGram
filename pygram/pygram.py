import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

from pygram.config import PyGramConfig
from pygram.filters import nss

class PyGram(object):
    class Frame(tk.Frame):
        def __init__(self,
                     master      = None,
                     window_size = (PyGramConfig.WINDOW_WIDTH, PyGramConfig.WINDOW_HEIGHT)):
            self.master      = master
            self.window_size = window_size
            tk.Frame.__init__(self, self.master)

            self.create_menu()
            self.create_image_panel()

        def create_menu(self):
            self.menu     = tk.Menu(self.master)
            self.master.config(menu = self.menu)

            self.filemenu = tk.Menu(self.menu,
                                    tearoff = False)
            self.menu.add_cascade(label = 'File',
                                  menu  = self.filemenu)

        def create_image_panel(self):
            size             = self.window_size[0]
            self.image_panel = tk.Label(self.master,
                                        width  = size,
                                        height = size)
            self.image_panel.grid(row        = 0,
                                  column     = 0,
                                  columnspan = PyGramConfig.BTNGRID_COLS,
                                  sticky     = tk.N + tk.E + tk.W + tk.S)

    def __init__(self,
                 window_aspect_ratio = PyGramConfig.WINDOW_ASPECT_RATIO,
                 window_width        = PyGramConfig.WINDOW_WIDTH,
                 window_height       = PyGramConfig.WINDOW_HEIGHT,
                 resizable           = False):
        self.window_size  = (int(window_width), int(window_height))
        self.root         = tk.Tk()
        self.root.title('{name} v{version}'.format(
            name    = PyGramConfig.NAME,
            version = PyGramConfig.VERSION
        ))
        self.root.geometry('{width}x{height}'.format(
            width   = window_width,
            height  = window_height
        ))
        self.root.resizable(width  = resizable,
                            height = resizable)
        self.frame        = PyGram.Frame(self.root, self.window_size)
        self.frame.filemenu.add_command(label   = 'Open File',
                                        command = self.on_open_file)

    def on_open_file(self):
        filetypes = PyGramConfig.ACCEPTED_FILES

        dialog    = filedialog.Open(self.frame, filetypes = filetypes)
        filename  = dialog.show()

        self.open_image(filename)

    def open_image(self, filename):
        if filename:
            self.image = Image.open(filename)
            self.image = PyGram.resize_image(self.image, self.window_size)
            self.update_image_panel(self.image)

    def resize_image(image, size):
        width, height = image.size
        aspect_ratio  = width / height

        if max(width, height) is width:
            width  = size[0]
            height = width  / aspect_ratio
        else:
            height = size[1]
            width  = height * aspect_ratio

        image.thumbnail((width, height), Image.ANTIALIAS)

        return image

    def update_image_panel(self, image):
        self.imagetk = ImageTk.PhotoImage(image)
        self.frame.image_panel.configure(image = self.imagetk)

    def run(self):
        self.open_image(PyGramConfig.DEFAULT_FILE)
        self.root.mainloop()
