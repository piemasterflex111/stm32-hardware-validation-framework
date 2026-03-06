# STM32F446RE Bring-Up: UART Evidence Pipe + I2C1 Scan + BME280 Validation

Python-free embedded bring-up and peripheral validation project for the **STM32F446RE (NUCLEO-F446RE)** focused on creating a repeatable evidence pipe through UART and proving real hardware communication over I2C.

This project documents a practical hardware validation workflow:
- bring up **USART2** for deterministic logging
- enable **I2C1**
- scan the bus and detect a live device at **0x76**
- read the **BME280 chip ID = 0x60**
- stream **raw temperature ADC values** over UART

It is a focused bring-up and validation project intended to show real embedded debugging, peripheral integration, and auditable proof of hardware communication.

---

## What I Built

I brought up USART2 for deterministic logging, then enabled I2C1 and verified real hardware communication by scanning the bus, detecting the sensor at **0x76**, reading the **BME280 chip ID = 0x60**, and streaming raw temperature ADC values over UART.

---

## Project Goal

Establish a repeatable **evidence pipe** through UART and use it to validate:

- firmware boot and execution
- stable serial logging
- correct peripheral initialization
- I2C bus communication
- successful sensor identification
- basic sensor data readout

The UART output acts as the proof channel for every next step in bring-up.

---

## Hardware / Target

- **MCU / Board:** STM32F446RE on NUCLEO-F446RE
- **Debug / Flash:** ST-LINK via STM32CubeIDE
- **Console:** UART through ST-LINK Virtual COM Port into PuTTY
- **Sensor:** BME280 breakout on I2C1

---

## Tools Used

- **STM32CubeIDE / STM32CubeMX**  
  Peripheral configuration and HAL code generation

- **ST-LINK GDB Server / STM32CubeProgrammer**  
  Build, flash, and verify

- **PuTTY**  
  UART log capture and runtime evidence

- **BME280 breakout + wiring**  
  I2C sensor validation target

---

## Validation Summary

This project validated the following:

- **USART2 logging path is working**
- **I2C1 bus is active**
- **Device ACK detected at 0x76**
- **BME280 chip ID register 0xD0 returned 0x60**
- **Raw temperature register reads were successful**
- **Runtime evidence streamed over UART**

---

## Why UART First

UART is the fastest way to prove:

- firmware boots and runs
- clocks are stable enough for serial communication
- GPIO alternate-function mapping is correct
- the full PC ↔ board communication path works

That makes UART the primary evidence pipe for all later validation work.

---

## Key Embedded Concepts

### UART / USART
USART2 was used in UART mode to create a stable console path from the STM32 to the PC terminal.

### I2C
I2C is a two-wire bus:
- **SCL** = clock
- **SDA** = data

A device responding at **0x76** means the MCU addressed that device and received an ACK.

### BME280 Chip ID
The BME280 chip ID register is located at **0xD0**.  
Expected value: **0x60**

Reading `0xD0 -> 0x60` is strong proof that the sensor communication is real and correct.

### Raw Temperature
The BME280 temperature ADC value is stored across registers **0xFA..0xFC**.  
This project reads and prints the raw value. Conversion to compensated °C is a next-step improvement.

---

## Hardware Wiring

### I2C1 pins used
- **PB8 = I2C1_SCL**
- **PB9 = I2C1_SDA**

### Sensor connections
- **BME280 VCC → 3.3V**
- **BME280 GND → GND**
- **BME280 SCL → PB8**
- **BME280 SDA → PB9**

### Constraints
- I2C requires pull-ups on SDA/SCL
- many BME280 breakout boards include them
- short wires help stability
- 100 kHz is a good starting point

---

## Firmware Configuration

### USART2
Configured for UART logging over the ST-LINK virtual COM port.

Typical pins:
- **PA2 = USART2_TX**
- **PA3 = USART2_RX**

### I2C1
Configured for sensor communication on:
- **PB8 = I2C1_SCL**
- **PB9 = I2C1_SDA**

Initial bus speed:
- **100 kHz**

---

## Runtime Evidence Captured

### I2C Scan Evidence
UART output shows:

```text
Scanning I2C...
Device found: 0x76
```

This confirms:
- I2C peripheral is initialized
- pin mapping is correct
- the sensor is powered and wired correctly
- the device acknowledged at address 0x76

### Sensor Identification Evidence
UART output shows:

```text
BME280 ID: 0x60
```

This confirms:
- register reads are working
- the device is a real BME280

### Raw Temperature Evidence
UART output shows:

```text
Raw Temp: <value>
```

This confirms:
- multi-byte register reads are working
- the sensor is alive
- the bus is stable enough for repeated reads

---

## Core Flow

A typical run follows this sequence:

1. System boots
2. UART initializes and prints boot/evidence messages
3. I2C bus scan runs
4. Device at **0x76** is detected
5. BME280 chip ID register is read
6. Raw temperature registers are read
7. Evidence is printed over UART

---

## Code Placement

The validation loop is executed after peripheral initialization in `main()`:

```c
int main(void)
{
  HAL_Init();
  SystemClock_Config();

  MX_GPIO_Init();
  MX_USART2_UART_Init();
  MX_I2C1_Init();

  uart_print("\r\nBOOT OK\r\n");
  uart_print("Scanning I2C...\r\n");

  while (1)
  {
    i2c_scan();
    read_bme280_id();
    read_bme280_raw_temp();
    HAL_Delay(500);
  }
}
```

---

## Example Logic

### I2C Scan
For each address in the valid range:
- call `HAL_I2C_IsDeviceReady(...)`
- print the address if the device responds with ACK

### BME280 ID Read
Read register `0xD0` using `HAL_I2C_Mem_Read(...)`  
Expected result:
- `0x60`

### Raw Temperature Read
Read registers `0xFA..0xFC` and combine bytes into the raw ADC temperature value.

---

## Example Output

```text
BOOT OK
Scanning I2C...
Device found: 0x76
BME280 ID: 0x60
Raw Temp: 519888
```

---

## Debug Checklist

### If UART stops printing
- verify correct COM port
- verify baud rate
- press RESET on the board
- confirm `MX_USART2_UART_Init()` is still called
- confirm logging is still routed through `huart2`

### If I2C scan finds nothing
- verify wiring to PB8 / PB9
- confirm sensor power at 3.3V
- confirm SDA/SCL pull-ups exist
- keep wires short
- keep bus speed at 100 kHz initially

---

## What This Project Demonstrates

This project shows that I can:

- bring up embedded peripherals on STM32
- use UART as a deterministic evidence/logging path
- validate I2C communication against real hardware
- identify a sensor through direct register access
- read raw sensor data from the device
- build a repeatable hardware validation flow with auditable proof

---

## Interview Summary

- Brought up **USART2** on STM32F446RE and used it as a persistent evidence/logging pipeline
- Configured **I2C1 on PB8/PB9** and validated bus integrity by scanning the bus
- Detected a live device at **0x76**
- Verified the correct sensor by reading **BME280 chip ID register 0xD0 → 0x60**
- Read and streamed raw temperature ADC data from **0xFA..0xFC** over UART
- Used a practical debug loop: wiring → init → bus scan → register proof → data streaming

---

## Next Improvements

- implement Bosch temperature compensation and print °C
- add a UART CLI (`scan`, `id`, `temp`)
- add a heartbeat LED independent of UART
- capture structured evidence artifacts for each run
- expand this into a more reusable embedded validation framework

---

## Why I Built This

My background is in hardware validation, automated test systems, and software-hardware integration.

I built this project to demonstrate a real embedded bring-up and validation workflow with auditable proof over UART. It reflects the kind of structured debugging and peripheral validation work used in firmware validation and hardware test environments.

---

## License

MIT License
