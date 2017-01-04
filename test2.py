#!/usr/bin/python
#
# This file is part of Ivport.
# Copyright (C) 2015 Ivmech Mechatronics Ltd. <bilgi@ivmech.com>
#
# Ivport is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ivport is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#title           :ivport_test_A.py
#description     :test ivport camera multiplexer
#author          :Caner Durmusoglu
#date            :20150425
#version         :0.1
#usage           :python ivport_test_A.py
#notes           :A indicates that Ivport jumper setting
#python_version  :2.7
#==============================================================================
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
