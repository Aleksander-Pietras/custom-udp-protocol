"""socket_manager.py
Handles:
    Listining on a port for incoming packets
    Sending packets to the ip address
    """
import socket

PORT: int = 9000
BUFFER_SIZE: int = 1024 # Max number of bytes to read per incoming packet

def send_packets(ip_address: str, packets:tuple):
    try:
        # Initalise UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        packets_size = 0
        for pack in packets:
            sock.sendto(pack, (ip_address, PORT))
            packets_size += len(pack)

    # except I don't know how this could fail

    finally:
        print(f"Sent {packets_size} bytes to {ip_address}:{PORT}")
        sock.close()



def recive_packet():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind('', PORT)

        sock.settimeout(1.0)

        counter: int = 0
        while True:
            if counter > 20:
                raise KeyboardInterrupt

            try:
                # Block and wait until a packet arrives
                # recvfrom returns a tuple: (raw_bytes, (sender_ip, sender_port))
                data, sender_address = sock.recvfrom(BUFFER_SIZE)
            except socket.timeout:
                counter += 1
                print(f"Waited for packets: {counter} seconds.")
                continue
            
            decoded_message = data.decode("utf-8")
            
            print(f"Received {len(data)} bytes from {sender_address[0]}:{sender_address[1]}")
            print(f"Message content: '{decoded_message}'\n")

    except KeyboardInterrupt: #idk how to actally do this, it doesn't stop when I press CRL + C or any other key
        print("\nShutting down receiver...")
    finally:
        sock.close()




if __name__ == "__main__":
    payload = [
        b"Message 1",
        b"Message 2"
    ]

    ip = "127.0.0.1"

    send_packets(ip, payload)
    

"""Temporary design notes
- Users do not enter an ip address when sending a message, they select a locating and a look up table or a DNS request is made to find the correct ip address
therefore, I will remove the fixed ip address
- Port number is fixed, like for whatsapp it does not change depending who is sending the packet
however, it might change in the future when changing devices, so I'll keep it in mind, but for now I will keep it fixed
- I think the packet is already wrapped with the header, it will have: session_id, checksum, order_id, and something to do with encryption maybe
therefore, f:send_packet does not handle the header and just sends the packet assuming its been correctly handled
"""