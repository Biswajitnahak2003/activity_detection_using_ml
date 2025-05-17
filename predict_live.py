import serial
import joblib
import time
import re  # for regex to extract BPM

# Load the trained model
model = joblib.load("bpm_activity_model.pkl")

# Activity mapping
activity_labels = {0: "rest", 1: "walk"}

# Serial port setup 
SERIAL_PORT = 'COM7'  # Update if needed
BAUD_RATE = 9600

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
    time.sleep(2)  # Wait for serial connection to initialize

    print("Listening for BPM values... (Press Ctrl+C to stop)")
    while True:
        line = ser.readline().decode('utf-8').strip()

        # Extract numeric BPM from line, e.g., "BPM: 140"
        match = re.search(r'\d+', line)
        if match:
            bpm = int(match.group())
            prediction = model.predict([[bpm]])[0]
            activity = activity_labels[prediction]
            print(f"BPM: {bpm} -> Activity: {activity}")
        else:
            print(f"Ignored: {line}")
except KeyboardInterrupt:
    print("Stopped.")
except Exception as e:
    print(f"Error: {e}")
finally:
    if 'ser' in locals():
        ser.close()
