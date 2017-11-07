from azure import *
from azure.servicemanagement import *

# subscription_id = '9f574ad2-7f16-495c-9b52-797bfcddfde6'  # Core Services
subscription_id = 'c8387722-df99-4ac4-9e19-682e684b048d'    # Testing and images
certificate_path = r'D:\Downloads\ad-2016\testingandimages.pem'

sms = ServiceManagementService(subscription_id, certificate_path)

# list hosted services in the subscription
result = sms.list_hosted_services()

for service in result:
    print('Service name: ' + service.service_name)
    print('Management URL: ' + service.url)
    print('Location: ' + service.hosted_service_properties.location)
    print('')