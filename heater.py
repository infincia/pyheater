#!/usr/bin/env python

import multiprocessing
import signal
import sys


heaters = []



def signal_handler(signal, frame):
    print 'Turning off heater elements'
    for heater in heaters:
        heater.terminate()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)



def heater_element():
    """
        Completely inefficient (or perfectly efficient for the purpose?) function

    """
    while True:
        pass



def add_heater():
    heater_process = multiprocessing.Process(target=heater_element)
    heaters.append(heater_process)
    heater_process.start()


def remove_heater():
    heater_process = heaters.pop()
    heater_process.terminate()



if __name__ == '__main__':
    for cpu in range(multiprocessing.cpu_count()):
        print "Adding heater %d" % cpu
        add_heater()
