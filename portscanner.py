import socket
from IPy import IP


class PortScan():
    banners = []
    open_ports = []

    def __init__(self, target, port_num):
        self.target = target
        self.port_num = port_num

    # scan the target and define the port range
    def scan(self):
        for port in range(1, 443):
            self.scan_port(port)

    # use IPy to convert hostname to ip
    def check_ip(self):
        try:
            IP(self.target)
            return self.target
        except ValueError:
            # get the ip from the hostname
            return socket.gethostbyname(self.target)

    # Create socket and connect to ip and port before scanning ports
    def scan_port(self, port):
        # condition to test for open ports
        try:
            converted_ip = self.check_ip()
            # create socket
            sock = socket.socket()
            # set a timeout on the socket, so it doesn't stall while running
            sock.settimeout(0.5)
            # connect to port
            sock.connect((converted_ip, port))
            self.open_ports.append(port)
            try:
                banner = sock.recv(1024).decode().strip('\n').strip('\r')
                self.banners.append(banner)
            except:
                self.banners.append(' ')
            sock.close()
        # catches all closed ports and passes so that only open ports are shown
        except:
            pass
