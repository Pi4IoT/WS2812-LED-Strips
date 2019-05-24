#!/usr/bin/env python3

import time
from neopixel import *


def color(stri, color, wait_ms=50):
    stri.setPixelColor(0, color)
    stri.show()
    time.sleep(wait_ms/1000.0)


if __name__ == '__main__':
    strip = Adafruit_NeoPixel(1, 18, 800000, 10, False, 255,0)
    strip.begin()



    for i in range(50):
        print (i)
        color(strip, Color(i, 0, 0))  # Red wipe
        color(strip, Color(0, i, 0))  # Blue wipe
        color(strip, Color(0, 0, i))  # Green wipe


    color(strip, Color(0,0,0), 255)
