# -*- coding: utf-8 -*-
# Define imports
import tkinter as tk
from tkinter.scrolledtext import *


class ManualPage(tk.Frame):
    """ Manual page class """
    def create_hint_label(self, text, pos):
        label = tk.Label(self.upper_frame, text=text,
                         background='white',
                         foreground="black").grid(row=pos, column=0,
                                                  sticky=tk.W)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        # Define main frame
        self.main_frame = tk.Frame(self, background='white')
        self.main_frame.pack(expand=1)
        self.main_frame.pack()
        # Define manual frame
        self.upper_frame = tk.Frame(self.main_frame, width=300, height=50,
                                    background='black')
        self.upper_frame.grid(column=0, row=0)
        strings = ['\n List of shortcuts:',
                   '\n Ctrl + A: Select all text elements in the text box',
                   '\n Ctrl + C : Copy text from the text box',
                   '\n Ctrl + V : Paste text from the text box',
                   '\n Ctrl + X : Cut the text elements from text box',
                   '\n Ctrl + O : open new file',
                   '\n Ctrl + S : save file',
                   '\n Ctrl + Alt + S : save file as']
        # Define labels
        self.create_hint_label(strings[0], 0)
        self.create_hint_label(strings[1], 1)
        self.create_hint_label(strings[2], 4)
        self.create_hint_label(strings[3], 3)
        self.create_hint_label(strings[4], 2)
        self.create_hint_label(strings[5], 6)
        self.create_hint_label(strings[6], 7)
        self.create_hint_label(strings[7], 5)
        # Define upper frame
        upper_frame = tk.Frame(self.main_frame, width=300, height=50,
                               background='white')
        upper_frame.grid(column=0, row=1)
        # Define label
        exit_string = (
                       "\n\n *If no key input is given, the following key"
                       " is 0123456789abcdef\n"
                       "*The save feature is used to save the hash/ "
                       "ciphered text to a txt file"
                      )
        exit_label = tk.Label(upper_frame, text=exit_string,
                              background='white', foreground="black")
        exit_label.pack(side="top", fill="x", pady=10)
        # Define middle frame
        self.middle_frame = tk.Frame(self.main_frame, background='grey',
                                     width=300, height=50)
        self.middle_frame.grid(column=0, row=2)
        # Define lower frame
        lower_frame = tk.Frame(self.main_frame, background='grey',
                               width=300, height=50)
        lower_frame.grid(column=0, row=3)
        # Define cancel button
        back_button = tk.Button(lower_frame, text="Go back",
                                command=lambda: controller.show_frame("PageOne"))
        back_button.pack(side=tk.RIGHT)
        # Configure the buttons
        back_button.configure(background='white', foreground='black',
                              activebackground='#0080ff',
                              activeforeground='white')
