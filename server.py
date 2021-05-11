from settings.gui_settings import UP_COLOR, DOWN_COLOR
from diagnostics import poll, ping, check_init
import time

class Server:

    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)

        self.services = {}

    def update(self, time_label):

        from diagnostics import SERVICES

        address = None
        for service in SERVICES:

            if 'bmc' in service:
                address = self.bmc_ipv4
            else:
                address = self.ipv4

            result = None
            check_init()
            if service in ['icmp', 'bmc']:
                result = ping(address)
            else:
                result = poll(address, SERVICES[service])

            if result:
                self.services[service] = f'{service}: UP'
            else:
                self.services[service] = f'{service}: DOWN'
            if hasattr(self, 'gui'):
                self.gui.update_label(service, 'text', self.services[service])
                self.gui.update_label(service, 'bg', UP_COLOR if 'UP' in self.services[service] else DOWN_COLOR)

        delete_these = []
        for service in self.services.keys():
            if service not in SERVICES:
                delete_these.append(service)
        for item in delete_these:
            del self.services[item]
            self.gui.labels[item].destroy()

        self.gui.master.update()

        time_label['text'] = f'Last Updated: {time.ctime()}'
