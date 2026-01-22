import time
from datetime import datetime
import random

OUT = "serial_log_sim.txt"

print("Simulating serial stream. Ctrl+C to stop.")
with open(OUT, "a", encoding="utf-8") as f:
    try:
        while True:
            
            ts = datetime.now().isoformat(timespec="seconds")
            line = f"TEMP={25+random.random()*2:.2f}, VBUS={12+random.random()*0.2:.2f}"
            msg = f"{ts} {line}"
            print(msg)
            f.write(msg + "\n")
            time.sleep(0.3)

        ...
    except KeyboardInterrupt:
        print("Stopped.")
