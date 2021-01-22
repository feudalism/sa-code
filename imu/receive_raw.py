from DataSocket import TCPReceiveSocket

import struct
import sys
import threading
import time

from config import REC_PORT, PI_IP_ADDR, IMU_HEADER

# Config
STOP_FLAG = threading.Event()

def print_data(data):
    imudata = struct.unpack('ffffff', data)
    print(f"{imudata[0]:7.3f} {imudata[1]:7.3f} {imudata[2]:7.3f}", end="    ")
    print(f"{imudata[3]:7.3f} {imudata[4]:7.3f} {imudata[5]:7.3f}")

# Main receive socket function
receive_socket = TCPReceiveSocket(tcp_port=REC_PORT,
        tcp_ip=PI_IP_ADDR,
        receive_as_raw=True,
        handler_function=print_data)

def start_receive_socket():
    print("Starting receive socket...")
    print(IMU_HEADER)
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
