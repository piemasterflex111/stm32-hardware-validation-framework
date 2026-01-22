# Software Test Automation Engineer (ECU Validation) — Home Lab Notes (Payam)

## Goal
Build a **home ECU-validation-style bench** that proves:
- Python-based test automation
- Instrument control / automation (PSU, scope, logic analyzer)
- Electrical debug skills (probe points, rails, timing)
- Industrial buses/protocols (UART/Serial, I2C, SPI, USB/VISA)
- Vehicle protocols (CAN) (add via USB-CAN later)
- Produce **artifacts**: logs + reports + screenshots + wiring/probe maps

---

## Job Context (What the role really is)
**Software Test Automation Engineer**
- Validates and tests automotive ECUs (telematics, infotainment, BMS, ADAS, zonal)
- Builds custom automated test solutions (software + low-level firmware + data mgmt)
- Needs deterministic tests, fast debug loops, stable benches

**Must-haves**
- Solid Python
- Automation instrumentation (PSUs, muxes, DMMs, analyzers, generators)
- Read circuits/schematics + navigate layouts + interpret datasheets
- Vehicle protocols (CAN, CAN-FD, DoIP, Automotive Ethernet, LIN)
- Industrial buses/protocols (USB, VISA, GPIB, Ethernet, Serial, RS-485, SPI, I2C)

Nice-to-have
- Databases/data mgmt (SQL, Databricks, Superset)

---

## Equipment I already have / discussed
### Boards (DUT options)
- STM32 Nucleo
- SAM Xplained D21
- Arduino Mega

### Instruments
- **Rigol DP832** triple output programmable DC power supply (good for SCPI/VISA control)
- **HP 54645D** oscilloscope (scope verification, power rail behavior, timing)
- **USB Logic Analyzer** (8ch 24MHz type) for UART/I2C/SPI captures
- Considering 10x passive probes (P6100 style)

### Candidate sensor
- **BME280** environmental sensor (I2C/SPI)

---

## Big Plan: Build a Fake ECU DUT and test it like a real validation bench
### DUT behaviors to implement (firmware)
- UART console:
  - Boot log
  - `READY` line when stable
  - Error lines on faults
- I2C:
  - Read a sensor (BME280 recommended)
  - Report values over UART (and later CAN)
- SPI:
  - Do a simple SPI transaction (loopback or SPI device later)
- Fault modes:
  - Brownout / undervoltage behavior
  - Sensor missing / NACK
  - Timeout / recovery paths
- (Later) CAN:
  - Heartbeat @ 100 ms
  - Command/response frames
  - Timeout detection

---

## Bench Safety / Setup Rules (non-negotiable)
- Use **one common ground**: PSU + scope + DUT + logic analyzer.
- Start with **current limits low** and increase as needed.
- Prefer 3.3V domain for MCU/sensors (avoid 5V on I2C/SPI unless level shifted).
- Use **10x scope probe** for most work.

---

## Step-by-step Bench Setup (first session)
### 1) DP832 initial configuration
- Independent channels
- Set limits (starting points):
  - CH1 = 5.0V, ILIM 0.30A (if powering 5V rail)
  - CH2 = 3.3V, ILIM 0.30A (typical MCU + sensor rail)
  - CH3 OFF initially
- Tie grounds together (common reference)

### 2) Scope setup (HP 54645D)
- Use 10x probe
- Ground clip to bench ground
- First measurements:
  - VIN rise at power on
  - 3.3V rail stability
  - Any reset/brownout behavior

### 3) Logic analyzer setup
- Install software on laptop
- Plan captures:
  - UART TX/RX (optional, mostly TX)
  - I2C SDA/SCL
  - SPI SCK/MOSI/MISO/CS

---

## “Probe Map” / Datasheet Practice (schematic & debug skill)
Create `hardware/probe_map.md` with:
- VIN / input rail test point
- 3.3V rail test point
- UART TX/RX pins
- I2C SDA/SCL pins
- SPI SCK/MOSI/MISO/CS pins

Add datasheet notes for 1 chosen component (recommended: BME280):
- Operating voltage range
- Absolute max ratings
- Timing constraints (I2C clock modes)
- Expected value ranges (temp/pressure/humidity)

---

## Python Automation Deliverables (what proves the MUST-HAVES)
### Repo structure (target)
`ecu-test-automation-lab/`
- `README.md`
- `hardware/` (probe map, wiring notes, screenshots)
- `firmware/` (DUT code)
- `python/`
  - `run_tests.py`
  - `instruments/`
  - `tests/`
- `configs/` (YAML)
- `logs/` (CSV)
- `reports/` (JSON)

### Test runner requirements
- One command runs all tests:
  - `python run_tests.py --config configs/bench.yaml`
- Standard flow:
  - Setup → pre-checks → execute → pass/fail → cleanup
- Logging:
  - CSV per run (timestamped)
  - JSON summary per run (PASS/FAIL + reasons + timings)

---

## First 3 High-Value Tests (fastest proof)
### Test 1 — UART boot + readiness
Steps:
1. Open UART port
2. Reset DUT (software reset or power cycle)
3. Parse lines until `READY`
4. Fail if not READY within X seconds
5. Write CSV + JSON summary

### Test 2 — I2C read sanity
Steps:
1. Trigger sensor read (or have DUT periodically read)
2. Capture UART output of values (temp/humidity/pressure)
3. Assert values in expected range
4. Capture I2C bus with logic analyzer (address + ACK + payload)

### Test 3 — Brownout recovery (manual PSU first → automate later)
Steps:
1. Start Python test logging UART
2. Manually dip PSU (example: 3.3V → 2.8V for 100–200 ms → back)
3. DUT prints `BROWNOUT` and `RECOVERED`
4. Python times the recovery and decides pass/fail
5. Save run artifacts

---

## Instrument Automation (turn this into “real lab automation”)
### DP832 remote control goal
From Python, you can:
- Set V/I limits
- Turn output ON/OFF
- Read back measured V/I

### Automated brownout test (end-state)
1. Python: set 3.3V, output ON
2. Wait 3 seconds
3. Python: set 2.8V for 200 ms
4. Python: restore 3.3V
5. Python watches UART for event + recovery
6. Pass/fail on:
   - event detected
   - recovery time under threshold
   - no reboot loops / no stuck states

This maps directly to:
- Python automation
- Automation instrumentation (PSU)
- Functional validation + fault injection

---

## Scope + Logic Analyzer “Validation Credibility” Checklist
### Scope captures to save
- VIN rise at power-on
- 3.3V rail dip and recovery during brownout
- SPI clock waveform during transaction
- (Optional) UART TX waveform quality

Save to: `hardware/screenshots/`

### Logic analyzer captures to save
- I2C transaction:
  - correct address
  - ACKs present
  - read bytes observed
- SPI transaction:
  - CS toggles
  - correct clocking (CPOL/CPHA)
  - correct byte count

Save to: `hardware/logic_captures/`

---

## Vehicle Protocols (CAN) — planned add-on
Current status: CAN interface not confirmed in bench.
To fully satisfy the “vehicle protocols” must-have, add:
- USB-to-CAN tool (CANable / Kvaser / Peak, etc.)
- CAN transceiver if needed

Firmware:
- Heartbeat every 100 ms
- Command/response
- Timeout behavior

Python tests:
- Validate message period
- Send command + verify response
- Detect missing heartbeat as fault

---

## BME280 Purchase Decision (sensor)
**Decision: YES, buy it.**
Why:
- Supports I2C + SPI (covers industrial buses)
- 3 signals (temp/humidity/pressure) → richer validation
- 3.3V friendly for STM32/SAM D21
- Cheap enough to stress (brownouts/soaks)
- Great for datasheet-driven pass/fail limits

How it will be used:
- Baseline I2C read + log
- Automated Python test with range checks
- Fault injection via PSU dips
- (Optional) repeat with SPI to show both interfaces

---

## What to show recruiters/hiring managers (hard proof)
Bring:
- Repo tree + README (“one command to run tests”)
- One CSV log file
- One JSON summary report (PASS/FAIL + reasons)
- Scope screenshots (rail behavior)
- Logic analyzer captures (I2C/SPI transactions)
- Probe map + datasheet limits notes

---

## Immediate Next Actions (in order)
1. Confirm DP832 remote interface method (USB or LAN).
2. Buy / wire BME280 (I2C first).
3. Implement firmware outputs:
   - Boot log + `READY`
   - Sensor read output
   - Brownout event lines
4. Implement Python runner + first 3 tests.
5. Capture and store scope + logic analyzer evidence.
6. Add USB-CAN later for full vehicle-protocol coverage.

---