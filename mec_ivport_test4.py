#!/usr/bin/python
# Goal with this test is to try N-1 configuration.  output of board B runs into Camera 4 on board A. So 3x cameras on each board.
# Removed the cluster connector to prevent the conflict.

import IIC
import RPi.GPIO as gp

iviic_A = IIC.IIC(addr=(0x70), bus_enable =(0x01))
iviic_B = IIC.IIC(addr=(0x71), bus_enable =(0x01))
iviic_A.write_control_register((0x01))                # default
#iviic_B.write_control_register((0x01))                # default


gp.setwarnings(False)
gp.setmode(gp.BOARD)

gp.setup(7, gp.OUT)     # Selection for all Jumpers
gp.setup(11, gp.OUT)    # Jumper A -- Enable 1
gp.setup(12, gp.OUT)    # Jumper A -- Enable 2 
gp.setup(15, gp.OUT)    # Jumper B -- Enable 1
gp.setup(16, gp.OUT)    # Jumper B -- Enable 2

# Turn off Cameras on board B
gp.output(7, False)
gp.output(15, True)
gp.output(16, True)

# Turn off Cameras on board A
gp.output(7, False)
gp.output(11, True)
gp.output(12, True)

c = ''

while c != 'q':
    c = raw_input("Enter Selection (q for quit):")
    if c == '1':
        iviic_A.write_control_register((0x01))
        # Turn on Camera 1 on board A
        gp.output(7, False)
        gp.output(11, False)
        gp.output(12, True)
    elif c == '2':
        iviic_A.write_control_register((0x02))
        # Turn on Camera 2 on board A
        gp.output(7, True)
        gp.output(11, False)
        gp.output(12, True)
    elif c == '3':
        iviic_A.write_control_register((0x04))
         # Turn on Camera 3 on board A
        gp.output(7, False)
        gp.output(11, True)
        gp.output(12, False)
    elif c == '4':
        iviic_A.write_control_register((0x08))
         # Turn on Camera 4 on board A
        gp.output(7, True)
        gp.output(11, True)
        gp.output(12, False)
        # Turn on Camera 1 on board B
        iviic_B.write_control_register((0x01))
        gp.output(7, False)
        gp.output(15, False)
        gp.output(16, True)
    elif c == '5':
        iviic_A.write_control_register((0x08))
         # Turn on Camera 4 on board A
        gp.output(7, True)
        gp.output(11, True)
        gp.output(12, False)
        # Turn on Camera 2 on board B
        iviic_B.write_control_register((0x02))
        gp.output(7, True)
        gp.output(15, False)
        gp.output(16, True)
    elif c == '6':
         # Turn on Camera 4 on board A
        gp.output(7, True)
        gp.output(11, True)
        gp.output(12, False)
        # Turn on Camera 3 on board B
        iviic_B.write_control_register((0x04))
        gp.output(7, False)
        gp.output(15, True)
        gp.output(16, False)
    else:
        continue

# Turn off Cameras on board B
gp.output(7, False)
gp.output(15, True)
gp.output(16, True)

# Turn off Cameras on board A
gp.output(7, False)
gp.output(11, True)
gp.output(12, True)
