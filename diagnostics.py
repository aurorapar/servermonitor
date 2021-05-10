import subprocess

SERVICES = {
    'ssh/sftp': 22,
    'vnc': 5900,
}


def poll(address, port):
    output = subprocess.check_output(['nmap', '-p', str(port), str(address)])
    if 'closed' in output.decode('utf-8'):
        return False
    return True


def ping(address):
    output = subprocess.check_output(['ping', '-n', '1', address])
    if 'Lost = 1' in output.decode('utf-8'):
        return False
    return True