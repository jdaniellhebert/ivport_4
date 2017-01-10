#!/usr/bin/python
# Original configuration switch alternate disabling of mux on boards
#

import IIC
import RPi.GPIO as gp

iviic_A = IIC.IIC(addr=(0x70), bus_enable =(0x00))                                  # IIC port A defined and disabled
iviic_B = IIC.IIC(addr=(0x71), bus_enable =(0x00))                                  # IIC port B defined and disabled

gp.setwarnings(False)
gp.setmode(gp.BOARD)

gp.setup(7, gp.OUT)                                                                 # Selection for all Jumpers
gp.setup(11, gp.OUT)                                                                # Jumper A -- Enable 1
gp.setup(12, gp.OUT)                                                                # Jumper A -- Enable 2 
gp.setup(15, gp.OUT)                                                                # Jumper B -- Enable 1
gp.setup(16, gp.OUT)                                                                # Jumper B -- Enable 2

iviic_A.write_control_register((0x00))                                              # Disable IIC mux board A
gp.output(11, True); gp.output(12, True); gp.output(7, False);                      # Turn off Cameras on board A

iviic_B.write_control_register((0x00))                                              # Disable IIC mux board B
gp.output(15, True); gp.output(16, True); gp.output(7, False);                      # Turn off Cameras on board B

c = ''

while c != 'q':
    c = raw_input("Enter Selection (q for quit):")
    if c == '1':
        # Disable board B
        iviic_B.write_control_register((0x00))                                      # Disable IIC mux board B
        gp.output(15, True); gp.output(16, True); gp.output(7, False);              # Turn off Cameras on board B
        # Enable board A AND enable camera 1
        iviic_A.write_control_register((0x01))                                      # Mux1(A) Enabled
        gp.output(11, False); gp.output(12, True); gp.output(7, False);             # EN1(A) = False; EN2(A)=True; SEL = False
        
    elif c == '2':
        # Disable board B
        iviic_B.write_control_register((0x00))                                      # Disable IIC mux board B
        gp.output(15, True); gp.output(16, True); gp.output(7, False);              # Turn off Cameras on board B
        # Enable board A AND enable camera 2
        iviic_A.write_control_register((0x02))                                      # Mux2(A) Enabled
        gp.output(11, False); gp.output(12, True); gp.output(7, True);              # EN1(A) = False; EN2(A)=True; SEL = True
        
    elif c == '3':
        # Disable board B
        iviic_B.write_control_register((0x00))                                      # Disable IIC mux board B
        gp.output(15, True); gp.output(16, True); gp.output(7, False);              # Turn off Cameras on board B
        # Enable board A AND enable camera 3
        iviic_A.write_control_register((0x04))                                      # Mux3(A) Enabled
        gp.output(11, True); gp.output(12, False); gp.output(7, False);              # EN1(A) = True; EN2(A)=False; SEL = False
        
    elif c == '4':
        # Disable board B
        iviic_B.write_control_register((0x00))                                      # Disable IIC mux board B
        gp.output(15, True); gp.output(16, True); gp.output(7, False);              # Turn off Cameras on board B
        # Enable board A AND enable camera 4
        iviic_A.write_control_register((0x08))                                      # Mux0(A) Enabled
        gp.output(11, True); gp.output(12, False); gp.output(7, True);             # EN1(A) = True; EN2(A)=False; SEL = True
        
    elif c == '5':
        # Disable board A
        iviic_A.write_control_register((0x00))                                      # Disable IIC mux board A
        gp.output(11, True); gp.output(12, True); gp.output(7, False);              # Turn off Cameras on board A
        # Enable board B AND enable camera 5
        iviic_B.write_control_register((0x01))                                      # Mux1(B) Enabled
        gp.output(15, False); gp.output(16, True); gp.output(7, False);             # EN1(B) = False; EN2(B)=True; SEL = False
        
    elif c == '6':
        # Disable board A
        iviic_A.write_control_register((0x00))                                      # Disable IIC mux board A
        gp.output(11, True); gp.output(12, True); gp.output(7, False);              # Turn off Cameras on board A
        # Enable board B AND enable camera 6
        iviic_B.write_control_register((0x02))                                      # Mux2(B) Enabled
        gp.output(15, False); gp.output(16, True); gp.output(7, True);              # EN1(B) = False; EN2(B)=True; SEL = True

    continue

iviic_B.write_control_register((0x00))                                              # Disable IIC mux board B
gp.output(15, True); gp.output(16, True); gp.output(7, False);                      # Turn off Cameras on board B

iviic_A.write_control_register((0x00))                                              # Disable IIC mux board A
gp.output(11, True); gp.output(12, True); gp.output(7, False);                      # Turn off Cameras on board A
