Write-Host "Upgrading STM32 Hardware Validation Repo..."

# -----------------------------
# Ensure folders exist
# -----------------------------

New-Item -ItemType Directory -Force src | Out-Null
New-Item -ItemType Directory -Force tests | Out-Null
New-Item -ItemType Directory -Force docs | Out-Null

# -----------------------------
# Create framework folder
# -----------------------------

New-Item -ItemType Directory -Force src/framework | Out-Null

# -----------------------------
# UART Interface
# -----------------------------

@"
import serial

class UARTDevice:

    def __init__(self, port, baudrate=115200):
        self.ser = serial.Serial(port, baudrate, timeout=1)

    def query(self, command):

        self.ser.write((command + "\n").encode())
        response = self.ser.readline().decode().strip()

        return response
"@ | Set-Content src/framework/uart.py

# -----------------------------
# CAN Interface
# -----------------------------

@"
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
"@ | Set-Content src/framework/can_interface.py

# -----------------------------
# Test Runner
# -----------------------------

@"
import importlib
import os

def run_tests():

    test_dir = "tests"

    for file in os.listdir(test_dir):

        if file.startswith("test_") and file.endswith(".py"):

            module_name = file[:-3]
            module = importlib.import_module(f"tests.{module_name}")

            if hasattr(module, "run"):
                print(f"Running {module_name}")
                module.run()

if __name__ == "__main__":
    run_tests()
"@ | Set-Content src/test_runner.py

# -----------------------------
# Example UART Test
# -----------------------------

@"
from framework.uart import UARTDevice

def run():

    print("UART test starting")

    try:

        dev = UARTDevice("COM4")

        response = dev.query("PING")

        print("Device response:", response)

    except Exception as e:

        print("UART test failed:", e)
"@ | Set-Content tests/test_uart.py

# -----------------------------
# Example CAN Test
# -----------------------------

@"
from framework.can_interface import CANInterface

def run():

    print("CAN test starting")

    can_bus = CANInterface()

    can_bus.send(0x123, [1,2,3,4,5,6,7,8])

    msg = can_bus.receive()

    print("Received:", msg)
"@ | Set-Content tests/test_can.py

# -----------------------------
# Documentation
# -----------------------------

@"
# STM32 Hardware Validation Framework

Python based validation environment for embedded hardware interfaces.

This project demonstrates how Python automation can interact with
embedded systems through UART and CAN.

---

## Architecture

Python Test Runner
        |
        v
Interface Layer
(PySerial / python-can)
        |
        v
Communication Interfaces
UART / CAN
        |
        v
Embedded Target
(STM32 Firmware + Sensors)

---

## Project Structure

src/
    framework/
        uart.py
        can_interface.py
    test_runner.py

tests/
    test_uart.py
    test_can.py

docs/
    documentation

---

## Running Tests

Install dependencies

pip install pyserial python-can

Run tests

python src/test_runner.py

---

## Example Output

Running test_uart
UART test starting

Device response: OK

Running test_can
CAN test starting

Received: <CAN message>

---

## Next Steps

Add real STM32 firmware interaction
Add sensor validation tests
Integrate instrument control
"@ | Set-Content README.md

# -----------------------------
# Docs folder starter
# -----------------------------

@"
Hardware validation notes and system documentation.
"@ | Set-Content docs/README.md

# -----------------------------
# Commit changes
# -----------------------------

git add .

git commit -m "upgrade repo: add framework, tests, runner, and improved documentation"

git push

Write-Host "Repo upgrade complete."