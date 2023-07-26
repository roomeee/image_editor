import customtkinter as ctk
from settings import *
from panels import *

class Menu(ctk.CTkTabview):
    def __init__(self, parent, pos_vars, color_vars, effect_vars):
        super().__init__(master=parent)
        self.grid(row=0, column=0, sticky='nsew', pady=10, padx=10)

        self.add('Position', )
        self.add('Effects')
        self.add('Color')
        self.add('Export')
        PositionFrame(self.tab('Position'), pos_vars)
        EffectFrame(self.tab('Effects'),effect_vars)
        ColorFrame(self.tab('Color'), color_vars)


class PositionFrame(ctk.CTkFrame):
    def __init__(self, parent, pos_vars):
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand=True, fill='both')
        Slider(self, 'Rotation', pos_vars['rotate'],0,360)
        Slider(self, 'Zoom', pos_vars['zoom'],0,200)
        SegmentedPanel(self,'Invert' ,pos_vars['flip'], FLIP_OPTIONS)


class EffectFrame(ctk.CTkFrame):
    def __init__(self, parent,effect_vars):
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand=True, fill='both')
        DropDownPanel(self, effect_vars['effect'],EFFECT_OPTIONS)
        Slider(self, 'Blur', effect_vars['blur'], 0, 3)
        Slider(self, 'Contrast', effect_vars['contrast'], 0, 10)


class ColorFrame(ctk.CTkFrame):
    def __init__(self, parent, color_vars):
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand=True, fill='both')

        SwitchPanel(self, (color_vars['grayscale'], 'B/W'),(color_vars['invert'], 'Invert'))
        Slider(self, 'Brightness', color_vars['brightness'],0,5)
        Slider(self, 'vibrance', color_vars['vibrance'],0,5)



class ExportFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand=True, fill='both')
