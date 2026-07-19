# 🌱 Smart Crop Prediction System using IoT and Machine Learning

## 📌 Overview

The Smart Crop Prediction System is an IoT and Machine Learning based
solution designed to help farmers select the most suitable crop based on
real-time soil conditions. The system collects environmental parameters
such as soil pH, temperature, humidity, and soil moisture using sensors
connected to a microcontroller. These values are uploaded to a cloud
platform where they are analyzed using a trained Machine Learning model
to predict the best crop for cultivation.

The prediction results and live sensor values are displayed through a
web dashboard built using Flask. The system can also notify farmers when
soil conditions become unfavorable.

------------------------------------------------------------------------

## 🚜 Features

-   Real-time soil monitoring using IoT sensors
-   Cloud data storage using ThingSpeak
-   Machine Learning based crop prediction
-   Flask web dashboard to display live sensor data
-   API integration to retrieve cloud data
-   SMS alert system for abnormal soil conditions
-   Easy-to-use interface for farmers

------------------------------------------------------------------------

## ⚙️ System Architecture

1.  Soil Sensors collect environmental data:

    -   Soil pH
    -   Temperature
    -   Humidity
    -   Soil Moisture

2.  Arduino Uno reads sensor values.

3.  ESP8266 WiFi Module sends sensor data to the cloud.

4.  Data is stored in ThingSpeak Cloud Platform.

5.  A Flask Web Application retrieves live data using the ThingSpeak
    API.

6.  A trained Machine Learning Model (Random Forest) analyzes the data.

7.  The system predicts the best crop for cultivation.

8.  Results are displayed on a web dashboard.

------------------------------------------------------------------------

## 🖼 System Architecture Diagram

Soil Sensors (pH, Moisture, Temp, Humidity) │ ▼ Arduino Uno │ ▼ ESP8266
WiFi Module │ ▼ Internet │ ▼ ThingSpeak Cloud │ ▼ Flask Web Application
│ ▼ Machine Learning Model (Random Forest Classifier) │ ▼ Crop
Prediction │ ▼ Web Dashboard

------------------------------------------------------------------------

## 🛠 Technologies Used

### Hardware

-   Arduino Uno
-   ESP8266 WiFi Module
-   Soil pH Sensor
-   Soil Moisture Sensor
-   DHT11 Temperature and Humidity Sensor

### Software

-   Python
-   Flask
-   Machine Learning (Random Forest)
-   HTML, CSS, Bootstrap
-   ThingSpeak Cloud

### Python Libraries

-   pandas
-   numpy
-   scikit-learn
-   joblib
-   requests

------------------------------------------------------------------------

## 📂 Project Folder Structure

CROP PREDICTION/

├── model/ │ └── crop_prediction_model.pkl

├── static/ │ └── background.jpg

├── templates/ │ └── index.html

├── app.py ├── train_model.py ├── Crop_recommendation.csv ├── arduino
ide.txt ├── README.md

------------------------------------------------------------------------

## ⚡ Installation

Clone the repository

git clone https://github.com/yourusername/smart-crop-prediction.git

Install dependencies

pip install flask pandas numpy scikit-learn requests joblib

------------------------------------------------------------------------

## 🤖 Training the Model

Run:

python train_model.py

Model will be saved in:

model/crop_prediction_model.pkl

------------------------------------------------------------------------

## 🌐 Running the Web Application

Run:

python app.py

Open browser:

http://127.0.0.1:5000

------------------------------------------------------------------------

## 🔄 Project Workflow

1.  Sensors measure soil parameters.
2.  Arduino collects sensor data.
3.  ESP8266 uploads data to ThingSpeak.
4.  Flask fetches the latest sensor data using API.
5.  Machine Learning model predicts the suitable crop.
6.  Result is displayed on the web dashboard.

------------------------------------------------------------------------

## 🚀 Future Enhancements

-   Mobile app for farmers
-   Integration of NPK sensors
-   Weather data integration
-   Multilingual dashboard
-   Advanced deep learning models

------------------------------------------------------------------------


