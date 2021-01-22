from DataSocket import TCPSendSocket, RAW

import threading
import sys
import time

from config import SEND_PORT, PI_IP_ADDR
import grk_imu

# Config
STOP_FLAG = threading.Event()

# Main send socket function
send_socket = TCPSendSocket(tcp_port=SEND_PORT, tcp_ip=PI_IP_ADDR, send_type=RAW)
send_socket.start()

def send_sig():
    while not STOP_FLAG.is_set():
        data_as_bytes = grk_imu.get_bytes()
        send_socket.send_data(data_as_bytes)
        time.sleep(0.5)

thread = threading.Thread(target=send_sig)
thread.start()

# Stop sending
input('Press enter to stop sending data.\n')
STOP_FLAG.set()
thread.join()

print("Stopping send socket.")
send_socket.stop()
sys.exit(0)
