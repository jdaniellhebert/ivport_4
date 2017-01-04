#!/usr/bin/python

import IIC
import RPi.GPIO as gp

iviic = IIC.IIC(addr=(0x70), bus_enable =(0x01))
iviic.write_control_register((0x01))                # default

gp.setwarnings(False)
gp.setmode(gp.BOARD)

gp.setup(7, gp.OUT)
gp.setup(11, gp.OUT)
gp.setup(12, gp.OUT)

gp.output(7, False)
gp.output(11, False)
gp.output(12, True)

c = ''

while c != 'q':
    c = raw_input("Enter Selection (q for quit):")
    if c == '1':
        iviic.write_control_register((0x01))
        gp.output(7, False)
        gp.output(11, False)
        gp.output(12, True)
    elif c == '2':
        iviic.write_control_register((0x02))
        gp.output(7, True)
        gp.output(11, False)
        gp.output(12, True)
    elif c == '3':
        iviic.write_control_register((0x04))
        gp.output(7, False)
        gp.output(11, True)
        gp.output(12, False)
    elif c == '4':
        iviic.write_control_register((0x08))
        gp.output(7, True)
        gp.output(11, True)
        gp.output(12, False)
    else:
        continue


gp.output(7, False)
gp.output(11, False)
gp.output(12, True)
