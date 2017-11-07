__author__ = 'richard.m'


class Workstation(object):
    """
    Stores information about the machine as it becomes a workstation
    """
    def __init__(self):
        self.ip_address = "192.168.64."
        self.last_octet = "35"