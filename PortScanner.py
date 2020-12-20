# Kode Blue, 10/29/2020
# Script for scanning for Open ports on a machine
# PortScanner.py

import socket
import sys

def scan_ports(host,minPorts,maxPorts):
    try:
        for port in range(minPorts,maxPorts):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((host, port))
            if result == 0:
                print("Port {}:    Open".format(port))
            sock.close()

    except KeyboardInterrupt:
        print("Keyboard Interrupt...Exiting")
        sys.exit()

    except socket.gaierror:
        print("Unable to resolve Hostname. Exiting")
        sys.exit()

    except socket.error:
        print("Unable to reach server.")
        sys.exit()

def scan_port(host,port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host,p))
        if result == 0:
            print("Port {}:    Open".format(port))
        sock.close()
    except:
        print("Port {}:    Closed".format(port))

def main(hostToScan,whichType,minPorts,maxPorts,particularPort):
    # Get user input
    remoteServer = hostToScan
    remoteServerIP = socket.gethostbyname(remoteServer)

    print("Scanning Host: ", remoteServerIP)
    if whichType == 0:
        scan_ports(remoteServerIP,minPorts,maxPorts)
    if whichType == 1:
        scan_port(remoteServerIP,particularPort)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Scan for Ports on a Host")
    parser.add_argument("-p", "--port", help="Scan a particular port", default="null")
    parser.add_argument("-m", "--max-port", help="Scan up to max port", default=1024)
    parser.add_argument("--min-port", help="Scan starting at Minimum port", default = 1)
    parser.add_argument("-n", "--hostname", help="Host to scan", default="null")

    args = parser.parse_args()
    minPorts = int(args.min_port)
    maxPorts = int(args.max_port)
    if args.hostname == "null":
        hostname = input("Host to scan: ")
    else:
        hostname = args.hostname

    if not (args.port == "null"):
        scanType=1
        main(hostname,scanType,minPorts,maxPorts,int(args.port))
    else:
        scanType=0
        main(hostname,scanType,minPorts,maxPorts,0)
