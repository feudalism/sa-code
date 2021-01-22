from imu import MPU6050
import time
import struct

DEVICE_ADDRESS = 0x68
imu = MPU6050(1, DEVICE_ADDRESS)

def print_imu_data():
    print("    a_x     a_y     a_z        g_x     g_y     g_z")
    while True:
        print(f"{imu.accel.x:7.3f} {imu.accel.y:7.3f} {imu.accel.z:7.3f}", end="    ")
        print(f"{imu.gyro.x:7.3f} {imu.gyro.y:7.3f} {imu.gyro.z:7.3f}")
        time.sleep(1)

def get_imu_data():
    data = [imu.accel.x, imu.accel.y, imu.accel.z, imu.gyro.x, imu.gyro.y, imu.gyro.z]
    return struct.pack('ffffff', *data)
