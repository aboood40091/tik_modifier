#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ticket Modifier
# Version v1.3
# Copyright © 2016 AboodXD

import os, sys, time

print("tik_modifier")
print("(C) 2016 AboodXD")
print("")

if len(sys.argv) != 2:
    print("Err...")
    time.sleep(3)
    sys.exit(1)
    
try:
    assert sys.argv[1].endswith('.tik')
except AssertionError:
    print("Are you sure this is a tik file?")
    time.sleep(3)
    sys.exit(1)
    
with open(sys.argv[1], "rb") as tik:
    print("Opening tik file...")
    tik1 = tik.read()
    tik.close()


tik2 = bytearray(tik1)

if tik2[0x1:0x1+1] == (1).to_bytes(1, 'big'):
    print("This tik file has already been modified!")
    time.sleep(3)
    sys.exit(1)

task = input("Did you get this tik using DiscU 4.1b or higher? [y/n]  ")

if (task == "y" or task == "Y" or task == "yes" or task == "Yes" or task == "YES" or task == "yES" or task == "yEs" or task == "yeS"):
    print("Modifing tik file...")
    tik2[0x1:0x1+1] = (1).to_bytes(1, 'big')

elif (task == "n" or task == "N" or task == "no" or task == "No" or task == "NO" or task == "nO"):
    print("Modifing tik file...")
    tik2[0x1:0x1+1] = (1).to_bytes(1, 'big')
    tik2[0xF:0xF+1] = (int.from_bytes(tik2[0xF:0xF+1], 'big') ^ 2).to_bytes(1, 'big')

name = os.path.splitext(sys.argv[1])[0]
    
with open(name + "_modified.tik", "wb+") as tik3:
    tik3.write(tik2)
    tik3.close()
    print("Modified!")
