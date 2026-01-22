## Overview

This project demonstrates a small embedded hardware validation framework used to automatically test an STM32 microcontroller.

The system consists of:

* STM32 firmware communicating over UART
* A Python validation runner that sends diagnostic commands
* Automated validation checks
* Structured test artifacts (CSV, JSON, Markdown reports)

The firmware reads a BME280 temperature sensor over I2C and exposes a simple command interface (`VERSION`, `TEMP`) that the validation runner interrogates.
