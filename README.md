# MQTT-SQL: 
Mqtt plus sql, simple subscribe and publish.

### Task Overview:
A simple deployment to establish communication between two ends A and B. It is composed of MYSQL for data storage and MQTT a communication protocol. Both ends A and B can publish a message to a topic and subscribe to a topic.
### Dependencies:
1. Install `mosquitto` - From the official website.
2. Install `paho-mqtt` - 
    ```python
    pip install paho-mqtt
    ```
3. Install `Mysql connector` :
    ```python
    pip install mysql-connector-python
    ```
4. Install ` Mysql` - From official website.
### Choice of Tools and Technologies:
The Paho Python Client provides a client class with support for MQTT v5.0, MQTT v3.1.1, and v3.1 on Python 2.7 or 3.x. It also provides some helper functions to make publishing one off messages to an MQTT server very straightforward.
### Configuration and Setup:
- Paho-mqtt

  ```python
    broker = 'localhost'
    port = 1883
  ```

- Mysql-connector
    ```python
    import mysql.connector as sql

    # Establish a connection to the MySQL database
    db = sql.connect(
    host="localhost",
    user="root",
    password="LennoxEKK99",
    database="mqtt_sql"
    )
    ```

    **NOTE** - Make sure that `mosquitto service` is running.
### Security Considerations:
Mysql - Secure compared to other DBMS, (Database Management Systems)
### References
1. [paho-mqtt-python](https://www.emqx.com/en/blog/how-to-use-mqtt-in-python?utm_source=mqttx&utm_medium=referral&utm_campaign=mqttx-help-to-blog)
2. [mosquitto](https://cedalo.com/blog/how-to-install-mosquitto-mqtt-broker-on-windows/)
3. [Mysql-connector-python](https://www.geeksforgeeks.org/how-to-connect-python-with-sql-database/)
### Version Control:
[Git](https://github.com/LennoxKK/Paho-mqtt-/)


### SQL DATABASE VIDEO


https://github.com/LennoxKK/Paho-mqtt-/assets/72440905/04bfd62d-4ef3-4aa2-be7b-df64c1a98554

### MQTT - SQL VIDEO

https://github.com/LennoxKK/Paho-mqtt-/assets/72440905/91745f89-c5f6-47b9-8feb-ebaf837e0044

### MYSQL - AFTER ADDING THE TOPIC : "test\client_w"

https://github.com/LennoxKK/Paho-mqtt-/assets/72440905/3179ee54-fe4e-49d8-92b1-daaeea048ad4

### FILES USED
-- Main files
1. pub.py - publisher
2. sub.py - subscriber
3. mysql_connector.py - connects python to mysql - server

-- Auxiliary files

1. connect.py - makes it possible to choose between publishing or subscribing
2. livestream.py - queries data from database and display it in real time.
3. choice.sh - Choosing between subscribing and pub;lishing.
   


