# Physical validation status

**Status: BLOCKED — no serial hardware interface detected**

Audit date: 2026-07-23

Observed host state:

- no `/dev/serial/by-id/*` device;
- no `/dev/ttyACM*` device;
- no `/dev/ttyUSB*` device;
- no STM32, ST-LINK, FTDI, Silicon Labs, Prolific, or SEGGER device in `lsusb`.

Therefore this repository does **not** claim a completed physical STM32 or sensor validation run. Software checks and simulated protocol helpers are not substitutes for a connected-device result.

The status may change only after `make hardware-check` finds a real serial interface and `scripts/run_uart_check.py` records a passing response under `artifacts/physical/`.
