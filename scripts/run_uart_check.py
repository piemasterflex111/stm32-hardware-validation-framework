#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import argparse
import json
import sys
import time


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run one explicit command/response check against a connected serial device."
    )
    parser.add_argument("--port", required=True, help="Explicit Linux device path, preferably /dev/serial/by-id/...")
    parser.add_argument("--baud", type=int, default=115200)
    parser.add_argument("--command", default="PING")
    parser.add_argument("--expect", required=True, help="Exact expected response after trimming whitespace")
    parser.add_argument("--timeout", type=float, default=2.0)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    port = Path(args.port)
    if not port.exists():
        print(f"BLOCKED: serial device does not exist: {port}", file=sys.stderr)
        return 2
    try:
        import serial
    except ImportError:
        print("BLOCKED: pyserial is not installed; run `python -m pip install -r requirements.txt`.", file=sys.stderr)
        return 2

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = Path("artifacts/physical") / stamp
    out_dir.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    raw = b""
    error: str | None = None
    try:
        with serial.Serial(str(port), args.baud, timeout=args.timeout) as device:
            device.reset_input_buffer()
            device.reset_output_buffer()
            device.write((args.command + "\n").encode("utf-8"))
            device.flush()
            raw = device.readline()
    except Exception as exc:
        error = f"{type(exc).__name__}: {exc}"

    response = raw.decode("utf-8", errors="replace").strip()
    passed = error is None and response == args.expect
    result = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "port": str(port),
        "resolved_port": str(port.resolve()),
        "baud": args.baud,
        "command": args.command,
        "expected_response": args.expect,
        "observed_response": response,
        "raw_hex": raw.hex(),
        "elapsed_seconds": round(time.monotonic() - started, 6),
        "error": error,
        "passed": passed,
    }
    (out_dir / "result.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    (out_dir / "raw.bin").write_bytes(raw)
    print(json.dumps(result, indent=2))
    print(f"Evidence: {out_dir}")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
