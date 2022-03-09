from gpiozero import LED, MCP3008
from raspberry_functions import read_2column_files, interpolate1d


ir = LED(2)
mcp = MCP3008(channel=7)

calib_file = 'ir_calibration.csv'
volt, distance = read_2column_files(calib_file, header=True)

ir.on()

while True:
    current_voltage = mcp.voltage
    current_distance = interpolate1d(volt, distance, current_voltage)
    print(f'Current distance from object is: {current_distance:.2} cm')