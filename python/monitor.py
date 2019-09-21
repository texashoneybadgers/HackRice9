from pyfirmata import Arduino, util
import time

# Initializes board
board = Arduino('COM6')

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