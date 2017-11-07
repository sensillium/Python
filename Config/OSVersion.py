__author__ = "richard.m"

# Determine the architecture of the installed OS
# Uses simple registry query
# Check for Program Files
# Check OS locale
# Check OS name

import Registry
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
    if Registry.open_reg("hklm", "SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Run"):
        return "x64"
    else:
        return "x86"


def test_os_bit():
    """ Call this to test OS version """
    try:
        if os_version() == "x64" and get_programfiles_64() == environ['PROGRAMW6432']:
            return True
        else:
            return False
    except:
        return None


def locale_detect():
    """detect the OS locale"""
    from locale import getdefaultlocale

    try:
        country_code, locale_code = getdefaultlocale()

        if country_code.lower() == "en_gb":
            os_lang = "OS is English (United Kingdom)"
            os_locale = 0
        elif country_code.lower() == "en_us":
            os_lang = "OS is English (United States)"
            os_locale = 0
        elif country_code.lower() == "fr_ch":
            os_lang = "OS is Swiss (French)"
            os_locale = 1
        elif country_code.lower() == "de_ch":
            os_lang = "OS is Swiss (German)"
            os_locale = 2
        elif country_code.lower() == "de_de":
            os_lang = "OS is German (German)"
            os_locale = 2
        elif country_code.lower() == "fr_fr":
            os_lang = "OS is French (French)"
            os_locale = 1
        else:
            # defaulting to country code en_gb
            os_lang = "Not detected, defaulting to en_gb"
            os_locale = 0
            return os_lang, os_locale
    except:
        return None, None
    else:
        return os_lang, os_locale


def os_name():
    """ detect the name of the OS from the registry """
    try:
        registry = Registry.query_reg("hklm", "Software\\Microsoft\\Windows NT\\CurrentVersion", "ProductName")

        if "7" in str(registry):
            return "w7", str(registry).split("'")[1]
        elif "8.1" in str(registry):
            return "8.1", str(registry).split("'")[1]
        elif "2008" in str(registry):
            return "s2008", str(registry).split("'")[1]
        elif "XP" in str(registry):
            return "XP", str(registry).split("'")[1]
        elif "2003" in str(registry):
            return "2003", str(registry).split("'")[1]
        else:
            return "Unrecognised", str(registry).split("'")[1]
    except:
        return None, None


if __name__ == "__main__":
    print "This is a helper, don't call explicitly"
    raw_input("Press Enter to exit")