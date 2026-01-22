from dataclasses import dataclass
from time import sleep
from datetime import datetime

@dataclass
class TestResult:
    name: str
    passed: bool
    details: str 

def test_power_on() -> TestResult:
    # Simulate a power-on test
    sleep(0.2)  # Simulating time taken for the test
    return TestResult(name="Power On Test", passed=True, details="Device powered on successfully.")

def test_communication() -> TestResult:
    # Simulate a communication test
    sleep(0.3)  # Simulating time taken for the test
    return TestResult(name="Communication Test", passed=False, details="Failed to establish communication.")

def main():
    tests = [test_power_on, test_communication]
    results = []

    for test in tests:
        result = test()
        results.append(result)
        status = "PASSED" if result.passed else "FAILED"
        print(f"{result.name}: {status} - {result.details}")

    # Summary
    passed_tests = sum(1 for r in results if r.passed)
    total_tests = len(results)
    print(f"\nTest Summary: {passed_tests}/{total_tests} tests passed.")

if __name__ == "__main__":
    main()