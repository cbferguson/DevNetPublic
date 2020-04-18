"""
Some lines are commented out.
You may or may not want to use the ipaddress library
but you will still need to check for a valid IPv4 adddress.

The 'with open('JSONdata') as f:' line will read the data file
AS LONG AS IT IS IN THE SAME DIRECTORY :)

The next line should get you started with a method you will need
from the json library to change the JSON text into something 
you can call from Python
"""
import ipaddress
import json

i=0
x=0

with open('JSONdata') as f:
    data = json.load(f)
    
for info in data:
    try:
        lanipaddress = data[i]['lanIp']
        serial_num = data[i]['serial']
        ipaddress.IPv4Address(lanipaddress)
        #print(data[i]['lanIp'] + data[i]['serial'])
        print (str(data[i]['lanIp']) + " is a Valid IP Address for Serial " + serial_num)
        i=i+1
        x=x+1
    except ValueError:
        i=i+1
        x=x+1
