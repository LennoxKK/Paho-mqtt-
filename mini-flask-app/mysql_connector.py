import mysql.connector as sql

# Establish a connection to the MySQL database
db = sql.connect(
    host="localhost",
    user="root",
    password="LennoxEKK99",
    database="mqtt_sql"
)

#Create an object to execute sql queries
cursor = db.cursor()


