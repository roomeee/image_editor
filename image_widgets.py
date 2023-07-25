import customtkinter as ctk
BLUE = '#7455ed'

class ImageImport(ctk.CTkFrame):
    def __init__(self, parent, impott_func):
        super().__init__(master=parent)
        self.grid(column=0, columnspan=2, row=0, sticky='nsew')
        ctk.CTkButton(self, text='open image', fg_color=BLUE).pack(expand=True)
