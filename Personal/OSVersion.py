"""
Created on 20 Mar 2014

@author: richard.m
"""
# Determine the architecture of the installed OS
# Uses simple registry query
# Check for Program Files

# imports
from _winreg import HKEY_LOCAL_MACHINE, OpenKey
from os import environ


def is_64_windows():
    """  Do not call externally """
    return 'PROGRAMFILES(X86)' in environ


def get_programfiles_32():
    """ Return the 32 bit Program Files directory """
    if is_64_windows():
        return environ['PROGRAMFILES(X86)']
    else:
        return environ['PROGRAMFILES']


def get_programfiles_64():
    """ Return the 64 bit Program Files directory """
    if is_64_windows():
        return environ['PROGRAMW6432']
    else:
        return None


def os_version():
    """ Registry test for OS version """
    try:
        areg = OpenKey(HKEY_LOCAL_MACHINE,
                               "SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Run")
    except OSError:
        return "x86"
    else:
        return "x64"


def x64_bit_os():
    """ Call this to test OS version """
    if os_version() == "x64" and get_programfiles_64() == environ['PROGRAMW6432']:
        return True
    else:
        return False


if __name__ == "__main__":
    print "This is a helper, don't call explicitly"
    raw_input("Press Enter to exit")