# activity_detection_using_ml

An IoT-based heart rate and activity detection system using Machine Learning and Arduino. This project collects heart rate data in real time, trains a model to detect the activity (Resting, Walking, or Running), and displays the predicted activity live.

---

## 💡 Project Overview

This project integrates Arduino and Machine Learning for real-time monitoring and classification of physical activity based on heart rate (BPM). It includes:

- **Hardware** for real-time BPM acquisition
- **Data collection and model training** in Python
- **Live prediction** based on streaming heart rate
- **LCD display** for outputting the activity 

---

## 🛠️ Components Used

### Hardwares
- **Arduino UNO** 
- **HW-827 Heart Rate Sensor Module**
- **I2C LCD (16x2)** with SDA/SCL pins
- **Jumper Wires** and **Breadboard**

### Software
- Python (vs code)
- Arduino IDE
- Git & GitHub

🚀 How It Works

    Data Collection:
    Upload the heart_rate_monitor.ino to Arduino. Use collect_data.py to receive and store BPM data in bpm_dataset.csv. more the number of data better model accuracy,as 
    a small course project i've collected only 150 dataset with 60% accuracy,it can be higher with more data.. 

    Model Training:
    Run train_model.py to train a Decision Tree model on the collected data. The model is saved as bpm_activity_model.pkl.

    Live Prediction
    Use predict_live.py to read live BPM from the Arduino and classify activity in real-time using the trained model.

    Output
    The activity class (Resting, Walking, Running) is displayed on the terminal of editer.
🖥️ Demo 


🤖 Future Improvements

    Use more features like motion data (accelerometer)

    Deploy to a mobile app or web interface

    Improve accuracy using deep learning models

🧠 Skills Demonstrated

  Arduino hardware interfacing

  Serial communication

  Machine Learning model training

  Real-time data visualization

