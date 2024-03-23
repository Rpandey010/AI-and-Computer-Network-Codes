import time
import random

def sender(message):
    print(f"Sender: Sending message '{message}'")
    time.sleep(1)  # Simulating transmission time
    return message

def receiver(received_message):
    success_rate = random.random()

    if success_rate < 0.6:  # (Case 1: Lost data)
        print("Receiver: Message lost during transmission")
        return False
    elif success_rate < 0.8:  # (Case 2: Lost acknowledgment)
        print("Receiver: Acknowledgment lost")
        return False
    else:
        print(f"Receiver: Received message '{received_message}' successfully")
        return True

def stop_and_wait_protocol(message):
    while True:
        sent_message = sender(message)

        if receiver(sent_message):
            acknowledgment_received = random.random() < 0.8  # (Case 3: Delayed acknowledgment)
            time.sleep(2) if acknowledgment_received else None  # Simulating delayed acknowledgment
            print("Receiver: Acknowledgment received")
            break
        else:
            print("Sender: Resending message")

if __name__ == "__main__":
    message_to_send = "Oye hoye"

    print("\nCase 1: Problems occur due to lost data")
    stop_and_wait_protocol(message_to_send)

    print("\nCase 2: Problems occur due to lost acknowledgment")
    stop_and_wait_protocol(message_to_send)

    print("\nCase 3: Problem due to delayed data or acknowledgment")
    stop_and_wait_protocol(message_to_send)
