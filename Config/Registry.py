__author__ = 'richard.m'

# Open registry keys for read or writing

import _winreg

with _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows NT\CurrentVersion") as key:
    registry = _winreg.QueryValueEx(key, "ProductName")

HKEY = {
    "hklm": _winreg.HKEY_LOCAL_MACHINE,
    "hkcu": _winreg.HKEY_CURRENT_USER,
    "hku": _winreg.HKEY_USERS,
    "hkcr": _winreg.HKEY_CLASSES_ROOT
}

VALUE_TYPE = {
    "reg_sz": _winreg.REG_SZ,
    "reg_dword": _winreg.REG_DWORD,
    "reg_binary": _winreg.REG_BINARY,
    "reg_expand": _winreg.REG_EXPAND_SZ,
    "reg_multi": _winreg.REG_MULTI_SZ
}


def query_reg(hkey, query_key, value):
    """
    Query a registry value
    :param hkey: string version of the HKEY to look up
    :param query_key: the rest of the key to be used as is
    :param value: the value name to return
    :return: the value with name specified
    """
    if hkey.lower() in HKEY:
        full_hkey = HKEY[hkey.lower()]
    else:
        return None

    try:
        with _winreg.OpenKey(full_hkey, query_key) as lookup_key:
            query_value = _winreg.QueryValueEx(lookup_key, value)
    except:
        return None
    else:
        return query_value


def open_reg(hkey, open_key):
    """
    Open a registry key (test for presence)
    :param hkey: string version of the HKEY to look up
    :param open_key: the rest of the key to be opened
    :return: True if they could be opened, False if not
    """
    if hkey.lower() in HKEY:
        full_hkey = HKEY[hkey.lower()]
    else:
        return None

    try:
        _winreg.OpenKey(full_hkey, open_key)
    except OSError:
        return False
    else:
        return True


def delete_reg(hkey, delete_key, value=None):
    """
    Delete a registry entry
    :param hkey: string version of the HKEY to look up
    :param delete_key: the rest of the key to be opened
    :param value: optional value name to be deleted
    :return: True if registry entry deleted, False if not
    """
    if hkey.lower() in HKEY:
        full_hkey = HKEY[hkey.lower()]
    else:
        return None

    try:
        with _winreg.OpenKey(full_hkey, delete_key) as lookup_key:
            if value is None:
                _winreg.DeleteKey(lookup_key)
            else:
                _winreg.DeleteValue(lookup_key, value)
    except:
        return False
    else:
        return True


def add_reg(hkey, add_key, value=None, value_name=None, value_type=None):
    """
    Add a registry entry
    :param hkey: string version of the HKEY to look up
    :param add_key: the rest of the key to be opened
    :param value: optional value name to be added
    :return: True if registry entry added, False if not
    """
    if hkey.lower() in HKEY:
        full_hkey = HKEY[hkey.lower()]
    else:
        return None

    try:
        with _winreg.OpenKey(full_hkey, add_key) as lookup_key:
            if value is None:
                _winreg.CreateKey(lookup_key)
            else:
                if value_type.lower() in VALUE_TYPE:
                    full_type = VALUE_TYPE[value_type.lower()]
                else:
                    return None
                _winreg.SetValueEx(full_hkey, value_name, full_type, value)
    except:
        return False
    else:
        return True


if __name__ == "__main__":
    print "This is a helper, don't call explicitly"
    raw_input("Press Enter to exit")