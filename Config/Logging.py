__author__ = 'richard.m'

# For writing output to the log

import logging

try:
    logging.basicConfig(filename="C:\\log\\config.log",
                        format="%(asctime)s %(levelname)s: %(message)s",
                        datefmt="%d/%m/%Y %H:%M:%S",
                        level=logging.DEBUG)
except IOError:
    print """
    ****************************
    *                          *
    *  Run as Administrator!!  *
    *                          *
    ****************************
    """


def log_i(message, args=None):
    """
    :param message: the text message to be displayed in the log file
    :param args: string.format substitutions
    :return: information message
    """
    if args is None:
        logging.info(message)
    else:
        logging.info(message, args)
        message = message % args

    print "{:15s} {:50s}".format("INFO:", message)


def log_w(message, args=None):
    """
    :param message: the text message to be displayed in the log file
    :param args: string.format substitutions
    :return: warning message
    """
    if args is None:
        logging.warning(message)
    else:
        logging.warning(message, args)
        message = message % args

    print "{:15s} {:50s}".format("WARNING:", message)


def log_e(message, args=None):
    """
    :param message: the text message to be displayed in the log file
    :param args: string.format substitutions
    :return: error message
    """
    if args is None:
        logging.error(message)
    else:
        logging.error(message, args)
        message = message % args

    print "{:15s} {:50s}".format("ERROR:", message)


def log_d(message, args=None):
    """
    :param message: the text message to be displayed in the log file
    :param args: string.format substitutions
    :return: debug message
    """
    if args is None:
        logging.debug(message)
    else:
        logging.debug(message, args)
        message = message % args

    print "{:15s} {:50s}".format("DEBUG:", message)


def failed(message, args=None):
    """
    Exit the program after reporting failure
    :param message: string
    :param args: string
    :return: void
    """
    if args is None:
        logging.error(message)
    else:
        logging.error(message, args)
        message = message % args

    print "{:15s}".format("********************************")
    print "{:15s} {:50s}".format("FATAL:", message)
    print "{:15s}".format("********************************")
    raw_input("Press Enter to quit")
    from sys import exit
    exit(0)

if __name__ == "__main__":
    print "This is a helper, don't call explicitly"
    raw_input("Press Enter to exit")