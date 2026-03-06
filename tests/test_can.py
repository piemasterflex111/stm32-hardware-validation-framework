from framework.can_interface import CANInterface

def run():

    print("CAN test starting")

    can_bus = CANInterface()

    can_bus.send(0x123, [1,2,3,4,5,6,7,8])

    msg = can_bus.receive()

    print("Received:", msg)
