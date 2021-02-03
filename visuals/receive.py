from DataSocket import TCPReceiveSocket

import struct
import threading
import sys
import time

import cv2 as cv

# Config
STOP_FLAG = threading.Event()
IP_ADDR = 'localhost'
REC_PORT = 4040

def show_data(data):
    print(data)
    #.imshow('frame', unpacked_data)

receive_socket = TCPReceiveSocket(tcp_port=REC_PORT,
        tcp_ip=IP_ADDR,
        receive_as_raw=True,
        handler_function=show_data)

def start_receive_socket():
    print("Starting receive socket...")
    receive_socket.start()

thread = threading.Thread(target=start_receive_socket)
thread.start()

# Stop receiving
input("Press enter to stop receiving data.\n")
STOP_FLAG.set()
thread.join()

print("Stopping receive socket.")
receive_socket.stop()
sys.exit(0)

