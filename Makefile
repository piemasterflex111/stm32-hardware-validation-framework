.PHONY: verify hardware-check

verify:
	python3 -m py_compile scripts/detect_hardware.py scripts/run_uart_check.py tests/test_hardware_gate.py
	python3 -m unittest discover -s tests -v

hardware-check:
	python3 scripts/detect_hardware.py
