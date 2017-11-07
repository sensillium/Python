__author__ = "richard.m"

# list all services
# find a service

from wmi import WMI


class Services(object):

    def __init__(self):
        self.services_running = []

    def running_services(self, machine_name):
        """
        get a list of running services
        :param machine_name: string
        :return: list
        """
        try:
            machine = WMI(machine_name)
            for service in machine.Win32_Service():
                self.services_running.append(service.Caption)
        except:
            return None
        else:
            return self.services_running

    def find_service(self, service_name, machine_name):
        """
        find a particular service by name (in Name or Caption)
        :param service_name: string
        :param machine_name: string
        :return: bool
        """
        try:
            for service in self.running_services(machine_name):
                if service_name in service.Caption or service_name in service.Name:
                    break
                else:
                    return False
        except:
            return None
        else:
            return True

    def stop_service(self, service_name, machine_name):
        """
        stop a particular service
        :param service_name: string
        :param machine_name: string
        :return: bool
        """
        try:
            for service in self.running_services(machine_name):
                if service_name.lower() == service.Caption or service_name.lower() == service.Name:
                    self.services_running[service_name.lower()].StopService()
                else:
                    return False
        except:
            return None
        else:
            return True

    def start_service(self, service_name, machine_name):
        """
        start a particular service
        :param service_name: string
        :param machine_name: string
        :return: bool
        """
        try:
            for service in self.running_services(machine_name):
                if service_name.lower() == service.Caption or service_name.lower() == service.Name:
                    self.services_running[service_name.lower()].StartService()
                else:
                    return False
        except:
            return None
        else:
            return True


if __name__ == "__main__":
    print "This is a helper, don't call explicitly"
    raw_input("Press Enter to exit")