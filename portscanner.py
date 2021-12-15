import socket
from IPy import IP


# scan the target and define the port range
def scan(target):
    # call the function that changes domain names into ip addresses
    converted_ip = check_ip(target)
    print('\n' + '[Scanning Target] ' + str(target))
    # scan port 1-500
    for port in range(1, 443):
        scan_port(converted_ip, port)


# use IPy to convert hostname to ip
def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        # get the ip from the hostname
        return socket.gethostbyname(ip)


def get_banner(s):
    return s.recv(1024)


# Create socket and connect to ip and port before scanning ports
def scan_port(ipaddress, port):
    # condition to test for open ports
    try:
        # create socket
        sock = socket.socket()
        # set a timeout on the socket, so it doesn't stall while running
        sock.settimeout(0.5)
        # connect to port
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+] Open Port ' + str(port) + ':' + str(banner.decode().strip('\n')))
        except:
            print('[+] Open Port ' + str(port))
    # catches all closed ports and passes so that only open ports are shown
    except:
        pass


if __name__ == "__main__":
    # prompt user for targets
    targets = input('[+] Enter Target/s To Scan(split multiple targets with ,): ')
    # if there is a comma after target then split the ip and strip any excess spaces
    if ',' in targets:

        # iterate to scan each ip address that is added
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    # commence with scanning the listed targets
    else:
        scan(targets)