from pyfirmata import Arduino, util

board = Arduino('COM6')

board.analog[5].enable_reporting()
board.analog[4].enable_reporting()
board.digital[11].write(1)
board.digital[13].write(1)
board.digital[12].write(1)

while True:

    board.iterate()
    # print(board.analog[5].read() + " ---- " + board.analog[4].read())
    print(board.analog[4].read())
    if board.analog[4].read() == 0.0 or board.analog[4].read() == 0.001:
        board.digital[12].write(1)
    else:
        board.digital[12].write(0)

    if board.analog[5].read() == 0.0 or board.analog[5].read() == 0.001:
        board.digital[10].write(1)
    else:
        board.digital[10].write(0)
