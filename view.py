import tkinter as tk
from tkinter import *
from turtle import Screen


# Superclass for Views
class TheView:

    def show_greetings(self):
        pass

    def input_command(self):
        pass


# 1. Interactive front end for the console
class ConsoleView(TheView):

    def show_greetings(self):
        print("Welcome to Console Interface")

    def input_command(self):
        command = input('\nCommand:')
        return command


# 2. Interactive GUI
class TkinterView(TheView):
    def __init__(self):
        self.window = tk.Tk()
        self.screen = Screen()
        self.window.geometry("500x500")

    def input_command(self):
        this_input = self.screen.textinput("tigr", "Command:")
        return this_input

    def show_greetings(self):
        label = Label(text=f'Welcome to the Tigr Application',  font=('Courier', 12, 'bold'))
        label.pack(side='bottom')



