from scapy.all import rdpcap
from meshtastic.protobuf import mesh_pb2
import sys

def parse_meshtastic_packet(packet_data):
    """Parse a Meshtastic protobuf packet."""
    try:
        mesh_packet = mesh_pb2.MeshPacket()
        mesh_packet.ParseFromString(packet_data)
        return mesh_packet
    except Exception as e:
        print(f"Error parsing packet: {e}")
        return None

def process_pcap(file_path):
    """Process a PCAP file and parse Meshtastic packets."""
    packets = rdpcap(file_path)
    for packet in packets:
        if packet.haslayer('Raw'):
            raw_data = bytes(packet['Raw'].load)
            parsed_packet = parse_meshtastic_packet(raw_data)
            if parsed_packet:
                print(parsed_packet)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parse_meshtastic_pcap.py <pcap_file>")
        sys.exit(1)

    pcap_file = sys.argv[1]
    process_pcap(pcap_file)
