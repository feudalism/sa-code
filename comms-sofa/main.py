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
    
# def sending_function():
    # """ Creates a send socket to transmit sample data. """
    # send_socket = TCPSendSocket(tcp_port=PORT, send_type=NUMPY)
    # send_socket.start(blocking=True)

    # # sample data: 1, 2, ... 6
    # for i in range(NUMBER_OF_MESSAGES):
        # print(f"\t sending! {i+1}")
        # send_socket.send_data(i+1)
        # time.sleep(1.5)

    # print("closing send socket.")
    # send_socket.stop()
    
# def receiving_function():
    # """ Runs SOFA with the Python script to change the y-position value
        # of the end node of a beam.
        
        # A receive socket is started from within the simulation
        # once the graph is initialised.
        # The y-position of the end node is given by the data received
        # from the send socket.
    # """    

# send_thread = Thread(target=sending_function)
# rec_thread = Thread(target=receiving_function)

# send_thread.start()
# rec_thread.start()

# send_thread.join()
# rec_thread.join()