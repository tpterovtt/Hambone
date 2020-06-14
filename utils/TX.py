###################################################
# FILE: tx.py                                     #
# AUTHOR: NotPike                                 #
# Function: Handles GPIO pins                     #
###################################################

import logging
import os

## Move back to root directory
import sys
sys.path.append("..")
from env import *


class TX:
    
    def __init__(self, gpio=17):
        env = ENV()

        self.GPIO = gpio
        if(os.path.isdir("/sys/class/gpio/gpio" + str(self.GPIO)) == False):
            logging.info("INIT GPIO " + str(self.GPIO) + ": OUT")

            ## Export GPIO
            stdr = os.system("echo " + str(self.GPIO) + " > /sys/class/gpio/export")
            if(stdr > 0):
                logging.critical("FAILED TO INIT GPIO")
                exit()

        ## Set GPIO to out
        stdr = os.system("echo \"out\" >  /sys/class/gpio/gpio" + str(self.GPIO) + "/direction")
        if(stdr > 0):
            logging.critical("FAILED TO SET GPIO DIRECTION")
            exit()

    def txOn(self):
        print(">>> TX ON")
        logging.info("TX ON")
        stdr = os.system("echo \"1\" > /sys/class/gpio/gpio" + str(self.GPIO) + "/value")
        if(stdr > 0):
            logging.critical("FAILED TO START TX")
            exit()

    def txOff(self):
        print(">>> TX OFF")
        logging.info("TX ON")
        stdr = os.system("echo \"0\" > /sys/class/gpio/gpio" + str(self.GPIO) + "/value")
        if(stdr > 0):
            logging.critical("FAILED TO STOP TX")
            exit()