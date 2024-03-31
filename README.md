# Simple intrusion_detection_system
This python script uses 'scapy' in finding high traffic from an IP address, possibly being a possible DDoS condition. For the sake of better reading, we will be using "high traffic" to refer to a number of received packets from a same IP address, exceeding some threshold value within a fixed time window.
# Features
Real-time packet sniffing using scapy, Detection of high traffic volumes from single sources based on a configurable threshold, Logging of potential threats with timestamp and source IP.
# Prerequisites
Python 3.x installed on your system, The scapy library.
# Installation
git clone https://github.com/aidanmacklen/intrusion_detection_system.git, cd directory, pip install scapy
# Running Script
sudo python simple_ids.py
# Configureation
You can adjust the sensitivity of the detection by modifying the following variables at the top of the file:

THRESHOLD_PACKETS_PER_MINUTE: The number of packets from a single source that triggers an alert. Increase for higher traffic networks.
MONITORING_WINDOW: The time window in seconds for tracking packets from each source.
# Note
The script will immediately begin sniffing for packets on all network interfaces. When it detects an IP address sending a number of packets exceeding the THRESHOLD_PACKETS_PER_MINUTE within a MONITORING_WINDOW of 60 seconds, it will log the event to the console.
