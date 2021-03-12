# register on cloud4rpi
# kiralysandor123@gmail.com
# sudo pip install cloud4rpi
# https://github.com/cloud4rpi/cloud4rpi-raspberrypi-python
# https://cloud4rpi.io/raspberry-pi-projects/humidity-in-the-cloud
# https://cloud4rpi.io/s/2CWE6pX2N
# -*- coding: utf-8 -*-

from time import sleep
import sys, time
import cloud4rpi
import rpi
import adafruit_dht
from gpiozero import Motor
from temperature_functions import get_hum, get_temp, ventillation

# Put your device token here. To get the token,
# sign up at https://cloud4rpi.io and create a device.
DEVICE_TOKEN = 'B7uUHBqu6SCPayDjgbj1hNUHc'


# Change these values depending on your requirements.
DATA_SENDING_INTERVAL = 3  # secs
DIAG_SENDING_INTERVAL = 3  # secs
POLL_INTERVAL = 0.5  # 500 ms

dev = adafruit_dht.DHT11(3)
motor = Motor(23,24,25)

last_update = time.time()-10


def get_motor_status(m):
	return m.is_active

			
def main():

    # Put variable declarations here
    # Available types: 'bool', 'numeric', 'string', 'location'
    variables = {
        'DHT11 Temp': {
            'type': 'numeric' ,
            'bind': lambda : get_temp(dev),
        },
        'DHT11 Humidity': {
            'type': 'numeric' ,
            'bind': lambda : get_hum(dev),
        },
        'Motor On': {
            'type': 'bool',
            'value': False,
            'bind': lambda : get_motor_status(motor)
        },
        'CPU Temp': {
            'type': 'numeric',
            'bind': rpi.cpu_temp
        },
    }

    diagnostics = {
        'CPU Temp': rpi.cpu_temp,
        'IP Address': rpi.ip_address,
        'Host': rpi.host_name,
        'Operating System': rpi.os_name,
        'Client Version:': cloud4rpi.__version__,
    }
    device = cloud4rpi.connect(DEVICE_TOKEN)

    # Use the following 'device' declaration
    # to enable the MQTT traffic encryption (TLS).
    #
    # tls = {
    #     'ca_certs': '/etc/ssl/certs/ca-certificates.crt'
    # }
    # device = cloud4rpi.connect(DEVICE_TOKEN, tls_config=tls)

    try:
        device.declare(variables)
        device.declare_diag(diagnostics)

        device.publish_config()

        # Adds a 1 second delay to ensure device variables are created
        sleep(1)

        data_timer = 0
        diag_timer = 0

        while True:
            if data_timer <= 0:
                tt = get_temp(dev)
                hum = get_hum(dev)
                ventillation(motor, tt,hum)
                device.publish_data()
                data_timer = DATA_SENDING_INTERVAL

            if diag_timer <= 0:
                device.publish_diag()
                diag_timer = DIAG_SENDING_INTERVAL

            sleep(POLL_INTERVAL)
            diag_timer -= POLL_INTERVAL
            data_timer -= POLL_INTERVAL

    except KeyboardInterrupt:
        cloud4rpi.log.info('Keyboard interrupt received. Stopping...')

    except Exception as e:
        error = cloud4rpi.get_error_message(e)
        cloud4rpi.log.exception("ERROR! %s %s", error, sys.exc_info()[0])

    finally:
        sys.exit(0)


if __name__ == '__main__':
    main()
