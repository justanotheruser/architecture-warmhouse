import random

from flask import Flask, request
from flask.json import jsonify


app = Flask(__name__)


@app.get("/temperature")
def get_temperature():
    location = request.args.get("location")
    sensor_id = request.args.get("sensorId")

    if location is None:
        match sensor_id:
            case "1":
                location = "Living Room"
            case "2":
                location = "Bedroom"
            case "3":
                location = "Kitchen"
            case _:
                location = "Unknown"

    if sensor_id is None:
        match location:
            case "Living Room":
                sensor_id = "1"
            case "Bedroom":
                sensor_id = "2"
            case "Kitchen":
                sensor_id = "3"
            case _:
                sensor_id = "0"

    return jsonify(
        {
            "value": random.random() * 30 + 15,
            "unit": "celcius",
            "location": location,
            "status": "ok",
            "sensor_id": sensor_id,
            "sensor_type": "temperatureMeasurement",
            "description": None,
        }
    )
