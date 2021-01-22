from imu import MPU6050
from config import DEVICE_ADDRESS

import time
import struct

imu = MPU6050(1, DEVICE_ADDRESS)

def print_bytes(data):
    imudata = struct.unpack('ffffff', data)
    print(f"{imudata[0]:7.3f} {imudata[1]:7.3f} {imudata[2]:7.3f}", end="    ")
    print(f"{imudata[3]:7.3f} {imudata[4]:7.3f} {imudata[5]:7.3f}")

def get_bytes():
    data = [imu.accel.x, imu.accel.y, imu.accel.z, imu.gyro.x, imu.gyro.y, imu.gyro.z]
    return struct.pack('ffffff', *data)
