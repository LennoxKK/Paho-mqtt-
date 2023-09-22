from flask import Flask, render_template, request, redirect, url_for
import paho.mqtt.client as mqtt
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# MQTT broker settings
MQTT_BROKER_HOST = "localhost"  # Change to your MQTT broker's host
MQTT_BROKER_PORT = 1883

# MySQL database settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:LennoxEKK99@<host>/mqtt_sql'
# Replace <username>, <password>, <host>, and <database> with your MySQL credentials

db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# MQTT client setup
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with code " + str(rc))

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, 60)

@app.route("/")
def index():
    messages = Message.query.all()
    return render_template("index.html", messages=messages)

@app.route("/publish", methods=["POST"])
def publish():
    message = request.form.get("message")
    if message:
        # Publish the message to an MQTT topic
        mqtt_client.publish("test/topic", message)
        # Store the message in the MySQL database
        new_message = Message(content=message)
        db.session.add(new_message)
        db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    # Create the database table if it doesn't exist
    db.create_all()

    app.run(debug=True)
