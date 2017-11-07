__author__ = 'richard.m'


class Workgroup(object):
    """
    Stores the details of the workgroup to be used
    """

    def __init__(self):
        self.workgroup_name = "cordic"

    def name(self):
        """
        sets self.name to chosen name
        :return: bool
        """
        try:
            answer = raw_input("Enter the workgroup name (Enter defaults to 'Cordic'): ")
            check = Check()
            if answer == "":
                self.workgroup_name = "cordic"
            else:
                self.workgroup_name = answer
            if not check.check(self.workgroup_name):
                self.name()
            else:
                return True
        except:
            return False


class VoiceRecording(object):
    """
    Ascertain if voice recording is being used
    """

    def __init__(self):
        self.using_voice_recording = True

    def voice_recording(self):
        """
        checks if voice recording is being used
        :return: bool
        """
        try:
            answer = raw_input("Is voice recording being used? (Enter defaults to 'Yes') [y/n]: ")
            check = Check()
            if answer == "y" or answer == "":
                self.using_voice_recording = True
            else:
                self.using_voice_recording = False
            if not check.check(self.using_voice_recording):
                self.voice_recording()
            else:
                return True
        except:
            return False


class Vnc(object):
    """
    Stores the details for VNC
    """

    def __init__(self):
        self.password = "12345"
        self.success = True

    def vnc_password(self):
        """
        sets self.password to chosen password
        :return: bool
        """
        try:
            answer = raw_input("Enter the VNC password (Enter defaults to '12345'): ")
            check = Check()
            if answer == "":
                self.password = "12345"
            else:
                self.password = answer
            if not check.check(self.password):
                self.vnc_password()
            else:
                return True
        except:
            return False


class Cti(object):
    """
    Asks the details for the CTI server
    """

    def __init__(self):
        self.server = "ServerStandby"

    def cti_server(self):
        """
        sets self.cti_server to chosen CTI server name
        :return: bool
        """
        try:
            check = Check()
            answer = raw_input("Enter the CTI server name (Enter defaults to 'ServerStandby'): ")
            if answer == "":
                self.server = "ServerStandby"
            else:
                self.server = answer
            if not check.check(self.server):
                self.cti_server()
            else:
                return True
        except:
            return False


class Check(object):
    """
    check the previous input
    """
    def check(self, answer):
        print "Set to: ", answer, "\n"
        if raw_input("Are you sure? [y/n]:").lower() == "y":
            return True
        else:
            return False