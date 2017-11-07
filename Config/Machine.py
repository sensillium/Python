__author__ = 'richard.m'

from win32api import GetComputerName
from OSVersion import os_name, test_os_bit
import Questions
import Services


class Machine(object):
    """
    Stores information about current machine
    """

    def __init__(self):
        self.machine_name = GetComputerName()
        self.os_name_short, self.os_name_long = os_name()
        self.os_bitness = test_os_bit()
        self.vnc_password = ""
        self.cti_server = ""
        self.workgroup_name = ""
        self.using_voice_recording = True
        self.service_list = []

    def initial_config(self):
        """
        update the variables after initial questions
        :return: bool
        """
        success = []

        # workgroup
        workgroup = Questions.Workgroup()
        success.append(workgroup.name())
        self.workgroup_name = workgroup.workgroup_name
        # voice recording
        voice_recording = Questions.VoiceRecording()
        success.append(voice_recording.voice_recording())
        self.using_voice_recording = voice_recording.using_voice_recording
        # VNC
        vnc = Questions.Vnc()
        success.append(vnc.vnc_password())
        self.vnc_password = vnc.password
        # CTI
        cti = Questions.Cti()
        success.append(cti.cti_server())
        self.cti_server = cti.server
        # services
        services = Services.Services()
        self.service_list = services.running_services(self.machine_name)

        return success

    def start_services(self, service_name):
        """
        start the named service
        :param service_name: string
        :return: bool
        """

        from Services import Services
        result = Services.start_service(service_name, self.machine_name)
        if result is None:
            return None
        elif result:
            return True
        else:
            return False