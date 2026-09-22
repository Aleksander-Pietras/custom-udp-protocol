"""socket_manager.py
Handles:
    Listining on a port for incoming packets
    Sending packets to the ip address
    """
import socket

PORT: int = 9000
BUFFER_SIZE: int = 1024 # Max number of bytes to read per incoming packet

def send_packets(ip_address: str, packets:tuple):
    """Sends byte payloads to a designated IP address over UDP"""
    try:
        # Initalise UDP socket
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            packets_size = 0
            for pack in packets:
                sock.sendto(pack, (ip_address, PORT))
                packets_size += len(pack)

            print(f"Sent {packets_size} bytes to {ip_address}:{PORT}")

    except socket.gaierror:
    # Triggers if the IP address string is malformed or hostname resolution fails 
        print(f"Error: Invalid IP address or hostname '{ip_address}'") 
    except OSError as e:
    # Triggers on general OS/network level errors (e.g., interface down) 
        print(f"Network error while sending: {e}")


def recive_packet():
    """Listens continuously for incoming UDP packets with non-blocking timeout checks."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            # Bind to all local interfaces ('') on the designated port
            sock.bind(('', PORT))

            # Setting a short timeout prevents blocking forever and allows
            # Python to process signals (like Ctrl+C / KeyboardInterrupt) across platforms
            sock.settimeout(1.0)
            print(f"Listening on port {PORT}... (Press Ctrl+C to stop)")

            while True:
                try:
                    data, sender_address = sock.recvfrom(BUFFER_SIZE)

                except TimeoutError:
                # 1-second timeout reached with no packet received.
                # Simply loop around and keep listening.
                    continue
                
            # Process incoming datagram 
                try:
                    decoded_message = data.decode("utf-8")
                    print(f"Received {len(data)} bytes from {sender_address}:{sender_address[1]}")
                    print(f"Message content: '{decoded_message}'\\n")
                except UnicodeDecodeError:
                    # Catches cases where raw binary datagrams (e.g. headers/checksums) can't be decoded as UTF-8
                    print(f"Received {len(data)} raw binary bytes from {sender_address}:{sender_address[1]}\\n")

    except KeyboardInterrupt:
        print("\\nShutting down receiver...")
    except OSError as e:
        # Triggers if another application is already using port 9000 (Address already in use)
        print(f"Socket binding error on port {PORT}: {e}")

