from DataSocket import TCPReceiveSocket
import struct
import sys
import threading
from time import sleep

REC_PORT = 4242
IP_ADDR = '129.69.94.93'
stop_flag = threading.Event()

def print_data(data):
    print(data, "unpacked:", struct.unpack('ffffff', data))

receive_socket = TCPReceiveSocket(tcp_port=REC_PORT,
        tcp_ip=IP_ADDR,
        receive_as_raw=True,
        handler_function=print_data)

def start_receive_socket():
    print("Starting receive socket...")
    receive_socket.start()

thread = threading.Thread(target=start_receive_socket)
thread.start()

input("Press enter to stop receiving data.\n")
stop_flag.set()
thread.join()

print("Stopping receive socket.")
receive_socket.stop()
sys.exit(0)
