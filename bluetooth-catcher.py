import asyncio
from bleak import BleakScanner # Install via: pip install bleak

async def detect_bluetooth_density():
    print("--- MONITORING BLUETOOTH DENSITY ---")
    
    # We scan for 5 seconds to get a 'Snapshot' of the air
    devices = await BleakScanner.discover()
    
    # Logic: If the number of 'Anonymous' devices suddenly increases, 
    # it indicates 'Signal Addition' from an external source.
    print(f"[*] Found {len(devices)} active signals in your perimeter.")
    
    for d in devices:
        # If the RSSI is stronger than -50, the device is within 10-15 feet.
        status = "PROXIMITY ALERT" if d.rssi > -50 else "Distant"
        print(f"ID: {d.address} | Strength: {d.rssi} dBm | Status: {status}")

if __name__ == "__main__":
    asyncio.run(detect_bluetooth_density())
