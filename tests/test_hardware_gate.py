from __future__ import annotations

import unittest

from scripts.detect_hardware import usb_candidates


class HardwareGateTests(unittest.TestCase):
    def test_known_usb_candidates_select_debug_and_serial_devices(self):
        text = "\n".join(
            [
                "Bus 001 Device 002: ID 0483:374b STMicroelectronics ST-LINK/V2.1",
                "Bus 001 Device 003: ID 046d:c52b Logitech Receiver",
                "Bus 001 Device 004: ID 10c4:ea60 Silicon Labs CP210x UART Bridge",
            ]
        )
        selected = usb_candidates(text)
        self.assertEqual(len(selected), 2)
        self.assertTrue(any("STMicroelectronics" in line for line in selected))
        self.assertTrue(any("Silicon Labs" in line for line in selected))

    def test_unrelated_usb_devices_are_not_physical_serial_evidence(self):
        self.assertEqual(usb_candidates("Bus 001 Device 003: Logitech Receiver"), [])


if __name__ == "__main__":
    unittest.main()
