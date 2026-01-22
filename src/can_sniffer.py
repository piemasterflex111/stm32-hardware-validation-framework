import argparse
import can

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--interface", default="virtual", help="virtual, pcan, kvaser, vector, etc.")
    ap.add_argument("--channel", default=None, help="Example: PCAN_USBBUS1 or 0")
    ap.add_argument("--bitrate", type=int, default=500000)
    args = ap.parse_args()

    if args.interface == "virtual":
        bus = can.Bus(interface="virtual")
    else:
        if args.channel is None:
            raise SystemExit("For non-virtual, you must pass --channel (example: PCAN_USBBUS1 or 0).")
        bus = can.Bus(interface=args.interface, channel=args.channel, bitrate=args.bitrate)

    print(f"Listening on interface={args.interface} channel={args.channel} bitrate={args.bitrate}. Ctrl+C to stop.")
    try:
        while True:
            msg = bus.recv(timeout=1.0)
            if msg:
                print(msg)
    except KeyboardInterrupt:
        print("Stopped.")

if __name__ == "__main__":
    main()
