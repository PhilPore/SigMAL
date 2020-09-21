#!/usr/bin/env python3

import argparse
import socket
import struct
import sys

availableports = []


def TCP_scan(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1.0)

    try:
        sock.connect((host, port))
        availableports.append(port)
    except:
        print("Connection failed for port {}!".format(port))

    #sock.shutdown()??
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


def ICMP_ping(host):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scans a host for open ports")
    parser.add_argument("host", help="IPv4 address of host", type=str)
    parser.add_argument("port", help="Destination port", type=int)
    parser.add_argument(
        "scantype", help="Type of scan to perform", choices=["U", "T", "I"], type=str
    )
    args = parser.parse_args()

    if args.scantype == "T":
        TCP_scan(args.host, 1)
    else:
        # for port in range(1 << 10):
        UDP_scan(args.host, 80)

    # udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print(args)
