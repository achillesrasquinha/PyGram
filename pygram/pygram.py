import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

from pygram.config import PyGramConfig
from pygram.filters import nss

class PyGram(object):
    class Frame(tk.Frame):
        def __init__(self,
                     master       = None,
                     window_size  = (PyGramConfig.WINDOW_WIDTH, PyGramConfig.WINDOW_HEIGHT),
                     btngrid_size = (PyGramConfig.BTNGRID_ROWS, PyGramConfig.BTNGRID_COLS)):
            self.master       = master
            self.window_size  = window_size
            self.btngrid_size = btngrid_size

            tk.Frame.__init__(self, self.master)

            self.build_user_interface()

        def build_user_interface(self):
            self.menu     = tk.Menu(self.master)
            self.master.config(menu = self.menu)

            self.filemenu = tk.Menu(self.menu,
                                    tearoff = False)
            self.menu.add_cascade(label = 'File',
                                  menu  = self.filemenu)

            rows, cols       = self.btngrid_size

            self.image_panel = tk.Label(self.master,
                                        width  = self.window_size[0],
                                        height = self.window_size[0])
            self.image_panel.grid(row        = 0,
                                  column     = 0,
                                  columnspan = cols,
                                  sticky     = tk.E + tk.W)
            self.button = { }
            k           = 0
            size        = len(PyGramConfig.FILTERS)
            for i in range(rows):
                for j in range(cols):
                    if k < size:
                        f      = PyGramConfig.FILTERS[k]
                        text   = f['name']
                        button = tk.Button(self.master,
                                           text = text.capitalize())
                        button.grid(row    = i + 1,
                                    column = j,
                                    sticky = tk.N + tk.E + tk.W + tk.S)
                        self.button[text]  = button

                        k      = k + 1

    def __init__(self,
                 window_aspect_ratio = PyGramConfig.WINDOW_ASPECT_RATIO,
                 window_width        = PyGramConfig.WINDOW_WIDTH,
                 window_height       = PyGramConfig.WINDOW_HEIGHT,
                 btngrid_rows        = PyGramConfig.BTNGRID_ROWS,
                 btngrid_cols        = PyGramConfig.BTNGRID_COLS,
                 resizable           = False):
        self.window_size  = (int(window_width), int(window_height))
        self.btngrid_size = (btngrid_rows, btngrid_cols)
        self.root         = tk.Tk()
        self.root.title('{name} v{version}'.format(
            name    = PyGramConfig.NAME,
            version = PyGramConfig.VERSION
        ))
        self.root.geometry('{width}x{height}'.format(
            width   = window_width + 2,
            height  = window_height
        ))
        self.root.resizable(width  = resizable,
                            height = resizable)
        self.frame        = PyGram.Frame(self.root,
                                         window_size  = self.window_size,
                                         btngrid_size = self.btngrid_size)
        self.frame.filemenu.add_command(label   = 'Open File',
                                        command = self.on_open_file)

    def on_open_file(self):
        filetypes = PyGramConfig.ACCEPTED_FILES

        dialog    = filedialog.Open(self.frame, filetypes = filetypes)
        filename  = dialog.show()

        self.open_image(filename)

    def open_image(self, filename):
        if filename:
            self.image   = Image.open(filename)
            self.image   = PyGram.resize_image(self.image, self.window_size)
            self.convert = self.image
            self.update_image_panel(self.image)

            rows, cols   = self.btngrid_size
            k            = 0
            size         = len(PyGramConfig.FILTERS)
            for i in range(rows):
                for j in range(cols):
                    if k < size:
                        f        = PyGramConfig.FILTERS[k]
                        text     = f['name']
                        function = lambda command = f['command']: self.on_click_filter(command)
                        self.frame.button[text].config(command = function)
                        k      = k + 1

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

    def on_click_filter(self, command):
        self.convert = command(self.image)
        self.update_image_panel(self.convert)

    def update_image_panel(self, image):
        self.imagetk = ImageTk.PhotoImage(image)
        self.frame.image_panel.configure(image = self.imagetk)

    def run(self):
        self.open_image(PyGramConfig.DEFAULT_FILE)
        self.root.mainloop()
