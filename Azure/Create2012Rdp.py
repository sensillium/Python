from azure import *
from azure.common.credentials import UserPassCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.storage import CloudStorageAccount
from azure.storage.blob.models import ContentSettings
from azure.mgmt.network import NetworkManagementClient
import easygui


def get_user_credentials():
    # show the user/password entry box
    msg = 'Enter Azure logon information'
    title = 'Azure subscription logon'
    field_names = ['Username', 'Subscription name', 'Password']
    field_values = []
    field_values = easygui.multpasswordbox(msg, title, field_names)

    while 1:
        for i in range(len(field_names)):
            errmsg = ''
            if field_values[i].strip() == '':
                errmsg = errmsg + ('"%s" is a required field.\n\n' % field_names[i])
        if errmsg == '':
            break
        field_values = easygui.multpasswordbox(errmsg, title, field_names, field_values)

    return field_values


user_name = ''
subscription_id = ''
password = ''

user_name, subscription_id, password = get_user_credentials()

credentials = UserPassCredentials(user_name, password)

resource_client = ResourceManagementClient(credentials, subscription_id)
storage_client = StorageManagementClient(credentials, subscription_id)

resource_client.resource_groups.list()

storage_client.storage_accounts.list_by_resource_group()

