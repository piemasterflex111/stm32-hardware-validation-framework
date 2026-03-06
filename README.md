# STM32 Hardware Validation Framework

Python-based embedded validation framework demonstrating automated testing of an STM32 device via UART.

Features

- UART command protocol
- Firmware interrogation (VERSION)
- Sensor validation (BME280)
- Automated validation runner
- Structured artifacts:
  - CSV results
  - JSON metadata
  - Markdown reports
  - evidence capture

Architecture

Python Test Runner
        │
        ▼
UART Serial Interface
        │
        ▼
STM32 Firmware
        │
        ▼
I2C Bus
        │
        ▼
BME280 Sensor
