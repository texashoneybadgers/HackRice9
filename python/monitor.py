from pyfirmata import Arduino, util

board = Arduino('COM6')

board.digital[8].write(1)
board.analog[5].enable_reporting()
board.digital[11].write(1)


while True:

    board.iterate()
    print(board.analog[5].read())

    if board.analog[5].read() == 0.0:
        board.digital[10].write(1)
    else:
        board.digital[10].write(0)