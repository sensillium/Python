from azure import *
from azure.servicemanagement import *

# subscription_id = '9f574ad2-7f16-495c-9b52-797bfcddfde6'  # Core Services
subscription_id = 'c8387722-df99-4ac4-9e19-682e684b048d'    # Testing and images
certificate_path = r'D:\Downloads\testingandimages.pem'

sms = ServiceManagementService(subscription_id, certificate_path)

name = 'python-test'
label = 'python-test'
desc = 'Python 3.6 x64 test'
location = 'North Europe'

result = sms.create_hosted_service(name, label, desc, location)

print('Operation status: ' + sms.get_operation_status(result.request_id))
