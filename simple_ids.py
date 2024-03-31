import collections
from scapy.all import sniff, IP
import threading
import time

THRESHOLD_PACKETS_PER_MINUTE = 100  # Threshold for triggering an alert
MONITORING_WINDOW = 60  # Time window in seconds

# Initialize a counter to keep track of packets per source IP
packet_counter = collections.Counter()

def packet_callback(packet):
    if IP in packet:
        packet_counter[packet[IP].src] += 1

def reset_packet_counter():
    global packet_counter
    while True:
        time.sleep(MONITORING_WINDOW)
        for ip, count in packet_counter.items():
            if count > THRESHOLD_PACKETS_PER_MINUTE:
                print(f"High traffic detected from {ip}: {count} packets in the last minute.")
        packet_counter.clear()

if __name__ == "__main__":
    # Start the counter reset thread
    threading.Thread(target=reset_packet_counter, daemon=True).start()

    # Start sniffing the network
    print("Starting network monitoring...")
    sniff(prn=packet_callback, store=False)
