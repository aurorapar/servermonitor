import time
from settings.gui_settings import GLOBAL_FONT, SERVER_HEADER_COLUMN_FONT, FRAME_MAIN_COLOR

from tkinter import *
from server import Server
from server_gui import ServerGui


SERVERS = []

# get_servers()
SERVERS = [
    Server(hostname='localhost', ipv4='127.0.0.1', bmc_ipv4='127.0.0.1'),
    Server(hostname='localhost', ipv4='127.0.0.1', bmc_ipv4='127.0.0.1'),
    Server(hostname='localhost', ipv4='127.0.0.1', bmc_ipv4='127.0.0.1'),
    Server(hostname='localhost', ipv4='127.0.0.1', bmc_ipv4='127.0.0.1'),
]


def main():
    main_window = Tk()
    last_update_lbl = Label(master=main_window, text=f'Last Update: {time.ctime()}')
    last_update_lbl.pack(side=TOP, padx=10)

    for server in SERVERS:
        server.gui = ServerGui(main_window)

        server.gui.create_label('title', text=server.hostname, font=(GLOBAL_FONT, SERVER_HEADER_COLUMN_FONT), bg=FRAME_MAIN_COLOR)
        server.gui.labels['title'].pack()

        server.gui.pack(side='left', padx=10, pady=10)

    while True:
        for server in SERVERS:
            server.update(last_update_lbl)


main()
