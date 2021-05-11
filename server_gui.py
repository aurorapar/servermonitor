from settings.gui_settings import GLOBAL_FONT, SERVER_INFO_FONT, LABEL_DEFAULT_COLOR, FRAME_MAIN_COLOR
from tkinter import Label
from tkinter import ttk


class ServerGui(ttk.Labelframe):

    def __init__(self, master=None):

        style = ttk.Style()
        style.configure('TLabelframe', background=FRAME_MAIN_COLOR)

        ttk.Labelframe.__init__(self, master)

        self.labels = {}

    def create_label(self, name, **kwargs):

        if not len(name):
            print("Label not named")
            exit(0)

        text = None
        label = Label(self)
        for k, v in kwargs.items():
            label[k] = v

        self.labels[name] = label
        self.labels[name].pack(side='top', pady=10, padx=4)

        if name != 'title':
            self.labels[name]['padx'] = 10
            self.labels[name]['pady'] = 10
            self.labels[name]['relief'] = 'raised'

    def update_label(self, name, attr, value):

        if name not in self.labels:

            self.create_label(name,
                              text=name,
                              font=(GLOBAL_FONT, SERVER_INFO_FONT),
                              padx=10,
                              pady=10
                              )

        self.labels[name][attr] = value

