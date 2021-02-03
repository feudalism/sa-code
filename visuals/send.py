from DataSocket import TCPSendSocket, RAW
import threading
import sys
import time

import cv2 as cv

# Config
STOP_FLAG = threading.Event()
IP_ADDR = 'localhost'
SEND_PORT = 4040

def send_sig():
    video_filename = 'f5_dynamic_deint_L.avi'
    cap = cv.VideoCapture(video_filename)

    while cap.isOpened() and not STOP_FLAG.is_set():
        ret, frame = cap.read()
        
        if not ret:
            print('Can\'t read frame. Exiting...')
            break

        send_socket.send_data(frame)
        time.sleep(0.5)

# Main send socket function
send_socket = TCPSendSocket(tcp_port=SEND_PORT,
    tcp_ip=IP_ADDR,
    send_type=RAW)
send_socket.start()

thread = threading.Thread(target=send_sig)
thread.start()

# Stop sending
input('Press enter to stop sending data.\n')
STOP_FLAG.set()
thread.join()

print("Stopping send socket.")
send_socket.stop()
sys.exit(0)
