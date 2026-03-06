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
