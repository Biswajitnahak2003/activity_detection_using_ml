#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2); // I2C LCD address

int sensorPin = A0;
int threshold = 550;     
bool pulseDetected = false;
unsigned long lastBeatTime = 0;
unsigned long currentTime = 0;
int bpm = 0;

void setup() {
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Heart Rate:");
}

void loop() {
  int sensorValue = analogRead(sensorPin);
  currentTime = millis();

  // Detect rising edge (heartbeat)
  if (sensorValue > threshold && !pulseDetected) {
    pulseDetected = true;

    unsigned long timeBetweenBeats = currentTime - lastBeatTime;
    if (timeBetweenBeats > 300) {  // Ignore noise (< 200ms = 300bpm, too fast)
      bpm = 60000 / timeBetweenBeats;
      lastBeatTime = currentTime;

      Serial.print("BPM: ");
      Serial.println(bpm);

      lcd.setCursor(0, 1);
      lcd.print("BPM: ");
      lcd.print(bpm);
      lcd.print("   ");
    }
  }

  // Reset pulse detection after pulse goes down
  if (sensorValue < threshold) {
    pulseDetected = false;
  }

  delay(10);  // Small delay for stability
}
