# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
from tkinter.scrolledtext import *


class StartPage(tk.Frame):
    """ Start page class """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')

        label = tk.Label(self, text='\n\n\n\n\nWelcome to Texthidder!\n\n'
                                    'It is a simple, beginner friendly'
                                    'encrypter and hasher written in '
                                    'python\n It provides AES-128 '
                                    'encryption and decryption alongside '
                                    'with SHA-256 hashing\n',
                         bg='white', fg="black")
        label.pack(side="top", fill="x", pady=10)
        self.FrameX = tk.Frame(self, bg='white')
        frame1 = tk.Frame(self.FrameX, width=300, height=50)
        frame1.grid(column=0, row=0)
        self.text = tk.Label(frame1,
                             text='\nDeveloped by 20DCE115 , 20DCE118 , 20DCE133 \n',
                             bg='white',
                             fg='black',
                             font=('Monospace', 10))
        self.text.pack()
        frame2 = tk.Frame(self.FrameX, bg='white', width=300, height=50)
        frame2.grid(column=0, row=1)
        frame3 = tk.Frame(self.FrameX, bg='white', width=300, height=50)
        frame3.grid(column=0, row=2)
        self.FrameX.pack()
        button1 = tk.Button(frame3, text="Exit",
                            command=lambda: controller.show_frame("ExitPage"))
        button1.pack(side=tk.RIGHT)
        button2 = tk.Button(frame3, text="Start",
                            command=lambda: controller.show_frame("PageOne"))
        button2.pack(side=tk.RIGHT, padx=5, pady=5)
        button1.configure(background="white", foreground='black',
                          activebackground='black',
                          activeforeground='black')
        button2.configure(background="white", foreground='black',
                          activebackground='black',
                          activeforeground='black')
