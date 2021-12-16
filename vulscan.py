from portscanner import *

targets_ip = input('[+] * Enter the Target to Scan for Vulnerable Ports: ')
port_number = int(input('[+] * Enter the Number of Ports to Scan: '))
vul_file = input('[+] * Enter the File Path: ')
print('\n')

target = PortScan(targets_ip, port_number)
target.scan()

with open(vul_file, 'r') as file:
    count = 0
    for banner in target.banners:
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner:
                print('[!!] VULNERABLE BANNER: ' + banner + 'ON PORT: ' + str(target.open_ports[count]))
        count += 1
