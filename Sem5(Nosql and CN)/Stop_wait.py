import time
import random

class StopAndWaitARQ:
    def __init__(self):
        self.sequence_number = 0
        self.timeout = 2  # in seconds

    def send(self, message):
        print(f"Sender: Sending message {self.sequence_number}")
        time.sleep(random.uniform(0, 1))  # Simulating network delay

        # Simulating possible scenarios in the network
        if random.random() < 0.2:  # Simulating timeout
            print("Sender: Timeout occurred. Resending message.")
            self.send(message)
            return None

        print("Receiver: Message received successfully.")
        self.sequence_number += 1
        return message

    def receive(self, message):
        # Simulating acknowledgement delay
        time.sleep(random.uniform(0, 1))
        
        if random.random() < 0.1:  # Simulating sequence number loss
            print("Receiver: Sequence number lost. Ignoring the message.")
            return None

        print(f"Receiver: Received message {message}. Sending acknowledgment.")
        return "ACK"

def simulate_network_conditions():
    sender = StopAndWaitARQ()
    receiver = StopAndWaitARQ()

    for _ in range(5):  # Simulating five messages
        message = f"Message {sender.sequence_number}"
        ack = None

        while ack is None:
            ack = receiver.receive(sender.send(message))

        print(f"Sender: Received acknowledgment {ack}")
        print("-------------------------------------------------------")

if __name__ == "__main__":
    simulate_network_conditions()
