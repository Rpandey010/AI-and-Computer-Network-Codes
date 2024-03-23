import time
from collections import deque
import random

class Packet:
    def __init__(self, seq_num, data):
        self.seq_num = seq_num
        self.data = data

class SlidingWindowProtocol:
    def __init__(self, window_size, timeout):
        self.window_size = window_size
        self.timeout = timeout
        self.sender_buffer = deque()
        self.receiver_buffer = deque()
        self.expected_seq_num = 0

    def send_packet(self, data):
        packet = Packet(self.expected_seq_num, data)
        self.sender_buffer.append(packet)
        print(f"Sender: Sending packet with seq_num={packet.seq_num}")
        self.expected_seq_num += 1

    def receive_packet(self, packet):
        if packet.seq_num == self.expected_seq_num:
            print(f"Receiver: Received packet with seq_num={packet.seq_num}")
            self.receiver_buffer.append(packet)
            self.expected_seq_num += 1
            self.send_ack(packet.seq_num)
            self.process_buffer()
        else:
            print(f"Receiver: Discarding out-of-order packet with seq_num={packet.seq_num}")

    def send_ack(self, seq_num):
        print(f"Sender: Sending ACK for seq_num={seq_num}")

    def process_buffer(self):
        while self.receiver_buffer and self.receiver_buffer[0].seq_num == self.expected_seq_num:
            packet = self.receiver_buffer.popleft()
            print(f"Receiver: Delivering data: {packet.data}")

    def simulate_network_conditions(self):
        # Simulating network conditions (adjust as needed)
        if random.random() < 0.2:
            print("Simulating sequence number loss...")
            return None
        time.sleep(self.timeout)
        return random.choice(self.sender_buffer)

def main():
    window_size = 4
    timeout = 1
    protocol = SlidingWindowProtocol(window_size, timeout)

    # Simulating data transmission
    for i in range(10):
        protocol.send_packet(f"Data{i}")

    while protocol.receiver_buffer and protocol.receiver_buffer[-1].seq_num < 9:
        packet = protocol.simulate_network_conditions()
        if packet:
            protocol.receive_packet(packet)

if __name__ == "__main__":
    main()
