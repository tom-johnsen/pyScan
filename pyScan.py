#!/usr/bin/env python3

import socket
import concurrent.futures
import argparse

def scan_port(target_ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(4) if not timeout else sock.settimeout(timeout)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                try:
                    service_name = socket.getservbyport(port)
                    print(f"Target: {target_ip}\tPort: {port} is open\tDefault Service: {service_name}")
                except OSError:
                    print(f"Target: {target_ip}\tPort: {port} is open\tDefault Service: Unknown")
    except socket.error as e:
        print(f"Error: {str(e)}")

def enumerate_services(target_ip, port_range):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(scan_port, target_ip, port) for port in port_range]
        concurrent.futures.wait(futures)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="pyScan", description="A Simple Multithreaded Service Enumerator")
    parser.add_argument("target_ip", type=str, help="Target IP address")
    parser.add_argument("-t", "--timeout", type=float, help="Set the scanner timeout")
    parser.add_argument("-p", "--ports", type=str, help="Port range (e.g., 1-100)", default="1-100")
    args = parser.parse_args()

    target_ip = args.target_ip
    timeout = args.timeout
    port_range = range(int(args.ports.split('-')[0]), int(args.ports.split('-')[1]) + 1)

    enumerate_services(target_ip, port_range)
