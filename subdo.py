#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import os
import sys
import threading
import Queue
import socket
import argparse

def print_banner():
    banner = """
    =============================================
       Massive Subdomain Enumerator v1.0
       Coded by: Python 2.7
    =============================================
    """
    print(banner)

def dns_resolve(subdomain, domain, results, lock):
    try:
        target = "{}.{}".format(subdomain, domain)
        ip = socket.gethostbyname(target)
        with lock:
            results.append((target, ip))
            print("[+] Found: {} - {}".format(target, ip))
    except socket.gaierror:
        pass

def worker(queue, domain, results, lock):
    while not queue.empty():
        subdomain = queue.get()
        dns_resolve(subdomain, domain, results, lock)
        queue.task_done()

def main():
    print_banner()

    parser = argparse.ArgumentParser(description="Massive Subdomain Enumerator")
    parser.add_argument("-d", "--domain", required=True, help="Target domain (e.g., example.com)")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to the subdomain wordlist")
    parser.add_argument("-t", "--threads", type=int, default=10, help="Number of threads (default: 10)")
    parser.add_argument("-o", "--output", help="Output file to save results")
    args = parser.parse_args()

    if not os.path.isfile(args.wordlist):
        print("[-] Error: Wordlist file not found!")
        sys.exit(1)

    with open(args.wordlist, "r") as f:
        subdomains = f.read().splitlines()

    queue = Queue.Queue()
    for subdomain in subdomains:
        queue.put(subdomain)

    results = []
    lock = threading.Lock()

    threads = []
    for _ in range(args.threads):
        t = threading.Thread(target=worker, args=(queue, args.domain, results, lock))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    if args.output:
        with open(args.output, "w") as f:
            for subdomain, ip in results:
                f.write("{} - {}\n".format(subdomain, ip))
        print("[*] Results saved to {}".format(args.output))
    else:
        print("\n[*] Subdomain Enumeration Completed!")
        for subdomain, ip in results:
            print("{} - {}".format(subdomain, ip))

if __name__ == "__main__":
    main()
