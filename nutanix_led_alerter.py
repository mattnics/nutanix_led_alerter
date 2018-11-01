from flux_led import WifiLedBulb
import time

ip_address = "10.0.3.9"

led = WifiLedBulb(ip_address)

while True:
    led.turnOn()
    time.sleep(10)
    led.turnOff()
    time.sleep(10)
