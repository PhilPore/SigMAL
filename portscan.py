#!/usr/bin/env python3

import argparse
import socket
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scans a host for open ports")
    parser.add_argument("host", help="IPv4 address of host", type=str)
    args = parser.parse_args()

    udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print(args)
