from flask import Flask, render_template
import requests
import joblib
import numpy as np

# Create Flask app
app = Flask(__name__)

# Load your trained model
model = joblib.load('model/crop_prediction_model.pkl')

# ThinkSpeak channel details
THINGSPEAK_API_KEY = 'OKXFVOIDKWNCAOTL'  # 🔵 Your Thingspeak Read API Key
CHANNEL_ID = '2916667'                   # 🔵 Your Thingspeak Channel ID

# Function to fetch latest data from Thingspeak
def get_latest_sensor_data():
    url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds/last.json?api_key={THINGSPEAK_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        
        try:
            temperature = float(data['field3']) if data['field3'] else 0.0
            humidity = float(data['field2']) if data['field2'] else 0.0
            soil_ph = float(data['field4']) if data['field4'] else 0.0
            soil_moisture = float(data['field1']) if data['field1'] else 0.0  # ⭐ Added Soil Moisture (Assume field5)

            return soil_ph, temperature, humidity, soil_moisture
        except (ValueError, TypeError) as e:
            print(f"Error parsing ThingSpeak data: {e}")
            return None
    else:
        return None

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction Route
@app.route('/predict')
def predict():
    sensor_data = get_latest_sensor_data()
    if sensor_data:
        soil_ph, temperature, humidity, soil_moisture = sensor_data
        features = np.array([[soil_ph, temperature, humidity, soil_moisture]])
        prediction = model.predict(features)
        crop = prediction[0]
        return render_template('index.html', soil_ph=soil_ph, temperature=temperature, humidity=humidity, soil_moisture=soil_moisture, crop=crop)
    else:
        return "Failed to fetch data from ThingSpeak."

if __name__ == '__main__':
    app.run(debug=True)
