import os
import logging
import string

debug = True
log_convolution = False  # Log timings in convolution_2d.py
log_convolution_forward = True
log_convolution_backward = True
log_convolution_backward_data = True

wd = os.getcwd()
logdir = os.path.join(wd, "timelogs")


# Replaces "," with ":"


def csvValue(s, bad=",", good=":"):
    s = str(s)
    s = string.replace(s, bad, good)
    return s


def LogFile(logfile):
    logging.basicConfig(filename=logfile, level=logging.DEBUG)
    print("cupy logs into {}".format(logfile))

    logging.debug("Address;Parameter;Value")
    return
