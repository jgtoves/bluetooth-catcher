import subprocess
import json
import time

def scan_bluetooth_proximity():
    print("--- SCANNING BLUETOOTH PERIMETER ---")
    try:
        # Calls the native Android Bluetooth scanner (requires Location to be ON)
        raw_output = subprocess.check_output(['termux-bluetooth-scan'], timeout=60)
        devices = json.loads(raw_output)
        
        found_count = len(devices)
        print(f"[*] Found {found_count} transmitters in range.")
        
        for dev in devices:
            name = dev.get('name', 'UNKNOWN_GHOST')
            rssi = dev.get('rssi', -100)
            mac = dev.get('address', '00:00:00')

            # Logic: If signal is stronger than -50, it's 'Savage' proximity.
            if rssi > -50:
                print(f"\n[!!!] PROXIMITY ALERT [!!!]")
                print(f"NAME: {name} | MAC: {mac} | STRENGTH: {rssi}dBm")
                print("ACTION: This device is likely in your immediate physical space.")
            else:
                print(f"[Safe] {name} ({mac}) at {rssi}dBm")
                
    except subprocess.TimeoutExpired:
        print("[!] Scan timed out. Ensure Bluetooth and Location are enabled.")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    while True:
        scan_bluetooth_proximity()
        print("\nWaiting for next sweep...")
        time.sleep(10) # Sweep every 10 seconds
