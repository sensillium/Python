__author__ = 'richard.m'

import Logging
#import Config


def log_test():
    Logging.log_d("debug %s message", "test")

    Logging.log_e("error message")

    Logging.log_i("information message %s", "test")

    Logging.log_w("warning message")


def service_test():
    import Services
    import Machine

    service_list = Services.running_services(Machine.machine_name)
    if service_list is None:
        Logging.log_e("Failed to discover services on %s", Machine.machine_name)
    else:
        Logging.log_i("Discovered services on %s", Machine.machine_name)
        print service_list[:]


def os_test():
    import OSVersion

    # os version
    if OSVersion.test_os_bit():
        Logging.log_i("OS is 64 bit")
    elif not OSVersion.test_os_bit():
        Logging.log_i("OS is 32 bit")
    elif OSVersion.test_os_bit() is None:
        Logging.log_e("Failed to discover OS bitness")
    else:
        Logging.log_d("OS bitness test abnormal termination in test")

    # os language
    lang, locale = OSVersion.locale_detect()
    if lang is None or locale is None:
        Logging.log_e("Failed to detect OS language")
    else:
        Logging.log_i(lang)
        Logging.log_i("Locale set to %s", locale)

    # os name
    shorter, longer = OSVersion.os_name()
    if shorter is None or longer is None:
        Logging.log_e("Unrecognised OS name", longer)
    else:
        Logging.log_i(longer)


def reg_test():
    import Registry

    # reg function testing
    if Registry.open_reg("hklm", "SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Run"):
        Logging.log_i("x64")
    else:
        Logging.log_i("x86")


def questions_test():
    from Questions import Workgroup, VoiceRecording, Vnc

    # set the workgroup name
    workgroup = Workgroup()
    if workgroup.name():
        Logging.log_i("Set work group name to %s", workgroup.workgroup_name)
    else:
        Logging.log_w("Workgroup name not set")

    voice_recording = VoiceRecording()
    if voice_recording.voice_recording():
        Logging.log_i("Set voice recording to %s", voice_recording.using_voice_recording)
    else:
        Logging.log_w("Voice recording not set")


#log_test()

#service_test()

#os_test()

#reg_test()

questions_test()