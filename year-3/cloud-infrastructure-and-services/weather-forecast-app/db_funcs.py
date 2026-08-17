import os
import mysql.connector
import datetime

# constants for table name and db name
DB_NAME = 'weatherDB'
TABLE_NAME = 'weather_data'

# db configuration
db_connection = mysql.connector.connect(
     host=os.environ['DB_HOST'],
     user=os.environ['DB_USER'],
     password=os.environ['DB_PASSWORD']
)

# create db if doesnt already exist
def create_db() -> None:
     db_cursor = db_connection.cursor()
     db_cursor.execute('CREATE DATABASE IF NOT EXISTS ' + DB_NAME)
     db_cursor.close()

# create table if doesn't already exist
def create_table() -> None:
     db_cursor = db_connection.cursor()
     db_cursor.execute('CREATE TABLE IF NOT EXISTS ' + DB_NAME + '.' + TABLE_NAME + 
                       '(day DATE PRIMARY KEY, temperature_avg FLOAT, temperature_min FLOAT, temperature_max FLOAT, wind_direction FLOAT, wind_speed_avg FLOAT, humidity_avg FLOAT, cloudiness_avg FLOAT, precipitation_value_avg FLOAT, precipitation_probability_avg FLOAT)'
                    )
     db_cursor.close()

# insert data into db (update if day already exists)
def insertData(combinedData: dict) -> None:
    db_cursor = db_connection.cursor()
    for day in combinedData:
        # convert day to correct format
        formattedDay = datetime.datetime.strptime(day, "%Y-%m-%d").date()
        data = (formattedDay,
                combinedData[day]['temperature']['avg'],
                combinedData[day]['temperature']['min'],
                combinedData[day]['temperature']['max'],
                combinedData[day]['wind']['direction'],
                combinedData[day]['wind']['speed'],
                combinedData[day]['humidity'],
                combinedData[day]['cloudiness'],
                combinedData[day]['precipitation']['value'],
                combinedData[day]['precipitation']['probability'])

        # Check if the date already exists in the table
        db_cursor.execute(f'SELECT 1 FROM {DB_NAME}.{TABLE_NAME} WHERE day = %s', (formattedDay,))
        if db_cursor.fetchone():
            # If the date exists, update the row
            db_cursor.execute(f'UPDATE {DB_NAME}.{TABLE_NAME} SET temperature_avg = %s, temperature_min = %s, temperature_max = %s, wind_direction = %s, wind_speed_avg = %s, humidity_avg = %s, cloudiness_avg = %s, precipitation_value_avg = %s, precipitation_probability_avg = %s WHERE day = %s', data)
        else:
            # If the date does not exist, insert a new row
            db_cursor.execute(f'INSERT INTO {DB_NAME}.{TABLE_NAME} (day, temperature_avg, temperature_min, temperature_max, wind_direction, wind_speed_avg, humidity_avg, cloudiness_avg, precipitation_value_avg, precipitation_probability_avg) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', data)

    db_connection.commit()
    db_cursor.close()



# deletes all rows in the db
def deleteAllRows() -> None:
     db_cursor = db_connection.cursor()
     db_cursor.execute(f"DELETE FROM {DB_NAME}.{TABLE_NAME}")
     db_connection.commit()
     db_cursor.close()

# selects and returns all rows in the db
def selectAll() -> list[dict]:
     db_cursor = db_connection.cursor()
     db_cursor.execute(f"SELECT * FROM {DB_NAME}.{TABLE_NAME}")
     rows = db_cursor.fetchall()
     db_cursor.close()
     return rows

# deletes the table
def delete_table() -> None:
    db_cursor = db_connection.cursor()
    db_cursor.execute('DROP TABLE IF EXISTS ' + DB_NAME + '.' + TABLE_NAME)
    db_cursor.close()