# STM32 Hardware Validation Framework

Python-based validation environment for testing embedded hardware interfaces.

## Architecture

Python Test Runner
        ↓
PySerial / python-can
        ↓
UART / CAN Interfaces
        ↓
STM32 Firmware
        ↓
Peripheral Devices

## Capabilities

- UART logging
- CAN messaging validation
- Python automation framework
- Structured debugging workflow

## Structure

src/        core scripts  
tests/      validation tests  
docs/       documentation  

## Next Steps

- connect real hardware
- add test runner framework
- integrate instrument control
