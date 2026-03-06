from framework.uart import UARTDevice

def run():

    print("UART test starting")

    try:

        dev = UARTDevice("COM4")

        response = dev.query("PING")

        print("Device response:", response)

    except Exception as e:

        print("UART test failed:", e)
