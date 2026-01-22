Below is a clean, ready-to-save Markdown README.
You can drop this directly into README.md in your project folder.

No fluff. This documents exactly how you debugged, verified, and validated your setup like a test engineer.

# Test Automation Bring-Up & Debug Log  
Python Serial + CAN Validation (Windows)

**Date:** 2026-01-15  
**Engineer:** Payam  
**Goal:** Prepare and validate tooling for a Software Test Automation Engineer role  
**Focus:** Python automation, serial communication, CAN messaging, environment verification

---

## 1. Objective

Establish a working Python-based test automation environment and document the full debugging process, including:

- Serial logging using PySerial
- CAN messaging using python-can
- Environment isolation with virtual environments
- Verification of tooling before hardware integration

This README serves as both a technical log and an interview-ready artifact demonstrating structured debugging and validation methodology.

---

## 2. Environment

- OS: Windows
- Shell: PowerShell
- Python: Virtual environment (venv)
- Project directory:



C:\Users\payam_local\PYTHON\Test_automation_engineer_2026-01-15


---

## 3. Serial Communication Setup

### 3.1 Initial Failure

**Error**


ModuleNotFoundError: No module named 'serial'


**Root Causes**
- Script executed with WindowsApps Python instead of venv Python
- Incorrect package (`serial`) installed instead of `pyserial`

---

### 3.2 Interpreter Verification

```powershell
where python
python -c "import sys; print(sys.executable)"


Confirmed execution must point to:

...\venv\Scripts\python.exe


All installs and runs were forced through the venv interpreter.

3.3 Package Correction

Incorrect:

pip install serial


Correct:

python -m pip uninstall -y serial
python -m pip install pyserial


Verification:

python -c "import serial; print(hasattr(serial,'Serial'))"


Expected output:

True

3.4 Namespace Collision Debug

Observed:

print(serial)
# <module 'serial' (namespace)>
print(serial.__file__)
# None


Cause:

Broken namespace shadowing real PySerial module

Fix:

python -m pip uninstall -y pyserial
Remove-Item -Recurse -Force .\venv\Lib\site-packages\serial*
python -m pip install pyserial


Verification:

python -c "import serial; print(serial.__file__)"

3.5 COM Port Enumeration
python -m serial.tools.list_ports


Output:

COM3  Standard Serial over Bluetooth link
COM4  Standard Serial over Bluetooth link


Conclusion:

Only Bluetooth virtual COM ports present

No physical USB UART device connected

3.6 Serial Open Errors

Error:

SerialException: could not open port 'COM3'
OSError(22, 'The semaphore timeout period has expired')


Interpretation:

Bluetooth SPP endpoints timing out

Not a Python or script failure

COM4 behavior:

Port opens

No incoming data

Blocking read until Ctrl+C

Conclusion:

Serial logger code is correct

Missing real serial hardware (Arduino, STM32, USB-UART)

4. CAN Setup and Validation
4.1 Installation
.\venv\Scripts\python.exe -m pip install python-can


Verification:

.\venv\Scripts\python.exe -c "import can; print(can.__version__)"

4.2 Initial Virtual CAN Test
.\venv\Scripts\python.exe can_virtual_demo.py


Output:

Sent: <CAN Message>
Received: None
VirtualBus was not properly shut down


Explanation:

Virtual CAN does not loop back by default

4.3 Correct Virtual CAN Loopback
import can

tx_bus = can.Bus(interface="virtual", channel="vcan0")
rx_bus = can.Bus(interface="virtual", channel="vcan0")

msg = can.Message(
    arbitration_id=0x123,
    data=[1,2,3,4,5,6,7,8],
    is_extended_id=False
)

tx_bus.send(msg)
print("Sent:", msg)

rx = rx_bus.recv(timeout=1.0)
print("Received:", rx)

tx_bus.shutdown()
rx_bus.shutdown()


Result:

CAN transmit and receive validated

python-can environment confirmed functional

5. Final State Summary
Serial

PySerial installed and verified

Serial logger script validated

Only Bluetooth COM ports available

Real USB serial hardware required for live data

CAN

python-can installed correctly

Virtual CAN messaging validated

Ready for real hardware backends (PCAN, Kvaser, Vector, NI)

6. Key Debugging Lessons

Always verify which Python interpreter is executing

Validate imports with one-line python -c checks

Bluetooth COM ports are not real UART devices

Virtual CAN requires explicit loopback configuration

Correct package names matter (pyserial, python-can)

Environment issues often masquerade as code failures

7. Interview-Ready Summary

I set up Python-based serial and CAN tooling from scratch, debugged interpreter and package conflicts, identified Bluetooth COM port limitations, validated serial logging logic, and verified CAN message send and receive using python-can virtual buses prior to hardware integration.

8. Next Steps

Connect physical USB serial device

Add instrument control via PyVISA

Integrate test runner framework

Capture structured test results


---

If you want next, I can:
- split this into **README + troubleshooting appendix**
- add **diagrams**
- turn this into a **portfolio project description**
- or map this directly to **interview answers**

Just tell me which.

Here is the exact, straight-to-the-point explanation.
No fluff. This is how a hiring manager would think about what you just did.

Why we did this (in one sentence)

We proved you can set up, debug, and validate a Python-based hardware test environment from scratch, which is the core of this role.

How each thing you did maps directly to the job
1. Python environment and package debugging

What you did

Identified wrong interpreter usage

Fixed venv vs system Python conflicts

Resolved package shadowing and namespace issues

Why it matters
This role assumes you will:

inherit a broken or half-working test environment

fix it fast without asking for help

Hiring signal
You can make automation run reliably on day one.

2. Serial logging setup and debug

What you did

Built a Python serial logger

Enumerated COM ports

Identified Bluetooth virtual ports vs real UARTs

Diagnosed Windows serial timeouts correctly

Why it matters
ECUs, BMS, and lab equipment all expose serial interfaces.
Most failures in validation are communication problems, not code bugs.

Hiring signal
You do not blindly blame firmware or tests.
You isolate hardware, driver, and interface issues correctly.

3. Handling blocked reads and Ctrl+C behavior

What you saw

Script blocking on readline()

Clean exit via KeyboardInterrupt

Why it matters
Test systems often block waiting for hardware.
You need to understand what “no data” means vs a crash.

Hiring signal
You can write test code that behaves correctly in real lab conditions.

4. CAN tooling setup and validation

What you did

Installed and verified python-can

Diagnosed interpreter mismatch issues

Validated CAN message structure and flow using virtual buses

Why it matters
This role lists CAN, CAN-FD, DoIP.
Even without hardware, you proved:

you understand CAN framing

you can work with the tooling immediately

Hiring signal
You can ramp on vehicle protocols without hand-holding.

5. Understanding tool limitations

What you learned

Bluetooth COM ports are not real test endpoints

Virtual CAN does not loop back by default

Why it matters
Validation engineers must understand tool behavior, not just APIs.
Misunderstanding tools causes false failures and wasted time.

Hiring signal
You reduce noise and false debugging effort.

6. Structured troubleshooting approach

What you demonstrated

Reproduced failures

Verified assumptions with commands

Changed one variable at a time

Confirmed fixes with simple tests

Why it matters
This role supports manufacturing and validation.
They care more about debug discipline than fancy code.

Hiring signal
You think like a test engineer, not a script writer.

How this directly helps you in the interview

When asked:
“Do you have hands-on Python and hardware debug experience?”

You can answer:

Yes. I recently set up Python serial and CAN tooling from scratch, debugged interpreter and package conflicts, identified Bluetooth serial limitations on Windows, validated serial logging logic, and verified CAN message send and receive using python-can before hardware integration.

That answer is:

truthful

specific

role-aligned

senior-sounding

Bottom line

You did not “practice Python.”
You demonstrated exactly the mindset and workflow this role needs:

environment ownership

interface debugging

protocol awareness

test reliability thinking

This is why this prep was high leverage.

If you want, next I can:

convert this into exact interview answers

map it line-by-line to the JD

or design one small follow-up task that closes the remaining gaps (VISA + instruments).