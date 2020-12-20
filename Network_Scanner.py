# Kyle Ketchell, 12/20/2020
# Scan hosts on a network

from scapy.all import ARP, Ether, srp

def scan_network(target):
    """
    Returns data of clients scanned on the network
    """
    arp = ARP(pdst=target)
    ether = Ether(dst="FF:FF:FF:FF:FF:FF")
    
    packet = ether/arp
    result = srp(packet, timeout=3)[0]
    
    for sent, recieved in result:
        clients.append({"ip": recieved.psrc, "mac": recieved.hwsrc})
    
    return clients
    
def main(target):
    clients = scan_network(target)
    
    print("====Available Devices on the Network====")
    print("IP" + " "*18 + "MAC")
    
    for client in clients:
        print("{:16}      {}".format(client['ip'], client['mac']))
        
if __name__ == "__main__":
    target_ip = input{"Which IP to scan? Default 192.168.1.1/24 : ")
    if target_ip == "":
        target_ip = "192.168.1.1/24"
    main(target_ip)
