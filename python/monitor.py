from pyfirmata import Arduino, util
import time
import requests
import json

# REST url
URL = "http://localhost:8080/api/locks/"

# Initializes board
# board = Arduino('COM6')
board = Arduino('/dev/cu.usbmodem1412401')

count = 0

# Booleans for determining stall vacancy
isOccupiedOne = False
isOccupiedTwo = False

# Sets analog pins to be able to read voltage
board.analog[5].enable_reporting()
board.analog[4].enable_reporting()

# Sets pins 11 and 13 to HIGH
board.digital[11].write(1)
board.digital[13].write(1)

# Continuously loop
while True:

    board.iterate()  # Makes the board cycle to refresh analog readings
    
    # Setting some preconditions
    occupiedStatusOne = isOccupiedOne
    occupiedStatusTwo = isOccupiedTwo

    # If the analog for latch one reads LOW, set pin 12 to HIGH, the stall is vacant
    # If the analog for latch one reads HIGH, set pin 12 to LOW, the stall is occupied
    if board.analog[4].read() == 0.0 or board.analog[4].read() == 0.001:
        board.digital[12].write(1)
        isOccupiedOne = False
    else:
        board.digital[12].write(0)
        isOccupiedOne = True

    # If the analog for latch two reads LOW, set pin 10 to HIGH, the stall is vacant
    # If the analog for latch two reads HIGH, set pin 10 to LOW, the stall is occupied
    if board.analog[5].read() == 0.0 or board.analog[5].read() == 0.001:
        board.digital[10].write(1)
        isOccupiedTwo = False
    else:
        board.digital[10].write(0)
        isOccupiedTwo = True

    # If precondition is different from postcondition
    if isOccupiedOne !=  occupiedStatusOne:
        ID = '5d858e0c62cf6efd43957f97'
        data = {}
        if isOccupiedOne:
            data = {'name': 'Lock Hack',
                    'location': '1st Floor',
                    'status': 1,
                    'reserved': 0}
        else:
            data = {'name': 'Lock Hack',
                    'location':'1st Floor',
                    'status': 0,
                    'reserved': 0}

        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.patch(URL + ID, data=json.dumps(data), headers=headers)
    if isOccupiedTwo !=  occupiedStatusTwo:
        ID = '5d858e1b62cf6efd43957f98'
        data = {}
        if isOccupiedTwo:
            data = {'name': 'Lock Rice',
                    'location': '2nd Floor',
                    'status': 1,
                    'reserved': 0}
        else:
            data = {'name': 'Lock Rice',
                    'location': '2nd Floor',
                    'status': 0,
                    'reserved': 0}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.patch(URL + ID, data=json.dumps(data), headers=headers)
