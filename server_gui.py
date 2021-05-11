from settings.gui_settings import GLOBAL_FONT, SERVER_INFO_FONT, LABEL_DEFAULT_COLOR
from tkinter import Frame, Label, StringVar


class ServerGui(Frame):

    def __init__(self, master=None):

        Frame.__init__(self, master)

        self.labels = {}

    def create_label(self, name, **kwargs):

        if not len(name):
            print("Label not named")
            exit(0)

        text = None
        label = Label(self)
        for k, v in kwargs.items():
            if k == 'textvariable':
                text = StringVar(master=label, value=v)
                label.textvariable = text
            else:
                label.__setattr__(k, v)

        if 'bg' not in kwargs.keys():
            label.bg = LABEL_DEFAULT_COLOR

        if not text:
            text = StringVar(master=label, value=name)
        self.labels[name] = label
        self.labels[name].pack()
        print('Label %s created' % name)

    def update_label(self, name, attr, value):

        if name not in self.labels:

            self.create_label(name,
                              textvariable=StringVar(self, f'{name}'),
                              font=(GLOBAL_FONT, SERVER_INFO_FONT),
                              padx=10,
                              pady=10
                              )

            self.labels[name].pack()

        if attr == 'textvariable':
            self.labels[name].textvariable.set(value)
        else:
            setattr(self.labels[name], attr, value)