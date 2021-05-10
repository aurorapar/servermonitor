from diagnostics import ping
from diagnostics import poll
from diagnostics import SERVICES


class Server:

    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)

        self.status = None
        self.bcm_status = None
        self.services = {}
        for service in SERVICES:
            self.services[service] = None

    def update(self):
        self.status = ping(self.ipv4)
        self.bcm_status = ping(self.bmc_ipv4)

        for service in self.services.keys():
            self.services[service] = poll(self.ipv4, SERVICES[service])
