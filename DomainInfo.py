# Kode Blue, 10/29/30
# Script for getting whois informaiton about a Domain Name
# DomainInfo.py

import requests
import whois 
import sys
from FastSubnetScanner import scan_domain

def is_registered(domain_name):
    """
    Returns boolean indicating if 'domain_name' is registered
    """
    try: 
        w= whois.whois(domain_name)
    except Exception:
        return FALSE
    else:
        return bool(w.domain_name)

def domain_information(domain):
    if is_registered(domain):
        whois_info = whois.whois(domain)
        print("Domain Registrar: ", whois_info.registrar)
        print("WHOIS Server: ", whois_info.whois_server)
        print("Creation Date: ", whois_info.creation_date)
        print("Expiration Date: ", whois_info.expiration_date)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Faster Subdomain Scanner")
    parser.add_argument("-d", "--domain", help="Domain to Scan")
    parser.add_argument("-l", "--wordlist", help="Wordlist to use on FSS", default="subdomains.txt")
    parser.add_argument("-n", "--num-threads", help="Number of Threads to execute FSS on", default=10)
    parser.add_argument("-f", "--fss", help="Also do a Fast Subdomain Scan of given Domain, usesage: '-f 1'", default="true", required=False)
    
    args = parser.parse_args()
    domain = args.domain
    wordlist = args.wordlist
    num_threads = int(args.num_threads)

    # Domain Information
    print("Domain Information for: ", domain)
    domain_information(domain)


    if args.fss:
        scan_domain(args.domain,args.num_threads,args.wordlist)
    print("Done")
