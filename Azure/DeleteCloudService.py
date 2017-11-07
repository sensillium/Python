from azure import *
from azure.servicemanagement import *

# subscription_id = '9f574ad2-7f16-495c-9b52-797bfcddfde6'  # Core Services
subscription_id = 'c8387722-df99-4ac4-9e19-682e684b048d'    # Testing and images
certificate_path = r'D:\Downloads\ad-2016\testingandimages.pem'

sms = ServiceManagementService(subscription_id, certificate_path)

service_to_delete = 'python-test'
sms.delete_hosted_service(service_to_delete)