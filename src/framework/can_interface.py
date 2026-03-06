import can

class CANInterface:

    def __init__(self, channel='vcan0'):
        self.bus = can.Bus(interface='virtual', channel=channel)

    def send(self, arbitration_id, data):

        msg = can.Message(
            arbitration_id=arbitration_id,
            data=data,
            is_extended_id=False
        )

        self.bus.send(msg)

    def receive(self, timeout=1):

        return self.bus.recv(timeout=timeout)
