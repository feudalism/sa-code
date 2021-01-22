from DataSocket import TCPSendSocket, RAW

import threading
import sys
import time

from run_imu import get_imu_data

SEND_PORT = 4242
IP_ADDR = '129.69.94.93'

send_socket = TCPSendSocket(tcp_port=SEND_PORT, tcp_ip=IP_ADDR, send_type=RAW)
send_socket.start()

stop_flag = threading.Event()

def send_sig():
    while not stop_flag.is_set():
        data_as_bytes = get_imu_data()
        send_socket.send_data(data_as_bytes)
        time.sleep(0.5)

thread = threading.Thread(target=send_sig)
thread.start()

input('Press enter to stop sending.\n')
stop_flag.set()
thread.join()

send_socket.stop()
sys.exit(0)
