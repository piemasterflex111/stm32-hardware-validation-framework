import can

def main():
    bus = can.Bus(interface="virtual")

    tx = can.Message(arbitration_id=0x123, data=[1,2,3,4,5,6,7,8], is_extended_id=False)
    bus.send(tx)
    print("Sent:", tx)

    rx = bus.recv(timeout=1.0)
    print("Received:", rx)

if __name__ == "__main__":
    main()
