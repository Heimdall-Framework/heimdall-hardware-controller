import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

relay_controller_pin=7
GPIO.setup(relay_controller_pin, GPIO.OUT)

def trigger_relay(delay):
    GPIO.output(relay_controller_pin, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(relay_controller_pin, GPIO.LOW)
