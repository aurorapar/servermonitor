import time
from tkinter import *
from diagnostics import SERVICES as SERVER_SERVICES
from diagnostics import ping
from diagnostics import poll
from server import Server
from server_gui import ServerGui


SERVERS = []

#get_servers()
SERVERS = [
    Server(hostname='tyan-a320-1', ipv4='10.86.201.3', bmc_ipv4='10.86.203.88'),
    Server(hostname='tyan-a320-2', ipv4='10.86.201.91', bmc_ipv4='10.86.202.250'),
    Server(hostname='tyan-a320-3', ipv4='10.86.201.13', bmc_ipv4='10.86.201.2'),
    Server(hostname='tyan-a320-4', ipv4='10.86.201.50', bmc_ipv4='10.86.200.243'),
]

MAIN_WINDOW_MIN_HEIGHT = 200
MAIN_WINDOW_MIN_WIDTH = 700

GLOBAL_FONT = 'Tahoma'
SERVER_HEADER_COLUMN_FONT = 20
SERVER_INFO_FONT = 12

main_window = Tk()
server_guis = []

for server in SERVERS:

    server_gui = ServerGui(main_window)
    server_guis.append(server_gui)

    server_gui.create_label('title', text=server.hostname, font=(GLOBAL_FONT, SERVER_HEADER_COLUMN_FONT))
    server_gui.labels['title'].pack()

    for service in ('ipv4', 'bmc_ipv4'):

        server_gui.create_label(service,
                                text=f'{service} : {server.__getattribute__(service)}',
                                font=(GLOBAL_FONT, SERVER_INFO_FONT),
                                padx=10,
                                pady=10
                                )

        server_gui.labels[service].pack()

    for service in server.services.keys():

        server_gui.create_label(service,
                                text=f'{service} : {server.services[service]}',
                                font=(GLOBAL_FONT, SERVER_INFO_FONT),
                                padx=10,
                                pady=10
                                )

        server_gui.labels[service].pack()

    server_gui.pack(side=LEFT, padx=10, pady=10)


for server in SERVERS:
    server.update()
    #time.sleep(60)

last_update_lbl = Label(master=main_window, text=f'Last Update: {time.ctime()}')
last_update_lbl.pack(side=TOP)
main_window.mainloop()
