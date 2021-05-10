from tkinter import *


class ServerGui(Frame):

    def __init__(self, master):

        self.master = master
        super(ServerGui, self).__init__()
        self.labels = {}

    def create_label(self, name, **kwargs):

        if not len(name):
            print("Label not named")
            exit(0)

        label = Label(master=self)
        for k, v in kwargs.items():
            label.__setattr__(k, v)

        self.labels[name] = label

    def update_label(self, name, attr, value):

        setattr(self.labels[name], attr, value)
