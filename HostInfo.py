# Kode Blue, 10/29/2020
# Combines several of the other scripts here to provide a super tool that
# can tell you a bunch of stuff about a particular machine
# HostInfo.py

import argparse
import socket
import sys
from datetime import datetime
#from dns import reversename,resolver
from PortScanner import scan_ports,scan_port
from DomainInfo import domain_information

def name_info(host):
    """
    Prints Hostname and IP Addr, Returns <IP Address>
    """
    hostIP = socket.gethostbyname(host)
    hostName = socket.gethostbyaddr(hostIP)
    print("Hostname:    ",hostName[0])
    print("IP Addrs:    ",hostIP)
    return hostIP

def noargument():
    return 1

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Scan for information about a remote host")
    parser.add_argument("-n", "--hostname", help="Host to Scan", default="null")
    parser.add_argument("-m", "--max-port", help="Scan for Open Ports, enter max port to scan", default="null")
    parser.add_argument("--min-port", help="Scan for Open ports, enter min port to scan", default = "null")
    parser.add_argument("-p", "--scan-port", help="Scan a particular port", default="null")
    parser.add_argument("--whois", help="Perform whois querey on host", action = 'store_true')

    args = parser.parse_args()
    
    if args.max_port == "null":
        maxPorts=1024
    else:
        maxPorts=int(args.max_port)

    if args.min_port == "null":
        minPorts=1
    else:
        minPorts=int(args.min_port)

    if args.hostname == "null":
        host = input("Enter the host to scan: ")
    else:
        host = args.hostname

    ipAddr = name_info(host)

    if not (args.max_port == "null" or args.min_port == "null"):
        scan_ports(ipAddr,minPorts,maxPorts)
    if not (args.scan_port == "null"):
        scan_port(ipAddr,int(args.scan_port))

    if (args.whois):
        print("="*10,"[WHOIS]","="*10)
        domain_information(ipAddr)
