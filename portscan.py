#!/usr/bin/env python3

import argparse
import socket
import struct
import sys
import queue
import threading

availableports = []


def TCP_scan(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1.0)

    try:
        sock.connect((host, port))
        availableports.append(port)
    except:
        print("Connection failed for port {}!".format(port))

    # sock.shutdown()??
    sock.close()


def UDP_scan(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1.0)

    try:
        sock.sendto(struct.pack("!i", 69), (host, port))
        data, addr = sock.recvfrom(64)
        print(data)
        sock.s
    except:
        print("Connection failed!")


class Worker(threading.Thread):
    def __init__(self, ports, openPorts, host, *args, **kwargs):
        self.ports = ports
        self.openPorts = openPorts
        self.host = host
        super().__init__(*args, **kwargs)

    def run(self):
        while True:
            try:
                portToScan = self.ports.get(timeout=3)  # 3s timeout
            except queue.Empty:
                return

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            status = ""
            try:
                sock.connect(("localhost", portToScan))
                status = "open"
                self.openPorts.put(portToScan)
            except:
                status = "closed"
            sock.close()
            print("%5s | %s" % (portToScan, status))
            self.ports.task_done()


def multi_thread_TCP_scan(host, minPort, maxPort):
    portsToVisitQueue = queue.Queue()
    openPortsQueue = queue.Queue()
    for i in range(minPort, maxPort):
        portsToVisitQueue.put_nowait(i)

    print(f"Scanning Ports on {host} from port {minPort} to port {maxPort}")
    print(" Port | Status")
    for _ in range(20):
        Worker(portsToVisitQueue, openPortsQueue, host).start()
    portsToVisitQueue.join()

    print("-----------------------------------")
    print("Open Ports:")
    try:
        while openPortsQueue.qsize != 0:
            print(openPortsQueue.get_nowait())
    except:
        pass


def ICMP_ping(host):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scans a host for open ports")
    parser.add_argument("host", help="IPv4 address of host", type=str)
    parser.add_argument("minport", help="Port to start searching at", type=int)
    parser.add_argument("maxport", help="Port to stop searching at", type=int)
    parser.add_argument(
        "scantype", help="Type of scan to perform", choices=["U", "T", "I"], type=str
    )
    args = parser.parse_args()

    if args.scantype == "T":
        multi_thread_TCP_scan(args.host, args.minport, args.maxport)
    else:
        # for port in range(1 << 10):
        UDP_scan(args.host, 80)

    # udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # print(args)
