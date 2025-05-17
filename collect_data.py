import serial
import csv
import time

# Change COM port to your Arduino port
SERIAL_PORT = 'COM7'
BAUD_RATE = 9600
CSV_FILE = 'bpm_dataset.csv'

def main():
    activity = input("Enter activity label (e.g., rest, walk, run): ").strip().lower()
    num_samples = int(input("How many samples do you want to record? "))

    # Open serial connection
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
    time.sleep(2)  # Wait for Arduino to reset

    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['bpm', 'activity'])

        print(f"Collecting {num_samples} samples... Press Ctrl+C to stop early.")
        count = 0
        while count < num_samples:
            try:
                line = ser.readline().decode('utf-8').strip()
                if line.startswith("BPM:"):
                    bpm = int(line.split(":")[1].strip())
                    writer.writerow([bpm, activity])
                    print(f"BPM: {bpm} -> Label: {activity}")
                    count += 1
            except Exception as e:
                print("Error:", e)

    ser.close()
    print(f"Saved {count} entries to {CSV_FILE}")

if __name__ == '__main__':
    main()
