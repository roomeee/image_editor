import customtkinter as ctk
from tkinter import filedialog, Canvas
from settings import *

BLUE = '#7455ed'


class ImageImport(ctk.CTkFrame):
    def __init__(self, parent, import_func):
        super().__init__(master=parent)
        self.grid(column=0, columnspan=2, row=0, sticky='nsew')
        self.import_func = import_func
        ctk.CTkLabel(self, text='Image Editor',
                     font=("Arial", 40, 'bold')).pack(pady=10)
        ctk.CTkButton(self, text='open image', fg_color=BLUE, command=self.open_dialog).pack(expand=True)

    def open_dialog(self):
        path = filedialog.askopenfile().name
        self.import_func(path)


class ImageOutput(Canvas):
    def __init__(self, parent, resize_image):
        super().__init__(master=parent, background='#242424', bd=0, highlightthickness=0, relief='ridge')
        self.grid(row=0, column=1, sticky='nsew',padx=10,pady=10)
        self.bind('<Configure>', resize_image)


class CloseOutput(ctk.CTkButton):
    def __init__(self, parent, close_func):
        super().__init__(master=parent,
                         command= close_func,
                         text='x',
                         text_color=WHITE,
                         fg_color='transparent',
                         width=40,
                         height=40,
                         corner_radius=0,
                         hover_color=RED)
        self.place(relx=0.99, rely=0.01, anchor='ne')
