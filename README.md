# Hardware Validation Bench

Python utilities for operating and recording a small serial/CAN hardware bench. The repository is intentionally fail-closed: software tests can verify parsing and detection logic, but they do not establish that physical hardware was tested.

## Current state

See [`PHYSICAL_VALIDATION_STATUS.md`](PHYSICAL_VALIDATION_STATUS.md). No supported serial device was connected during the latest audit, so physical validation remains blocked.

## Verification layers

### 1. Software verification

```bash
make verify
```

This checks script syntax and hardware-detection logic. It is not a physical test.

### 2. Hardware presence gate

```bash
make hardware-check
```

The command exits nonzero unless Linux exposes a serial interface such as `/dev/serial/by-id/...`, `/dev/ttyACM*`, or `/dev/ttyUSB*`.

### 3. Explicit physical command/response check

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/run_uart_check.py \
  --port /dev/serial/by-id/<device> \
  --baud 115200 \
  --command PING \
  --expect PONG
```

A run records the selected device, command, exact response, raw bytes, timing, error state, and pass/fail result under `artifacts/physical/<timestamp>/`.

## Evidence rule

A hardware capability may be stated only when a physical evidence directory exists and identifies the actual device and observed response. Mock tests, virtual CAN, and simulated serial logs remain development aids only.

## Existing helpers

The `src/` directory retains serial, CAN, and VISA exploration utilities. They are reference code and are not described as production-grade or physically verified unless their behavior is covered by a recorded bench run.
