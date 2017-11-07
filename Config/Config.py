__author__ = 'richard.m'
__version__ = "$Revision: 1.1$"

import Logging
from Machine import Machine

SQL_SERVICE = "MSSQLSERVER"
this_computer = Machine()

# Begin logging
Logging.log_i("Beginning Config on %s", this_computer.machine_name)
Logging.log_i("OS is %s", this_computer.os_name_long)
if this_computer.os_bitness:
    Logging.log_i("64 bit")
elif not this_computer.os_bitness:
    Logging.log_i("32 bit")
else:
    Logging.log_w("Abnormal return in OS bitness test")

# Ask initial questions
# Compile the list of services on the machine
# Ask workgroup question
if False in this_computer.initial_config():
    Logging.failed("Failed during initial setup")
else:
    Logging.log_i("Set workgroup name to '%s'", this_computer.workgroup_name)
    Logging.log_i("Set voice recording to '%s'", this_computer.using_voice_recording)
    Logging.log_i("Set VNC password to '%s'", this_computer.vnc_password)
    Logging.log_i("Set CTI server name to '%s'", this_computer.cti_server)

#todo: start sql service
result = Machine.start_services(SQL_SERVICE)
if result is None:
    Logging.failed("Failed to start SQL Server service")
elif result:
    Logging.log_i("Started SQL Server Service")
else:
    Logging.log_w("%s service not found") % SQL_SERVICE


#todo: start VR daemon at the end to prevent entry being written to computer table

#todo: test to see if trusted connection is open
#todo: open secureasset if not


#todo: select machine type; server or workstation