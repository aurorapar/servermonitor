import subprocess
import os
import json

SERVICES_FILE = 'services.json'

SERVICES = {
    'icmp': None,
    'bmc':  80,
    'ssh/sftp': 22,
    'vnc': 5900,
}


def check_init():
    global SERVICES
    if not os.path.exists(SERVICES_FILE):
        with open(SERVICES_FILE, 'w') as f:
            json.dump(SERVICES, f)
    else:
        with open(SERVICES_FILE, 'r') as f:
            SERVICES = json.load(f)


def poll(address, port):
    try:
        output = subprocess.check_output(['nmap', '-p', str(port), str(address)])
        if 'open' in output.decode('utf-8'):
            return
        return False
    except:
        return False


def ping(address):
    try:
        output = subprocess.check_output(['ping', '-n', '1', address])
        if 'Lost = 1' in output.decode('utf-8'):
            return False
        return True
    except:
        return False
