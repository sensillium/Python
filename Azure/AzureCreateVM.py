from azure.servicemanagement import *


def _image_by_name(name):
        # return the first one listed, which should be the most stable
        for i in sms.list_os_images():
            if name in i.name:
                return True
        return False

subscription_id = '9f574ad2-7f16-495c-9b52-797bfcddfde6'

# The certificate comes from the local store, not from a .pem file on Windows
certificate_path = "CURRENT_USER\\Personal\\Pay-As-You-Go-8-20-2015-credentials"

# instantiate a service management service
sms = ServiceManagementService(subscription_id, certificate_path)

# Name of an os image as returned by list_os_images (catalog and yours)
image_name = 'testcopy1.vhd'
_image_by_name(image_name)

# provide a service name and location
name = 'CabGuruBeta-SS2'
location = 'West Europe'

# You can either set the location or an affinity_group
sms.create_hosted_service(service_name=name, label=name, location=location)

# Destination url://storage account/container/blob where the VM disk will be created
media_link = 'http://cabguruhdd.blob.core.windows.net/vhds/'+name+'.vhd'

# The documentation shows a Linux VM. Windows is more complicated.
# WindowsConfigurationSet contains metadata for a Windows VM
windows_config = WindowsConfigurationSet('CabGuruBeta-SS2', 'test')
# by default the api will look for domain credentials. if you want no domain:

windows_config.domain_join = None

# Here's the hard disk for the os

os_hd = OSVirtualHardDisk(image_name, media_link)

# Unless you specify endpoints, you won't be able to connect to the VM.

# The documentation is unclear on the matter.

endpoint_config = ConfigurationSet()
endpoint_config.configuration_set_type = 'NetworkConfiguration'

endpoint1 = ConfigurationSetInputEndpoint(name='rdp', protocol='tcp', port='33890', local_port='3389', load_balanced_endpoint_set_name=None, enable_direct_server_return=False)
endpoint2 = ConfigurationSetInputEndpoint(name='web', protocol='tcp', port='8080', local_port='80', load_balanced_endpoint_set_name=None, enable_direct_server_return=False)

# endpoints must be specified as elements in a list

endpoint_config.input_endpoints.input_endpoints.append(endpoint1)
endpoint_config.input_endpoints.input_endpoints.append(endpoint2)

# Finally you can deploy the VM


sms.create_virtual_machine_deployment(service_name=name,
                                      deployment_name=name,
                                      deployment_slot='production',
                                      label=name,
                                      role_name=name,
                                      system_config=windows_config,
                                      network_config=endpoint_config,
                                      os_virtual_hard_disk=os_hd,
                                      role_size='Standard_D3')
