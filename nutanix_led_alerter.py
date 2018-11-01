from flux_led import WifiLedBulb

ip_address = "10.0.3.9"

leds = flux_led.WifiLedBulb(ip_address)

while true:
    led.turnOn()
    wait 10
    led.turnOff()