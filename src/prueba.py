import serial
import time

ser = serial.Serial('COM3', 9600)
time.sleep(2)

try:
    while True:
        line = ser.readline().decode('utf-8').strip()
        sensor_value = float(line)
        print(f'Sensor Value: %.4f' % sensor_value)
except KeyboardInterrupt:
    print("Finalizando lectura serial.")
finally:
    ser.close()
