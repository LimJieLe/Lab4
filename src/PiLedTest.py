# System imports
import socket
import time
from time import sleep


# Local imports

#from ..hal import hal_dc_motor as dc_motor


from hal import hal_led as led
from hal import hal_input_switch as switch
from hal import hal_lcd as LCD
from hal import hal_dc_motor as dc_motor
from hal import hal_buzzer as buzzer
from hal import hal_servo as servo
import version as ver

def blink_led(delay):
    # Led Blink
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
    lcd = LCD.lcd()
    if switch.read_slide_switch() == 1 :
        sleep(0.5)
        lcd.backlight(0)  # turn backlight off

        sleep(0.5)
        lcd.backlight(1)  # turn backlight on
    else :
        sleep(0.5)
        lcd.backlight(0)  # turn backlight on

if __name__ == "__main__":
    main()