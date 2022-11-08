import time

from hal import hal_led as led
from hal import hal_input_switch as switch

def blink_led(delay):
    led.init()

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)

def main():
    led.init()
    switch.init()
    x = switch.read_slide_switch()
    if x == 1 :
        blink_led(1)
    else :
        led.set_output(0, 0)

if __name__ == "__main__":
    main()