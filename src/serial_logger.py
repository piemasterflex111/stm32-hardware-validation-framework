import argparse
from datetime import datetime
import serial
import serial.tools.list_ports

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--port", default=None)
    ap.add_argument("--baud", type=int, default=115200)
    ap.add_argument("--out", default="serial_log.txt")
    args = ap.parse_args()

    if args.list:
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            print(f"{p.device}  {p.description}")
        print(f"{len(ports)} ports found")
        return

    if not args.port:
        print("Error: --port is required. Use --list first.")
        return

    print(f"Opening {args.port} at {args.baud}")
    with serial.Serial(args.port, args.baud, timeout=1) as ser, open(args.out, "a", encoding="utf-8") as f:
        print("Logging. Ctrl+C to stop.")
        while True:
            raw = ser.readline()
            if not raw:
                continue
            line = raw.decode(errors="replace").strip()
            ts = datetime.now().isoformat(timespec="seconds")
            msg = f"{ts} {line}"
            print(msg)
            f.write(msg + "\n")

if __name__ == "__main__":
    main()
