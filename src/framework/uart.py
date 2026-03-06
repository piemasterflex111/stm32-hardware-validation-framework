import serial

class UARTDevice:

    def __init__(self, port, baudrate=115200):
        self.ser = serial.Serial(port, baudrate, timeout=1)

    def query(self, command):

        self.ser.write((command + "\n").encode())
        response = self.ser.readline().decode().strip()

        return response
