# Kode Blue, 10/29/30
# Script for getting whois informaiton about a Domain Name
# FastSubnetScanner.py

import requests
from threading import Thread
from queue import Queue
import sys

q = Queue()

def scan_subdomains(domain):
    global q
    while True:
        # Get subdomain from Queue
        subdomain = q.get()
        # scan subdomain
        url= f"http://{subdomain}.{domain}"
        try:
            requests.get(url)
        except requests.ConnectionError:
            pass
        except KeyboardInterrupt:
            print("Keyboard Interrupt. Exiting.")
            sys.exit()
        else:
            print("[+] Discovered Subdomain: ", url)

        q.task_done()

def controller(domain,n_threads,subdomains):
    global q
    for subdomain in subdomains:
        q.put(subdomain)
    for t in range(n_threads):
        # Start all threads
        worker = Thread(target=scan_subdomains, args=(domain,))
        worker.daemon = True
        worker.start()

def scan_domain(domain,n_threads,subdomains):
    global q
    controller(domain=domain,n_threads=n_threads,subdomains=open(subdomains).read().splitlines())
    q.join()

def run_alone():
    if __name__ == "__main__":
        import argparse
        parser = argparse.ArgumentParser(description="Faster Subdomain Scanner")
        parser.add_argument("-d", "--domain", help="Domain to Scan")
        parser.add_argument("-l", "--wordlist", help="Wordlist to Scan from", default="subdomains.txt")
        parser.add_argument("-n", "--num-threads", help="Number of threads to use", default=10)

        args = parser.parse_args()
        domain = args.domain
        wordlist = args.wordlist
        num_threads = int(args.num_threads)

        controller(domain=domain,n_threads=num_threads,subdomains=open(wordlist).read().splitlines())
        q.join()
        print("Done")

run_alone()
