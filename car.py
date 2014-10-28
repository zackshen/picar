#coding=utf-8
import time

# import RPi.GPIO as GPIO
OUT_PIN1 = 27
OUT_PIN2 = 22
OUT_PIN3 = 23
OUT_PIN4 = 24
LED_PIN  = 5


class SmartCar(object):

    def _init(self):
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(OUT_PIN1, GPIO.OUT)
        GPIO.setup(OUT_PIN2, GPIO.OUT)
        GPIO.setup(OUT_PIN3, GPIO.OUT)
        GPIO.setup(OUT_PIN4, GPIO.OUT)

    def _clear(self):
        import RPi.GPIO as GPIO
        GPIO.cleanup()

    def forward(self):
        import RPi.GPIO as GPIO
        self._init()
        GPIO.output(OUT_PIN1, True)
        GPIO.output(OUT_PIN2, False)
        GPIO.output(OUT_PIN3, True)
        GPIO.output(OUT_PIN4, False)

    def backward(self):
        import RPi.GPIO as GPIO
        self._init()
        GPIO.output(OUT_PIN1, False)
        GPIO.output(OUT_PIN2, True)
        GPIO.output(OUT_PIN3, False)
        GPIO.output(OUT_PIN4, True)

    def turn_left(self):
        import RPi.GPIO as GPIO
        self._init()
        GPIO.output(OUT_PIN1, False)
        GPIO.output(OUT_PIN2, False)
        GPIO.output(OUT_PIN3, True)
        GPIO.output(OUT_PIN4, False)

    def turn_right(self):
        import RPi.GPIO as GPIO
        self._init()
        GPIO.output(OUT_PIN1, True)
        GPIO.output(OUT_PIN2, False)
        GPIO.output(OUT_PIN3, False)
        GPIO.output(OUT_PIN4, False)

    def stop(self):
        self._clear()

    def blink(self):
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED_PIN, GPIO.OUT)
        count = 0
        while count < 3:
            GPIO.output(LED_PIN, True)
            time.sleep(0.5)
            GPIO.output(LED_PIN, False)
            time.sleep(0.5)
        self._clear()

car = SmartCar()
