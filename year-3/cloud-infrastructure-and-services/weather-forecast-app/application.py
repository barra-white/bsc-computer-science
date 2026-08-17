import requests
import json
import xmltodict
import db_funcs

from flask import Flask, render_template

# Flask App
application = Flask(__name__)

# Met Eireann Forcast API URL
URL = "http://metwdb-openaccess.ichec.ie/metno-wdb2ts/locationforecast?lat=54.7210798611;long=-8.7237392806"

### DATA MANIPULATION FUNCTIONS ###
# order of execution
# parser() -> transformer() -> getData() -> combine()
# OUT: Formatted + manipulated data in json format

'''
     Parses XML data from API to JSON
     Params:
          xmlData: xml data response from API
     Returns:
          jsonData: json data in string format
'''
def parser(xmlData: str) -> str:
     # convert XML to dict
     data = xmltodict.parse(xmlData)
     # convert dict to JSON
     jsonData = json.dumps(data)

     return jsonData

'''
     Transforms the data to be grouped by day rather than by hour
     Params:
          parsedData: parsed json data in string format
     Returns:
          transformedData: transformed json data by day in string format
'''
def transformer(parsedData: str) -> dict:
     # load json data
     data = json.loads(parsedData)
     # create empty dict for transformed data
     transformedData = {}
     # loop to iterate over each forecast in the data
     for forecast in data['weatherdata']['product']['time']:
          # extract the day from the forecast
          day = forecast['@from'][:10]
          # check if day is included in transformed data
          if day not in transformedData:
               # add day to transformed data with fields
               transformedData[day] = {
                    'temperature': [],
                    'windDirection': [],
                    'windSpeed': [],
                    'humidity': [],
                    'cloudiness': [],
                    'precipitation': {
                         'value': [],
                         'probability': []
                    }
               }

          # add forecast data to transformed data in appropriate fields
          location = forecast['location']
          if 'temperature' in location:
               transformedData[day]['temperature'].append(location['temperature']['@value'])
          if 'windDirection' in location:
               transformedData[day]['windDirection'].append(location['windDirection']['@name'])
          if 'windSpeed' in location:
               transformedData[day]['windSpeed'].append(location['windSpeed']['@mps'])
          if 'humidity' in location:
               transformedData[day]['humidity'].append(location['humidity']['@value'])
          if 'cloudiness' in location:
               transformedData[day]['cloudiness'].append(location['cloudiness']['@percent'])
          if 'precipitation' in location:
               transformedData[day]['precipitation']['value'].append(location['precipitation']['@value'])
               if '@probability' in location['precipitation']:
                    transformedData[day]['precipitation']['probability'].append(location['precipitation']['@probability'])
          else:
               # if precipitation data does not exist for day, add 0 values
               transformedData[day]['precipitation']['value'].append('0')
               transformedData[day]['precipitation']['probability'].append('0')

     return transformedData

'''
     Combines data produced by transformer function to get average values for each field
          temperature: 
               avg
               min
               max
          wind:
               direction: most common
               speed: avg
          humidity: avg
          cloudiness: avg
          precipitation:
               value: avg
               probability: avg
     Params:
          transformedData: transformed json data by day in string format
     Returns:
          combinedData: combined json data by day in string format
'''
def combine(transformedData: dict) -> dict:
     # create empty dict for combined data
     combinedData = {}
     # loop to iterate over each day in transformed data
     for day in transformedData:
          # convert string values to float
          temperature = list(map(float, transformedData[day]['temperature']))  # given in celsius values
          windSpeed = list(map(float, transformedData[day]['windSpeed']))  # given in mps values
          humidity = list(map(float, transformedData[day]['humidity']))  # given in percent values
          cloudiness = list(map(float, transformedData[day]['cloudiness']))  # given in percent values
          precipValue = list(map(float, transformedData[day]['precipitation']['value']))  # given in mm values
          # if statement to check if probability value exists as does not exist for all days
          precipProb = list(map(float, transformedData[day]['precipitation']['probability'])) if transformedData[day]['precipitation']['probability'] else []  # given in percent values
          
          # add day to combined data with fields
          combinedData[day] = {
               'temperature': {
                    'avg': sum(temperature) / len(temperature),
                    'min': min(temperature),
                    'max': max(temperature)
               },
               'wind': {
                    'direction': max(transformedData[day]['windDirection'], key=transformedData[day]['windDirection'].count),  # given as string (eg 'NW', 'S', etc)
                    'speed': sum(windSpeed) / len(windSpeed)
               },
               'humidity': sum(humidity) / len(humidity),
               'cloudiness': sum(cloudiness) / len(cloudiness),
               'precipitation': {
                    'value': sum(precipValue) / len(precipValue) if precipValue else 0,
                    'probability': sum(precipProb) / len(precipProb) if precipProb else 0
               }
          }
     return combinedData

'''
     Gets data from api and calls parsing and transforming functions
     Params:
          None
     Returns:
          Transformed data in JSON format
'''
def getData() -> str:
     response = requests.get(URL)
     # check if response is ok
     if response.status_code == 200:
          xmlData = response.text
          # parse xml data + return
          transformedData = transformer(parser(xmlData))
          return transformedData



'''
     Creates HTML table from combined data
'''
def createTable(combinedData: dict) -> str:
     # create table header with CSS for center alignment, column width, and alternating row colors
     table = '''
     <table>
     <style>
     table {
          width: 100%;
     }
     th, td {
          text-align: center;
     }
     .day {
          width: 20%;
     }
     tr:nth-child(even) {
          background-color: #f2f2f2;
     }
     </style>
     <thead>
     <tr>
     <th class="day">Day</th>
     <th>Average Temperature (°C)</th>
     <th>Minimum Temperature (°C)</th>
     <th>Maximum Temperature (°C)</th>
     <th>Wind Direction</th>
     <th>Average Wind Speed (mps)</th>
     <th>Average Humidity (%)</th>
     <th>Average Cloudiness (%)</th>
     <th>Average Precipitation Value (mm)</th>
     <th>Average Precipitation Probability (%)</th>
     </tr>
     </thead>
     <tbody>
     '''
     
     # loop through each day in combined data and add row to table
     for day in combinedData:
          table += f'<tr><td class="day">{day}</td><td>{combinedData[day]["temperature"]["avg"]:.2f}</td><td>{combinedData[day]["temperature"]["min"]:.2f}</td><td>{combinedData[day]["temperature"]["max"]:.2f}</td><td>{combinedData[day]["wind"]["direction"]}</td><td>{combinedData[day]["wind"]["speed"]:.2f}</td><td>{combinedData[day]["humidity"]:.2f}</td><td>{combinedData[day]["cloudiness"]:.2f}</td><td>{combinedData[day]["precipitation"]["value"]:.2f}</td><td>{combinedData[day]["precipitation"]["probability"]:.2f}</td></tr>'
     
     # close table
     table += '</tbody></table>'
     
     return table


def createSQLTable(rows: list[tuple]) -> str:
    # list of column names
    columns = ['day', 'temperature_avg', 'temperature_min', 'temperature_max', 'wind_direction', 'wind_speed_avg', 'humidity_avg', 'cloudiness_avg', 'precipitation_value_avg', 'precipitation_probability_avg']
    # create table header
    header = "<tr>"
    for col in columns:
        header += f"<th>{col}</th>"
    header += "</tr>"

    # create table rows
    table_rows = ""
    for row in rows:
        table_rows += "<tr>"
        for val in row:
            table_rows += f"<td>{val}</td>"
        table_rows += "</tr>"

    # combine header and rows into table
    table = f"<table>{header}{table_rows}</table>"
    return table

@application.route('/')
def index():
     # get data from API
     # parse the XML
     # manipulate the data
     uncombinedData = getData()
     # combine the data
     combinedData = combine(uncombinedData)
     # create HTML table
     table = createTable(combinedData)
     # create db if doesnt already exist
     db_funcs.create_db()
     # create table if doesnt already exist
     db_funcs.create_table()
     # insert data into db
     db_funcs.insertData(combinedData)
     # query the db to show is working
     data = db_funcs.selectAll()
     # display sql table and data
     sqlTable = createSQLTable(data)
     return render_template('index.html', table=table, sqlTable=sqlTable)

if __name__ == '__main__':
     application.run()