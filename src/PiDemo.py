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
    switch.init()
    x = switch.read_slide_switch()
    if x == 1 :
        blink_led(200)
    else :
        led.set_output(0, 0)

if __name__ == "__main__":
    main()
    for i in range(0, 180, 5):
        servo.set_servo_position(i)
        sleep(0.05)


def test_motor():
    dc_motor.init()
    dc_motor.set_motor_speed(100)

    sleep(2)


def main():
    # Instantiate and initialize the LCD driver
    lcd = LCD.lcd()

    sleep(0.5)
    lcd.backlight(0)  # turn backlight off

    sleep(0.5)
    lcd.backlight(1)  # turn backlight on

    lcd.lcd_clear()
    lcd.lcd_display_string("DevOps for AIoT", 1)  # write on line 1
    lcd.lcd_display_string("Rel = " + ver.rel_ver, 2)  # write on line 2
    # starting on 3rd column

    sleep(2)  # wait 2 sec

    # Get IP address
    local_ip_address = socket.gethostbyname("raspberrypi")

    # Buzzer beep
    buzzer.init()
    buzzer.short_beep(0.1)

    blink_led(1)

    rotate_servo()

    test_motor()


# Main entry point
if __name__ == "__main__":
    main()
