# This file is executed on every boot (including wake-boot from deepsleep)
#import esp   github.com/rafgus1/IoT
#esp.osdebug(None)
try:
  import usocket as socket
except:
  import socket

from machine import Pin

import esp
esp.osdebug(None)

import gc
gc.collect()

led = Pin(2, Pin.OUT)

import network
station = network.WLAN(network.STA_IF)
station.active(True)
if not station.isconnected():
    print('connecting to network...')
    station.connect('biuroalfa', 'alfa0314')
    while not station.isconnected():
        pass
print('network config:', station.ifconfig())
import webrepl
webrepl.start()