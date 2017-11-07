import easygui
import subprocess
import time

flag = True
while flag:
    command = r'cmd /c nslookup sb3proxy.cordiccloud.com'
    output = subprocess.check_output(command, shell=True, universal_newlines=True)

    if str(output).find('non-existent', 0, len(output)):
        time.sleep(60)
        continue
    else:
        flag = False
        easygui.msgbox("DNS Record updated", "Time to test...")
