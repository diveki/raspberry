# from gpiozero import LED, MCP3008
from raspberry_functions import read_2column_files, interpolate1d
import random, time

# ir = LED(2)
# mcp = MCP3008(channel=7)

calib_file = 'ir_calibration.csv'
volt, distance = read_2column_files(calib_file, header=True)

while True:
    current_voltage = random.uniform(0.1,2)
    # current_voltage = mcp.voltage
    current_distance = interpolate1d(volt, distance, current_voltage)
    print(f'Current distance from object is: {current_distance:.2} cm')
    time.sleep(0.2)