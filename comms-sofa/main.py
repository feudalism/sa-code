"""
    Forces the end node of a beam to a new position value
    from an external data source.
    The communication with SOFA is done using PyDataSocket.
"""

from DataSocket import TCPSendSocket, NUMPY
from threading import Thread
from settings import NUMBER_OF_MESSAGES, PORT
import time, os, sys

SCRIPT_NAME = 'sofa_set_position.py'
    


# send_thread = Thread(target=sending_function)
# rec_thread = Thread(target=receiving_function)

# send_thread.start()
# rec_thread.start()

# send_thread.join()
# rec_thread.join()