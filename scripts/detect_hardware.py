#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import json
import subprocess
import sys

SERIAL_PATTERNS = ("/dev/serial/by-id/*", "/dev/ttyACM*", "/dev/ttyUSB*")
KNOWN_USB_TERMS = (
    "STMicroelectronics",
    "STM32",
    "FTDI",
    "Silicon Labs",
    "Prolific",
    "SEGGER",
)


def serial_candidates() -> list[str]:
    found: list[str] = []
    for pattern in SERIAL_PATTERNS:
        for path in sorted(Path("/").glob(pattern.lstrip("/"))):
            resolved = str(path.resolve()) if path.is_symlink() else str(path)
            label = f"{path} -> {resolved}" if str(path) != resolved else str(path)
            if label not in found:
                found.append(label)
    return found


def usb_candidates(lsusb_text: str) -> list[str]:
    return [
        line for line in lsusb_text.splitlines()
        if any(term.lower() in line.lower() for term in KNOWN_USB_TERMS)
    ]


def detect() -> dict[str, object]:
    try:
        lsusb_text = subprocess.check_output(["lsusb"], text=True, stderr=subprocess.STDOUT)
    except (OSError, subprocess.SubprocessError) as exc:
        lsusb_text = f"lsusb unavailable: {type(exc).__name__}: {exc}"
    serial = serial_candidates()
    usb = usb_candidates(lsusb_text)
    return {
        "serial_candidates": serial,
        "known_usb_candidates": usb,
        "physical_interface_present": bool(serial),
    }


def main() -> int:
    result = detect()
    print(json.dumps(result, indent=2))
    if not result["physical_interface_present"]:
        print(
            "BLOCKED: no serial interface is connected; no physical validation may be claimed.",
            file=sys.stderr,
        )
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
