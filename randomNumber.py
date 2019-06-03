#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# team: gowi, cc, marcel
# expert of exercise block 1: marcel

import random
import time
import sys
import matplotlib.pyplot as plt

def get_random_number(start, end):
    num = random.randint(start, end)
    return num


def write_log_file(outputfilename, data):
    f = open(outputfilename + ".log", "a")
    f.write("Our randomly generated number is " + str(data) + " (" + time.strftime("%H:%M:%S") + ")\n")
    f.close()

def get_colour_by_dice_roll(spots):

    if spots == 1:
	return "red"
    if spots == 2:
	return "blue"
    if spots == 3:
	return "black"
    if spots == 4:
	return "orange"
    if spots == 5:
	return "yellow"
    if spots == 6:
	return "green"

if __name__ == "__main__":
    outputfilename = "randomNumber"
    rolls = []
    for i in range(6):
        roll = get_random_number(1, 6)
        rolls.append(roll)
    print(rolls)
    sys.stdout.flush()
    colour = get_colour_by_dice_roll(roll)
    write_log_file(outputfilename, colour)
    print("debug print")
    plt.bar(range(6),rolls)
    plt.show()
