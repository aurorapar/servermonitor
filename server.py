from settings.gui_settings import UP_COLOR, DOWN_COLOR
from diagnostics import poll
from diagnostics import ping
from diagnostics import SERVICES


class Server:

    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)

        self.services = {}
        for service in SERVICES:
            self.services[service] = None

    def update(self):

        address = None
        for service in self.services.keys():
            if 'bmc' in service:
                address = self.bmc_ipv4
            else:
                address = self.ipv4

            result = None
            if service == 'icmp':
                result = ping(address)
            else:
                result = poll(address, SERVICES[service])

            if result:
                self.services[service] = f'{service}: UP'
            else:
                self.services[service] = f'{service}: DOWN'
            if hasattr(self, 'gui'):
                self.gui.update_label(service, 'textvariable', self.services[service])
                self.gui.update_label(service, 'bg', UP_COLOR if 'UP' in self.services[service] else DOWN_COLOR)
                self.gui.master.update()
