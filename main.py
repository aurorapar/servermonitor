import time
from settings.gui_settings import GLOBAL_FONT, SERVER_HEADER_COLUMN_FONT

from tkinter import *
from server import Server
from server_gui import ServerGui


SERVERS = []

# get_servers()
SERVERS = [
    Server(hostname='tyan-a320-1', ipv4='10.86.201.3', bmc_ipv4='10.86.203.88'),
    Server(hostname='tyan-a320-2', ipv4='10.86.201.91', bmc_ipv4='10.86.202.250'),
    Server(hostname='tyan-a320-3', ipv4='10.86.201.13', bmc_ipv4='10.86.201.2'),
    Server(hostname='tyan-a320-4', ipv4='10.86.201.50', bmc_ipv4='10.86.200.243'),
]

main_window = Tk()

for server in SERVERS:

    server.gui = ServerGui(main_window)

    server.gui.create_label('title', textvariable=server.hostname, font=(GLOBAL_FONT, SERVER_HEADER_COLUMN_FONT),\
                            bg='red', container=True)
    server.gui.labels['title'].pack()

    server.gui.pack()

    #server.update()

last_update_lbl = Label(master=main_window, text=f'Last Update: {time.ctime()}')
last_update_lbl.pack(side=TOP)

#main_window.update()
main_window.mainloop()
