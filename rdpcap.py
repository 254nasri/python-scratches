from scapy.all import *
import scapy
x=rdpcap("/root/Desktop/wireshark/mail.pcap")
sessions=x.sessions()
for session in sessions:
    httpay=""
    for packet in sessions[session]:
        try:
            if packet["%TCP%"].dport==80 or packet["%TCP%"].sport==80:
                httpay+=str(packet["%TCP%"].payload)
                print(httpay)
        except:
            pass
    header=get_http_headers()
