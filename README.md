STM32 Hardware Validation Framework

Python-based validation environment for testing embedded hardware interfaces.

This project demonstrates how Python automation can interact with embedded systems through UART and CAN communication, enabling automated device validation similar to workflows used in hardware test and firmware validation environments.

The framework provides a minimal structure for:

Python-based test automation

Hardware interface abstraction

Embedded device communication

Structured validation tests

Architecture
Python Test Runner
        │
        ▼
Interface Layer
(PySerial / python-can)
        │
        ▼
Communication Interfaces
UART / CAN
        │
        ▼
Embedded Target
(STM32 Firmware + Sensors)

The test runner executes validation scripts which interact with embedded devices through Python interface modules.

Project Structure
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

src/framework

Contains communication interface modules used to interact with hardware devices.

tests

Contains validation scripts executed by the test runner.

docs

Additional documentation and design notes.

Running Tests

Install dependencies:

pip install pyserial python-can

Run the test runner:

python src/test_runner.py

The test runner automatically discovers and executes test files located in the tests/ directory.

Example Test Flow

Python test script sends a command to the device over UART.

STM32 firmware processes the command.

Device returns response data to the host system.

Python validation logic verifies expected results.

Test outcome is logged and reported.

Example Output
Running test_uart
UART test starting
Device response: OK

Running test_can
CAN test starting
Received: <CAN message>

Test summary
2 tests passed
0 tests failed
Key Capabilities

UART communication using PySerial

CAN messaging using python-can

Modular Python interface layer

Automated test discovery and execution

Minimal framework for embedded validation workflows

Future Improvements

Planned enhancements include:

STM32 command protocol integration

Sensor validation (e.g., BME280)

Structured test artifacts (JSON / CSV reports)

Integration with lab instruments

Continuous test logging

License

MIT License
