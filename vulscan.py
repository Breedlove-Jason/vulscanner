from portscanner import *

targets_ip = input('[+] * Enter the Target to Scan for Vulnerable Ports: ')
port_number = int(input('[+] * Enter the Number of Ports to Scan: '))
vul_file = input('[+] * Enter the File Path: ')
print('\n')

target = PortScan(targets_ip, port_number)
target.scan()

