#!/usr/bin/env python3

import argparse
import socket
import sys


def TCP_scan():
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def UDP_scan():
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scans a host for open ports")
    parser.add_argument("host", help="IPv4 address of host", type=str)
    parser.add_argument("scantype", help="U - UDP, T - TCP", type=str)
    args = parser.parse_args()
    
    if args.scantype == 'T':
        print("10")
        TCP_scan()
    else:
        print("01")
        UDP_scan()


    #udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    print(args)
