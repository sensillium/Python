from azure import *
from azure.servicemanagement import *


testing_subscription_id = 'c8387722-df99-4ac4-9e19-682e684b048d'    # Testing and images
testing_certificate_path = r'D:\Downloads\ad-2016\testingandimages.pem'

coreservices_subscription_id = '9f574ad2-7f16-495c-9b52-797bfcddfde6'  # Core Services
coreservices_certificate_path = r'D:\Downloads\ad-2016\coreservices.pem'

testing_sms = ServiceManagementService(testing_subscription_id, testing_certificate_path)
coreservices_sms = ServiceManagementService(coreservices_subscription_id, coreservices_certificate_path)

# disks
source_disk_sm_os = None
source_disk_sm_data1 = None
source_disk_sm_data2 = None
source_disk_sm_data3 = None
source_disk_gw_os = None
source_disk_gw_data = None
source_disk_ss_os = None
source_disk_sr_os = None

# images
dest_image_sm_os = None
dest_image_sm_data0 = None
dest_image_sm_data1 = None
dest_image_sm_data2 = None
dest_image_gw_os = None
dest_image_gw_data = None
dest_image_ss_os = None
dest_image_sr_os = None

# source infrastructure variables

# dest infrastructure variables
dest_vm_sm_name = 'servermain'
dest_vnet_name = 'test-cng'
dest_storage_name = 'testcng'
dest_location = 'North Europe'
dest_cloudservice_name = 'test-cng'


# todo: create destination cloud service
testing_cloud_service_result = testing_sms.create_hosted_service(dest_cloudservice_name, dest_cloudservice_name,
                                                                 dest_cloudservice_name, dest_location)
print('Operation status: ' + testing_sms.get_operation_status())

# todo: create destination storage account
testing_storage_account_result = testing_sms.create_storage_account(dest_storage_name, dest_storage_name,
                                                                    dest_storage_name, location=dest_location)
print('Operation status: ' + testing_sms.get_operation_status())

# todo: create destination vnet


# todo: create destination VMs

